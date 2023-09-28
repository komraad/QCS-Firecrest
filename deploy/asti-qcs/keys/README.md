# The keys reciding here will be use for the Certificator service, HPC cluster.  The ca-key.pub is already appended to the cluster.
## To generate the keys use these commands :

ssh-keygen -t ed25519 -b 521 -P "" -f ca-key -C "CA Authority-f7t"
ssh-keygen -t ed25519 -b 256 -P "" -f user-key

## Correct the permission to 400 for both user-key and ca-key
