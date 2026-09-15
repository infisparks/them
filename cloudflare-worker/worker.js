/**
 * Cloudflare Worker for InfiSparks Digital Theme Store & WhatsApp Automation
 * Domain: https://digitalthem.infisparks.workers.dev
 * Handles:
 * 1. Razorpay Payment Verification & License Generation
 * 2. Razorpay Server Webhooks (payment.captured / order.paid)
 * 3. Instant Lead Capture into Firebase RTDB (even if user abandons / doesn't pay)
 * 4. Automatic Customer License Delivery via Evolution API (instance: mudassir)
 * 5. Automatic Admin Sales Alert via Evolution API (instance: mudassir)
 * 6. Direct WhatsApp Proxy Forwarding for external services
 */

// =============================================================================
// CONFIGURATION & CREDENTIALS
// =============================================================================
const CONFIG = {
  // Firebase Realtime Database
  FIREBASE_DB_URL: "https://awdeveloper-f2b8a-default-rtdb.firebaseio.com",
  FIREBASE_SECRET: "Yo5r6sDdNUjBGXdN4xHHsI2wJpW0trjxFzcYjf5r",

  // Razorpay
  RAZORPAY_KEY_ID: "rzp_live_TbySDUVsA57Ndi",
  RAZORPAY_KEY_SECRET: "epCcF2GzdKH4OCH5snsO3oY0",
  RAZORPAY_WEBHOOK_SECRET: "epCcF2GzdKH4OCH5snsO3oY0",

  // Evolution WhatsApp API
  EVO_BASE_URL: "https://evo.infisparks.in",
  EVO_API_KEY: "vR39h6avY69g7kAU3YQbS6V6XEvudson",
  EVO_INSTANCE: "mudassir", // Active verified instance

  // Admin Notification WhatsApp
  ADMIN_WHATSAPP: "919958399157",

  // Portal URL
  PORTAL_URL: "https://them-delta.vercel.app/purchase"
};

// Standard CORS headers allowing requests from any origin
const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, apikey, X-Razorpay-Signature",
};

// Format phone to standard E.164 digits without '+'
function cleanPhoneNumber(phone) {
  if (!phone) return "";
  let digits = String(phone).replace(/\D/g, "");
  if (digits.length === 10) digits = "91" + digits; // Default to India 91 prefix
  return digits;
}

// Generate License Key: LIC-45LP-XXXX-XXXX
function generateLicenseKey() {
  const chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  let p1 = "", p2 = "";
  for (let i = 0; i < 4; i++) p1 += chars.charAt(Math.floor(Math.random() * chars.length));
  for (let i = 0; i < 4; i++) p2 += chars.charAt(Math.floor(Math.random() * chars.length));
  return `LIC-45LP-${p1}-${p2}`;
}

// Firebase Realtime Database REST API Helper
async function firebaseDb(path, method = "GET", body = null) {
  const url = `${CONFIG.FIREBASE_DB_URL}/${path}.json?auth=${encodeURIComponent(CONFIG.FIREBASE_SECRET)}`;
  const options = {
    method,
    headers: { "Content-Type": "application/json" }
  };
  if (body && method !== "GET") {
    options.body = JSON.stringify(body);
  }
  const res = await fetch(url, options);
  if (!res.ok) {
    const errText = await res.text();
    console.error(`[Firebase Error ${res.status}] ${path}:`, errText);
    throw new Error(`Firebase Error: ${errText}`);
  }
  return await res.json();
}

// Evolution API WhatsApp Sender (Using instance: mudassir)
async function sendWhatsAppViaEvo(number, text, instance = null, apiKey = null) {
  const targetInstance = instance || CONFIG.EVO_INSTANCE; // Default: mudassir
  const targetKey = apiKey || CONFIG.EVO_API_KEY; // Default: vR39h6avY69g7kAU3YQbS6V6XEvudson
  const cleanNumber = cleanPhoneNumber(number);

  if (!cleanNumber) {
    console.warn("[WhatsApp] Invalid phone number, aborting send.");
    return false;
  }

  const targetUrl = `${CONFIG.EVO_BASE_URL}/message/sendText/${targetInstance}`;
  try {
    const res = await fetch(targetUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "apikey": targetKey,
      },
      body: JSON.stringify({ number: cleanNumber, text: text }),
    });

    const data = await res.text();
    console.log(`[Evolution WhatsApp Sent via ${targetInstance} to ${cleanNumber}]:`, data);
    return true;
  } catch (err) {
    console.error(`[Evolution WhatsApp Error via ${targetInstance}]:`, err);
    return false;
  }
}

