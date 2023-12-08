from web3 import Web3

# Replace with your Alchemy endpoint and API key
alchemy_endpoint = "https://eth-sepolia.g.alchemy.com/v2/8gdP7Vxqu1ihb5b-_Ezj_iWrUOtAMNYj"

# Connect to Alchemy
w3 = Web3(Web3.HTTPProvider(alchemy_endpoint))

# Replace with your contract address and ABI
contract_address = "0x3a9F7Ad50AcCF46F8F51614fc9294Fc205a057ab"
owner_address = "0x83610eBdD0EFFD8F07E346c281AA211e25E4dE69"
contract_abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"winner","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AuctionEnded","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"bidder","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"BidPlaced","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bids","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"endAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"highestBid","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"highestBidder","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"placeBid","outputs":[],"stateMutability":"payable","type":"function"}]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Replace with your private key
private_key = "57debafa21a5d67114f8a48966babbec29ad555ce514075481a60e4f893af5d0"

# Account to interact with the contract
account = w3.eth.account.from_key(private_key)

def test_auction():
    # Get the current highest bid
    current_highest_bid = contract.functions.highestBid().call()
    print(f"Current Highest Bid: {current_highest_bid}")

    # Get the updated highest bid
    updated_highest_bid = contract.functions.highestBid().call()
    print(f"Updated Highest Bid: {updated_highest_bid}")

    # End the auction (only the owner can do this)
    if account.address == contract.functions.owner().call():
        tx_hash = end_auction()
        print(f"Auction ended by the owner. Transaction hash: {tx_hash}")
    else:
        print("You are not the owner. Cannot end the auction.")

    # Check the final state
    final_highest_bidder = contract.functions.highestBidder().call()
    final_highest_bid = contract.functions.highestBid().call()
    print(f"Final Highest Bidder: {final_highest_bidder}")
    print(f"Final Highest Bid: {final_highest_bid}")

# Function to end the auction
def end_auction():
    transaction = contract.functions.endAuction().build_transaction({
        'from': owner_address,
        'gas': 6000000,
        'gasPrice': w3.to_wei('40', 'gwei'),
        'nonce': w3.eth.get_transaction_count(owner_address),
    })

    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return tx_hash

# Example usage
#tx_hash = end_auction()
tx_hash = test_auction()
#print(f"Auction ended. Transaction hash: {tx_hash}")
#final_highest_bidder = contract.functions.highestBidder().call()
#final_highest_bid = contract.functions.highestBid().call()
#print(f"Final Highest Bidder: {final_highest_bidder}")
#print(f"Final Highest Bid: {final_highest_bid}")
