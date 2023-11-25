from web3 import Web3

# Replace with your Alchemy endpoint and API key
alchemy_endpoint = "https://eth-sepolia.g.alchemy.com/v2/8gdP7Vxqu1ihb5b-_Ezj_iWrUOtAMNYj"

# Connect to Alchemy
w3 = Web3(Web3.HTTPProvider(alchemy_endpoint))

# Replace with your contract address and ABI
contract_address = "0x3a9F7Ad50AcCF46F8F51614fc9294Fc205a057ab"
contract_abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"winner","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AuctionEnded","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"bidder","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"BidPlaced","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bids","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"endAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"highestBid","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"highestBidder","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"placeBid","outputs":[],"stateMutability":"payable","type":"function"}]
# Replace with your contract ABI
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Replace with your private key
private_key = "57debafa21a5d67114f8a48966babbec29ad555ce514075481a60e4f893af5d0"

# Account to interact with the contract
#account = w3.eth.account.privateKeyToAccount(private_key)
account = '0x83610eBdD0EFFD8F07E346c281AA211e25E4dE69'

def place_bid(amount):
    nonce = w3.eth.getTransactionCount(account.address)
    gas_price = w3.toWei('40', 'gwei')

    # Construct the transaction parameters
    transaction_parameters = {
        'from': account.address,
        'gas': 200,
        'gasPrice': gas_price,
        'nonce': nonce,
        'value': amount,
    }

    # Get the function and its transaction data
    place_bid_function = contract.functions.placeBid()
    transaction_data = place_bid_function.buildTransaction(transaction_parameters)

    # Sign the transaction
    signed_transaction = w3.eth.account.sign_transaction(transaction_data, private_key)

    # Send the transaction
    tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    return tx_hash

# Example usage
bid_amount = 1000
tx_hash = place_bid(bid_amount)
print(f"Bid placed. Transaction hash: {tx_hash}")
