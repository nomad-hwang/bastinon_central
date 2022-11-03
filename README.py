# SSH Bastion Management

It's a simple SSH Bastion Management system. It's a work in progress.

- Provisioning with temporary access token retreived from web page
- Client side no extra dependency, just shell script

Process of provisioning a client:
1. Requests a token from the server. (This is done by the user)
2. User sends/type in the token to the client.
3. Client sends the token to the server for registration.
4. Server validates the token and creates a credential(including random password) for the client.
5. Server returns the credential to the client. (Only time the password is returned)
6. Client stores the credential.
7. Client uses the credential to authenticate to the server.