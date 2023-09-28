## This certificates will be used for proxy server and keycloak. However, this are self signed and it is better to get a authentic certificates from the trusted stores.

## Create a CA certificate 
openssl genrsa 2048 > ca-key.pem
openssl req -new -x509 -nodes -days 3600 -key ca-key.pem -out ca.pem

## Create a Server certificate, remove pass phrase and sign it
## server-cert.pem = publick key, server-key.pem = private key
openssl req -newkey rsa:2048 -days 3600 -nodes -keyout server-key.pem -out server-req.pem
openssl rsa -in server-key.pem -out server-key.pem
openssl x509 -req -in server-req.pem -days 3600 -CA ca.pem -CAkey ca-key.pem -set_serial 01 -out server-cert.pem
