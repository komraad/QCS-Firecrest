# Nginx Configuration for HTTP and HTTPS with Reverse Proxy

This Nginx configuration file sets up an HTTP server and an HTTPS server with reverse proxy capabilities.

**HTTP Server Configuration**

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # Redirecting HTTP to HTTPS
    return 301 https://$host$request_uri;
}
```

- The HTTP block listens on port 80 (and its IPv6 equivalent) and serves as the default server.
- The `return 301` directive is used to redirect all HTTP requests to their HTTPS counterparts. This ensures that all traffic is encrypted and secure.

**HTTPS Server Configuration:**

The HTTPS server is configured to listen on port 443 and uses SSL for secure communication. Here's the relevant code:

```nginx
server {
    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;
    server_name ____;

    ssl_certificate "/path-to-your-certificate/";
    ssl_certificate_key "/path-to-your-certificate-key/";

    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout 10m;
    ssl_protocols TLSv1.2 TLSv1.3;
}
```
