# Nginx Configuration for HTTP and HTTPS with Reverse Proxy

This Nginx configuration file sets up an HTTP server and an HTTPS server with reverse proxy capabilities. It includes detailed explanations and code snippets to help a junior developer understand the configuration.

## HTTP Server Configuration

The HTTP server is configured to listen on port 80 and redirect all incoming HTTP requests to HTTPS using a 301 redirect. Here's the relevant code:

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # Redirecting HTTP to HTTPS
    return 301 https://$host$request_uri;
}
```


## Reverse Proxy Configuration

The reverse proxy configuration routes incoming requests to different backend servers based on the request path.

# Setting
- Redirect HTTP to HTTPS
- Certicates (self-signed)
- Proxy location