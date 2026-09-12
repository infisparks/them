FROM nginx:alpine

# Remove default nginx html
RUN rm -rf /usr/share/nginx/html/*

# Copy website files to nginx html
COPY . /usr/share/nginx/html

# Copy custom high-security nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Clean up git and internal files from container & generate master bundle zip
RUN apk add --no-cache python3 \
    && python3 -c "import os, zipfile; cwd = '/usr/share/nginx/html'; out = os.path.join(cwd, 'downloads'); os.makedirs(out, exist_ok=True); bpath = os.path.join(out, 'complete-45-landing-pages-bundle.zip'); dirs = sorted([d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d)) and not d.startswith('.') and d not in ['downloads', 'zips', 'purchase', 'admin', 'tools']]); zf = zipfile.ZipFile(bpath, 'w', zipfile.ZIP_DEFLATED); [zf.write(os.path.join(r, f), os.path.relpath(os.path.join(r, f), cwd)) for d in dirs for r, _, fs in os.walk(os.path.join(cwd, d)) for f in fs]; zf.close()" \
    && apk del python3 \
    && rm -rf /usr/share/nginx/html/.git \
    && rm -rf /usr/share/nginx/html/nginx.conf \
    && rm -rf /usr/share/nginx/html/Dockerfile

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
