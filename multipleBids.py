import random
import time
from web3 import Web3

# Replace with your Alchemy endpoint and API key
alchemy_endpoint = "https://eth-sepolia.g.alchemy.com/v2/8gdP7Vxqu1ihb5b-_Ezj_iWrUOtAMNYj"

# Connect to Alchemy
w3 = Web3(Web3.HTTPProvider(alchemy_endpoint))

# Replace with your contract address and ABI
contract_address = "0x3a9F7Ad50AcCF46F8F51614fc9294Fc205a057ab"
contract_abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"winner","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AuctionEnded","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"bidder","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"BidPlaced","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bids","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"endAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"highestBid","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"highestBidder","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"placeBid","outputs":[],"stateMutability":"payable","type":"function"}]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

private_keys = ["84b4091e15267b50f6645d44bb96b4bc3179377daa2a8808b224d9f579be1cf1", "0ed7b2db696a63d09cfc3f1372d18b7edb019ce61a90907b2ebaba7b9d209ee6", "e0023eb49080755858a869113960ff7077c814201a2bc44ea5579686e27841ea", "873027b1d6b90ba91c01056abd2a344d2120a12eefd300adae90bb64817e263c", "ced74225be9e26fed49fd7384a21677b4a6217d479c2987e46df3f9494677a6f"]  # Add more private keys as needed

# Function to place a random bid
def place_random_bid(private_key):
    account = w3.eth.account.from_key(private_key)
    account_address = account.address

    # Random bid between 500 and 1000 wei
    bid_amount = random.randint(500, 1000)

    transaction = contract.functions.placeBid().build_transaction({
        'from': account_address,
        'gas': 200000,
        'gasPrice': w3.to_wei('40', 'gwei'),
        'value': bid_amount,
        'nonce': w3.eth.get_transaction_count(account_address),
    })

    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    
    print(f"Bid placed by {account_address}. Bid amount: {bid_amount} wei. Transaction hash: {tx_hash}")

# Example usage
for private_key in private_keys:
    place_random_bid(private_key)
    time.sleep(2)  # Add a delay to avoid nonce issues

# Add more bids as needed
