import requests
from azure.identity import ClientSecretCredential

tenant_id = "TENANT_ID"
client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"

credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

token = credential.get_token("https://analysis.windows.net/powerbi/api/.default")

headers = {
    "Authorization": f"Bearer {token.token}"
}

response = requests.get(
    "https://api.powerbi.com/v1.0/myorg/groups",
    headers=headers
)

print(response.json())
