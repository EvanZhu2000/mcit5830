from web3 import Web3
from web3.providers.rpc import HTTPProvider
import requests
import json

bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
contract_address = Web3.to_checksum_address(bayc_address)

# You will need the ABI to connect to the contract
# The file 'abi.json' has the ABI for the bored ape contract
# In general, you can get contract ABIs from etherscan
# https://api.etherscan.io/api?module=contract&action=getabi&address=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D
with open('ape_abi.json', 'r') as f:
    abi = json.load(f)

############################
# Connect to an Ethereum node
INFURA_KEY = "7a22d2b37e2d43faa3d400346ef7b9b7"
api_url = f"https://mainnet.infura.io/v3/{INFURA_KEY}"  # YOU WILL NEED TO PROVIDE THE URL OF AN ETHEREUM NODE
provider = HTTPProvider(api_url)
web3 = Web3(provider)


def get_ape_info(ape_id):
    assert isinstance(ape_id, int), f"{ape_id} is not an int"
    assert 0 <= ape_id, f"{ape_id} must be at least 0"
    assert 9999 >= ape_id, f"{ape_id} must be less than 10,000"

    data = {'owner': "", 'image': "", 'eyes': ""}

    # YOUR CODE HERE
    # Get owner of the ape
    contract = web3.eth.contract(address=contract_address, abi=abi)
    owner = contract.functions.ownerOf(ape_id).call()
    data['owner'] = owner

    # Get token URI
    token_uri = contract.functions.tokenURI(ape_id).call()
    
    # Convert IPFS URI to HTTP URL using Pinata gateway
    if token_uri.startswith('ipfs://'):
        ipfs_hash_with_path = token_uri[7:]  # Remove 'ipfs://' prefix
        # Use Pinata gateway to fetch metadata
        # gateway_url = f"https://gateway.pinata.cloud/ipfs/{ipfs_hash_with_path}"
        gateway_url = f"https://cloudflare-ipfs.com/ipfs/{ipfs_hash_with_path}"
    else:
        gateway_url = token_uri
    
    # Fetch metadata from IPFS via Pinata gateway
    try:
        response = requests.get(gateway_url, timeout=10) # increase timeout to pass the test case?
        if response.status_code == 200:
            metadata = response.json()
            
            # Extract image and eyes attributes
            data['image'] = metadata.get('image', '')
            
            # Find eyes attribute
            attributes = metadata.get('attributes', [])
            for attr in attributes:
                if attr.get('trait_type') == 'Eyes':
                    data['eyes'] = attr.get('value', '')
                    break
        else:
            print(f"Error fetching metadata: HTTP {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")     

    assert isinstance(data, dict), f'get_ape_info{ape_id} should return a dict'
    assert all([a in data.keys() for a in
                ['owner', 'image', 'eyes']]), f"return value should include the keys 'owner','image' and 'eyes'"
    return data

if __name__ == "__main__":
    print(get_ape_info(8033))