// HMAC-SHA256 signature verification for Razorpay Webhooks
async function verifyWebhookSignature(rawBody, signature, secret) {
  if (!signature || !secret) return false;
  try {
    const encoder = new TextEncoder();
    const key = await crypto.subtle.importKey(
      "raw",
      encoder.encode(secret),
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign"]
    );
    const sigBuffer = await crypto.subtle.sign("HMAC", key, encoder.encode(rawBody));
    const hex = Array.from(new Uint8Array(sigBuffer))
      .map((b) => b.toString(16).padStart(2, "0"))
      .join("");
    return hex.toLowerCase() === signature.toLowerCase();
  } catch (err) {
    console.error("[Crypto Error] Webhook signature verification error:", err);
    return false;
  }
}

// Format customer delivery WhatsApp message
function createCustomerWhatsAppMessage(name, licenseKey, phone) {
  const clean = cleanPhoneNumber(phone);
  const portalLink = `${CONFIG.PORTAL_URL}/?key=${encodeURIComponent(licenseKey)}&phone=${encodeURIComponent(clean)}`;

  return `🎉 *Payment Confirmed! Access Your 45+ Landing Page Bundle*

Hello *${name || "Customer"}*,
Thank you for purchasing the *45+ Ultimate Landing Page Bundle*! 🚀

🔑 *Your Official Commercial License Key:*
\`${licenseKey}\`

📥 *Click to Unlock & Download Complete Source Codes:*
${portalLink}

✨ *What You Received:*
✅ Full lifetime access to all 45+ production landing pages
✅ 100% Commercial Client & Personal Usage Rights
✅ 1-Click ZIP Source Code Downloads (Clean unencrypted HTML, Tailwind CSS, JS)
✅ Future updates & luxury templates included

💡 *Quick Tip:* Bookmark your customer portal link above so you can access and download your templates anytime.

Need bespoke custom landing page design, domain connection, or support? Simply reply directly to this WhatsApp chat!`;
}

// Format admin notification message
function createAdminWhatsAppAlert(name, phone, amount, paymentId, licenseKey) {
  return `💰 *New Theme Bundle Sale Received!*

👤 *Customer:* ${name || "Anonymous"}
📱 *WhatsApp:* +${cleanPhoneNumber(phone)}
💵 *Amount:* ₹${amount || 399}
💳 *Payment ID:* ${paymentId || "N/A"}
🔑 *License Key:* \`${licenseKey}\`
📅 *Time:* ${new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" })}`;
}

