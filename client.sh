ACCESS_TOKEN_PATH = "/etc/bastion/access_token" # Path to the file containing the access token

CLIENT_ID=$(cat /etc/machine-id)

CENTRAL_HOST = "https://central.example.com" # Central server URL
CENTRAL_PORT = "443" # Central server port

# Check if the access token file exists
if [ ! -f $ACCESS_TOKEN_PATH ]; then
    echo "Access token file not found"
    
    # Wait for user to enter access token
    echo "Enter access token received from the server:"
    read ACCESS_TOKEN

    # Save access token to file
    echo $ACCESS_TOKEN > $ACCESS_TOKEN_PATH

    # Set access token permissions
    chmod 600 $ACCESS_TOKEN_PATH

    # Send request to server
    curl -X POST -H "Content-Type: application/json" -d '{"client_id": "'$CLIENT_ID'", "access_token": "'$ACCESS_TOKEN'"}' https://$CENTRAL_HOST:$CENTERAL_PORT/register
fi

# Get accessable bastion hosts
BASTION_HOSTS=$(curl -X GET -H "Content-Type: application/json" -d '{"client_id": "'$CLIENT_ID'", "access_token": "'$ACCESS_TOKEN'"}' http://$1:8080/clients)

# ssh to bastion host
ssh -i $ACCESS_TOKEN_PATH $BASTION_HOSTS
