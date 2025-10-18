1. Connecting to the Ethereum Blockchain
Querying the Ethereum blockchain
Validators in Ethereum keep track of the current state of the blockchain, as well as a record of all transactions that have been processed. Every Ethereum client implements a JSON-RPC API that makes it possible to connect to a validator and query the state of the blockchain.
Although the Ethereum client software provides such an interface, most Ethereum validators do not make this API available to the public.
In order to access on-chain data, you can either run your own Ethereum node, or connect to a node run by an infrastructure provider. Throughout this course, we’ll be connecting to the Ethereum blockchain, so you will need to have access to an Ethereum node. You are welcome to run your own Ethereum node, but it is
probably much easier to get access through an infrastructure provider.
I have used services through the following providers:
Infura
Alchemy
NowNodes
Chainstack
These providers all offer a free tier of service will be sufficient for everything we do in this class, there is no need to pay for API access (unless you want to do data-heavy exploration of the blockchain on your own)
Step 1: getting access to an Ethereum node
Get access to an Ethereum node. I recommend signing up for a free account with one of the providers listed above.
They will give you an API and a URL which will give you access to an Ethereum node.
We will use Mainnet as the network for the first part of this assignment and the BNB testnet network for the second
Step 2: Connecting to ETH mainnet
We will use the Python web3 library to connect to your blockchain node.
Fill in your provider details in the file connect_to_eth.py. Specifically, finish the function "connect_to_eth", and make sure it returns a connected web3 instance.
This step is very straightforward. You just need to fill in the address and API key of your node provider.
To verify that your returned web3 instance (as w3) is connected you should be able to use it to interact with the blockchain by calling methods such as w3.is_connected() and w3.eth.get_block(‘latest’)
Step 3: Connect to a contract on the BNB testnet
We will continue to use the Python web3 library to connect to a BNB testnet node. The BNB chain is EVM compatible, meaning that smart contracts work in basically the same way on BNB as on Ethereum. The consensus mechanism, and the node software is not exactly the same, however, so you need to inject “middleware” to read and write from the BNB testnet.
To read from the BNB testnet, you will have to add middleware (we have imported the correct type for you in the starter code).
Once you have connected to the BNB testnet, you will need to connect to a contract called “MerkleValidator” that we deployed on the BNB testnet.
The python web3 documentation provides details on how to create contract objects in python. In the “Merkle Validator” assignment in Module 4, we’ll interact with this contract in detail, but for now, you just need to create the contract object in python, so there’s no real need to understand the contract itself yet.
Testnet nodes often have more “open” access then mainnet nodes. You can search the web for testnet node providers and aggregators like Chainlist that don’t require you to set up an account at all. Getting a personal API key from one of the providers listed above is usually more reliable than connecting to a public node that doesn’t require authentication.
So, for this part of the assignment, you will need to fill in your provider details in the file connect_to_eth.py. Specifically, finish the function "connect_with_middleware", and make sure it returns a connected web3 instance and a contract object. We have provided you with starter code to read in the correct contract address and ABI from the “contract_info.json” file.
Remember to hold on to your connection information as you’ll need it for several future assignments.
When you are ready you can click “Run Test Cases” to test the code in your linked github repo before submitting for a final grade.