// =============================================================================
// MAIN WORKER FETCH HANDLER
// =============================================================================
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // 1. Handle CORS Preflight OPTIONS Request
    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: corsHeaders,
      });
    }

    // 2. Health Check
    if (request.method === "GET" && (url.pathname === "/" || url.pathname === "/api/health")) {
      return new Response(
        JSON.stringify({
          status: "online",
          service: "InfiSparks Digital Theme Store & WhatsApp Backend",
          instance: CONFIG.EVO_INSTANCE,
          razorpay_key: CONFIG.RAZORPAY_KEY_ID,
          version: "2.5.0",
          timestamp: new Date().toISOString(),
        }),
        { headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    // 3. POST /api/leads - Save lead (Even if visitor abandons / does not pay)
    if (url.pathname === "/api/leads" && request.method === "POST") {
      try {
        const body = await request.json();
        const name = body.name || "Anonymous";
        const phone = cleanPhoneNumber(body.phone);
        const amount = body.amount || 399;
        const status = body.status || "pending";

        const leadRecord = {
          name,
          phone: body.phone,
          cleanPhone: phone,
          amount,
          status,
          source: body.source || "checkout_modal",
          timestamp: Date.now(),
          createdAt: new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" }),
        };

        const saved = await firebaseDb("leads", "POST", leadRecord);

        return new Response(
          JSON.stringify({ success: true, message: "Lead saved successfully", id: saved.name }),
          { headers: { ...corsHeaders, "Content-Type": "application/json" } }
        );
      } catch (err) {
        return new Response(
          JSON.stringify({ success: false, error: err.message }),
          { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
        );
      }
    }

    // 4. POST /api/verify-payment - Client Success Callback from Razorpay Checkout
    if (url.pathname === "/api/verify-payment" && request.method === "POST") {
      try {
        const body = await request.json();
        const {
          razorpay_payment_id,
          razorpay_order_id,
          razorpay_signature,
          name,
          phone,
          amount = 399,
        } = body;

        const cleanPhone = cleanPhoneNumber(phone);

        if (!razorpay_payment_id) {
          return new Response(
            JSON.stringify({ success: false, error: "Missing razorpay_payment_id" }),
            { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
          );
        }

        // Check if license already exists for this payment (idempotent)
        const allLicenses = (await firebaseDb("licenses")) || {};
        let existingKey = Object.keys(allLicenses).find(
          (k) => allLicenses[k] && allLicenses[k].paymentId === razorpay_payment_id
        );

        let licenseKey = existingKey;
        if (!licenseKey) {
          licenseKey = generateLicenseKey();

          const licenseRecord = {
            key: licenseKey,
            name: name || "Verified Customer",
            phone: phone || "",
            cleanPhone: cleanPhone,
            paymentId: razorpay_payment_id,
            orderId: razorpay_order_id || "",
            amount: Number(amount) || 399,
            tier: "Commercial Lifetime License",
            status: "active",
            verified: true,
            createdAt: new Date().toISOString(),
            dateFormatted: new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" }),
            downloadsCount: 0,
          };

          // Save License into Firebase
          await firebaseDb(`licenses/${licenseKey}`, "PUT", licenseRecord);

          // Save / Update Lead to Paid
          await firebaseDb("leads", "POST", {
            name: name || "Customer",
            phone: phone || "",
            cleanPhone: cleanPhone,
            amount: Number(amount) || 399,
            status: "paid",
            paymentId: razorpay_payment_id,
            licenseKey: licenseKey,
            timestamp: Date.now(),
            createdAt: new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" }),
          });

          // Dispatch WhatsApp Delivery to Customer via Evolution API instance "mudassir"
          const customerMsg = createCustomerWhatsAppMessage(name, licenseKey, cleanPhone);
          ctx.waitUntil(sendWhatsAppViaEvo(cleanPhone, customerMsg, CONFIG.EVO_INSTANCE));

          // Dispatch Alert to Admin WhatsApp (+91 99583 99157)
          const adminMsg = createAdminWhatsAppAlert(name, cleanPhone, amount, razorpay_payment_id, licenseKey);
          ctx.waitUntil(sendWhatsAppViaEvo(CONFIG.ADMIN_WHATSAPP, adminMsg, CONFIG.EVO_INSTANCE));
        }

        const purchaseUrl = `${CONFIG.PORTAL_URL}/?key=${encodeURIComponent(licenseKey)}&phone=${encodeURIComponent(cleanPhone)}`;

        return new Response(
          JSON.stringify({
            success: true,
            licenseKey,
            purchaseUrl,
            message: "Payment verified, license generated and WhatsApp dispatched successfully",
          }),
          { headers: { ...corsHeaders, "Content-Type": "application/json" } }
        );
      } catch (err) {
        return new Response(
          JSON.stringify({ success: false, error: err.message }),
          { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
        );
      }
    }

    // 5. POST /api/razorpay-webhook - Server-to-Server Razorpay Webhook
    if (url.pathname === "/api/razorpay-webhook" && request.method === "POST") {
      try {
        const rawBody = await request.text();
        const signature = request.headers.get("x-razorpay-signature");

        const webhookSecret = env?.RAZORPAY_WEBHOOK_SECRET || CONFIG.RAZORPAY_WEBHOOK_SECRET;
        const isValid = await verifyWebhookSignature(rawBody, signature, webhookSecret);

        if (!isValid) {
          console.warn("[Razorpay Webhook ❌] Invalid webhook signature.");
          return new Response(JSON.stringify({ error: "Invalid signature" }), {
            status: 400,
            headers: { "Content-Type": "application/json" },
          });
        }

        const eventData = JSON.parse(rawBody);
        console.log("[Razorpay Webhook 🔔] Received event:", eventData.event);

        if (eventData.event === "payment.captured" || eventData.event === "order.paid") {
          const payment = eventData.payload?.payment?.entity || {};
          const paymentId = payment.id;
          const notes = payment.notes || {};
          const description = payment.description || "";
          const amountPaise = payment.amount || 0;

          // SAFEGUARD: If you run multiple websites on this Razorpay account,
          // Razorpay broadcasts every payment to all webhooks.
          // Filter to make sure this event actually belongs to the 45 Landing Pages Bundle:
          const isLandingPageBundle =
            (notes.bundle && notes.bundle.toLowerCase().includes("landing")) ||
            description.toLowerCase().includes("landing") ||
            description.toLowerCase().includes("theme") ||
            notes.product === "45_landing_pages_bundle" ||
            amountPaise === 39900 ||
            amountPaise === 99900 ||
            amountPaise === 100;

          if (!isLandingPageBundle) {
            console.log(`[Razorpay Webhook ⏭️] Payment ${paymentId} belongs to another website on this account. Safely ignored.`);
            return new Response(
              JSON.stringify({
                status: "ignored",
                message: "Event ignored: Belongs to another website/product on this Razorpay account",
              }),
              { status: 200, headers: { "Content-Type": "application/json" } }
            );
          }

          const contact = payment.contact || notes.phone || notes.customer_phone || "";
          const name = notes.name || notes.customer_name || "Valued Customer";
          const amount = amountPaise ? amountPaise / 100 : 399;
          const cleanPhone = cleanPhoneNumber(contact);

          // Check if already processed
          const allLicenses = (await firebaseDb("licenses")) || {};
          const existing = Object.values(allLicenses).find((l) => l && l.paymentId === paymentId);

          if (!existing && cleanPhone) {
            const licenseKey = generateLicenseKey();

            const licenseRecord = {
              key: licenseKey,
              name,
              phone: contact,
              cleanPhone,
              paymentId,
              amount,
              tier: "Commercial Lifetime License",
              status: "active",
              verified: true,
              source: "razorpay_webhook",
              createdAt: new Date().toISOString(),
              dateFormatted: new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" }),
            };

            await firebaseDb(`licenses/${licenseKey}`, "PUT", licenseRecord);

            // Record paid lead
            await firebaseDb("leads", "POST", {
              name,
              phone: contact,
              cleanPhone,
              amount,
              status: "paid",
              paymentId,
              licenseKey,
              source: "razorpay_webhook",
              timestamp: Date.now(),
              createdAt: new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" }),
            });

            // Dispatch customer delivery WhatsApp
            const customerMsg = createCustomerWhatsAppMessage(name, licenseKey, cleanPhone);
            ctx.waitUntil(sendWhatsAppViaEvo(cleanPhone, customerMsg, CONFIG.EVO_INSTANCE));

            // Dispatch admin alert WhatsApp
            const adminMsg = createAdminWhatsAppAlert(name, cleanPhone, amount, paymentId, licenseKey);
            ctx.waitUntil(sendWhatsAppViaEvo(CONFIG.ADMIN_WHATSAPP, adminMsg, CONFIG.EVO_INSTANCE));
          }
        }

        return new Response(JSON.stringify({ status: "ok" }), {
          status: 200,
          headers: { "Content-Type": "application/json" },
        });
      } catch (err) {
        console.error("[Razorpay Webhook Error]:", err);
        return new Response(JSON.stringify({ error: err.message }), {
          status: 500,
          headers: { "Content-Type": "application/json" },
        });
      }
    }

    // 6. Generic WhatsApp Proxy POST (Matches your Talbina proxy worker)
    // Allows sending WhatsApp messages from any tool/script via POST to / or /message/sendText
    if (request.method === "POST" && (url.pathname === "/" || url.pathname === "/message/sendText" || url.pathname === "/api/send-whatsapp")) {
      try {
        const body = await request.json();
        const number = body.number;
        const text = body.text;
        const instance = body.instance || CONFIG.EVO_INSTANCE; // Default: mudassir
        const apiKey = body.apikey || CONFIG.EVO_API_KEY;

        if (!number || !text) {
          return new Response(
            JSON.stringify({ success: false, error: "Missing required fields: number, text" }),
            { status: 400, headers: { "Content-Type": "application/json", ...corsHeaders } }
          );
        }

        const targetUrl = `${CONFIG.EVO_BASE_URL}/message/sendText/${instance}`;
        const res = await fetch(targetUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "apikey": apiKey,
          },
          body: JSON.stringify({ number: cleanPhoneNumber(number), text }),
        });

        const data = await res.text();
        return new Response(data, {
          status: res.status,
          headers: { "Content-Type": "application/json", ...corsHeaders },
        });
      } catch (err) {
        return new Response(
          JSON.stringify({ success: false, error: err.message || "Proxy worker error" }),
          { status: 500, headers: { "Content-Type": "application/json", ...corsHeaders } }
        );
      }
    }

    // 404 for unknown routes
    return new Response(
      JSON.stringify({ error: "Endpoint not found", path: url.pathname }),
      { status: 404, headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  },
};
