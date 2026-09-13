# InfiSparks Theme Store - Cloudflare Worker & Razorpay Integration

## Overview
This Cloudflare Worker (`https://digitalthem.infisparks.workers.dev`) handles:
1. **Instant Lead Capture**: Automatically saves customer leads directly into Firebase Realtime Database (even if checkout is cancelled or payment is abandoned).
2. **Standard Razorpay Checkout**: Connects live with Key ID `rzp_live_TXvv4nCnkVjFWm`.
3. **Automated License Generation**: Generates unique `LIC-45LP-XXXX-XXXX` license keys upon payment verification.
4. **WhatsApp Automation**: Dispatches instant WhatsApp messages via Evolution API (`https://evo.infisparks.in`) to the customer with their license key and direct download link.
5. **Admin Sales Alert**: Instantly alerts admin WhatsApp (`+91 99583 99157`) on every sale.
6. **Razorpay Webhooks**: Server-to-server backup ensuring 100% reliable license delivery even if customer closes browser early.

---

## 1. How to Deploy to Cloudflare Workers

### Option A: Cloudflare Web Dashboard (Quickest)
1. Go to [dash.cloudflare.com](https://dash.cloudflare.com/) and navigate to **Workers & Pages**.
2. Select or create your worker: **`digitalthem`** (URL: `https://digitalthem.infisparks.workers.dev`).
3. Click **Quick Edit** or **Edit Code**.
4. Copy the entire contents of [`cloudflare-worker/worker.js`](./worker.js) and paste it into the editor.
5. Click **Save and Deploy**.

---

## 2. Step-by-Step: Add Webhook in Razorpay Dashboard

1. Log into your Razorpay Dashboard at [dashboard.razorpay.com](https://dashboard.razorpay.com/).
2. Navigate to **Account & Settings** &rarr; **Webhooks** (under Website and app settings).
3. Click **+ Add New Webhook**.
4. Fill in the webhook form:
   - **Webhook URL:** `https://digitalthem.infisparks.workers.dev/api/razorpay-webhook`
   - **Secret:** `XtzQBL84oexfAFHDPOHSrXc4`
   - **Alert Email:** Your email for webhook health notices
5. Under **Active Events**, check the following checkboxes:
   - ✅ `payment.captured`
   - ✅ `order.paid`
6. Click **Create Webhook**.

---

## 3. API Endpoints Reference

| Endpoint | Method | Purpose |
|---|---|---|
| `/` or `/api/health` | `GET` | Health check & config status verification |
| `/api/leads` | `POST` | Saves visitor leads directly into Firebase RTDB |
| `/api/verify-payment` | `POST` | Verifies Razorpay payment, generates license, updates Firebase & triggers customer WhatsApp |
| `/api/razorpay-webhook` | `POST` | Razorpay webhook listener for automatic background fulfillment |

---

## 4. WhatsApp Customer Delivery Template

When a customer pays ₹999, they immediately receive:
```
🎉 *Payment Confirmed! Access Your 45+ Landing Page Bundle*

Hello *Customer Name*,
Thank you for purchasing the *45+ Ultimate Landing Page Bundle*! 🚀

🔑 *Your Official Commercial License Key:*
`LIC-45LP-XXXX-XXXX`

📥 *Click to Unlock & Download Complete Source Codes:*
https://them.infisparks.com/purchase/?key=LIC-45LP-XXXX-XXXX&phone=919876543210

✨ *What You Received:*
✅ Full lifetime access to all 45+ production landing pages
✅ 100% Commercial Client & Personal Usage Rights
✅ 1-Click ZIP Source Code Downloads (HTML, Tailwind CSS, JS)
✅ Future updates & luxury templates included
```
