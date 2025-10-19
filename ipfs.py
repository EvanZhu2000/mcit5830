import requests
import json

#API Key: a2cd687fe44848166a56
#API Secret: c8008f094efa729e3b404c712c0c825beff2dc05ee0c83fa30e1758dc3cad118
#JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJiOTM2N2FjMS1mN2FkLTQ3MzAtOWY5MC0wOTRkOGM4ZDczNTIiLCJlbWFpbCI6ImV6dmhhdW5AZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiRlJBMSJ9LHsiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImEyY2Q2ODdmZTQ0ODQ4MTY2YTU2Iiwic2NvcGVkS2V5U2VjcmV0IjoiYzgwMDhmMDk0ZWZhNzI5ZTNiNDA0YzcxMmMwYzgyNWJlZmYyZGMwNWVlMGM4M2ZhMzBlMTc1OGRjM2NhZDExOCIsImV4cCI6MTc5MjM3NDk5OX0.IAgcLT7h3ZsplRGCxFQmHEslcvpvke4X0drJ1zvlU2c

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error: pin_to_ipfs expects a dictionary"

    # Your Pinata API credentials
    pinata_api_key = "a2cd687fe44848166a56"  # Replace with your actual key
    pinata_secret_api_key = "c8008f094efa729e3b404c712c0c825beff2dc05ee0c83fa30e1758dc3cad118"  # Replace with your actual secret key

    # Pinata API endpoint for pinning JSON
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

    # Headers for authentication
    headers = {
        'pinata_api_key': pinata_api_key,
        'pinata_secret_api_key': pinata_secret_api_key,
        'Content-Type': 'application/json',
    }

    # The payload includes your data
    payload = {
        "pinataContent": data
    }

    # Send the POST request to Pinata
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        # Parse the response to get the IPFS Content Identifier (CID)
        result = response.json()
        cid = result["IpfsHash"]
        return cid
    else:
        # Provide error information if the request failed
        raise Exception(f"Failed to pin data: {response.status_code} - {response.text}")

def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "Error: get_from_ipfs accepts a CID string"

    # Construct the URL using a public IPFS gateway
    gateway_url = f"https://gateway.pinata.cloud/ipfs/{cid}"

    # Fetch the data from the gateway
    response = requests.get(gateway_url)

    if response.status_code == 200:
        # Parse and return the JSON data
        data = response.json()
        assert isinstance(data, dict), "Error: get_from_ipfs should return a dict"
        return data
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code}")