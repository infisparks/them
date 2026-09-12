FROM nginx:alpine

# Remove default nginx html
RUN rm -rf /usr/share/nginx/html/*

# Copy website files to nginx html
COPY . /usr/share/nginx/html

# Copy custom high-security nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Clean up git and internal files from container
RUN rm -rf /usr/share/nginx/html/.git \
    && rm -rf /usr/share/nginx/html/nginx.conf \
    && rm -rf /usr/share/nginx/html/Dockerfile

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
