from web3 import Web3

# Replace with your Alchemy endpoint and API key
alchemy_endpoint = "https://eth-sepolia.g.alchemy.com/v2/8gdP7Vxqu1ihb5b-_Ezj_iWrUOtAMNYj"

# Connect to Alchemy
w3 = Web3(Web3.HTTPProvider(alchemy_endpoint))

# Replace with your contract address and ABI
contract_address = "0x3a9F7Ad50AcCF46F8F51614fc9294Fc205a057ab"
contract_abi = [
   {
      "inputs":[
         {
            "internalType":"string",
            "name":"initMessage",
            "type":"string"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"constructor"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "internalType":"string",
            "name":"oldStr",
            "type":"string"
         },
         {
            "indexed":False,
            "internalType":"string",
            "name":"newStr",
            "type":"string"
         }
      ],
      "name":"UpdatedMessages",
      "type":"event"
   },
   {
      "inputs":[
         
      ],
      "name":"message",
      "outputs":[
         {
            "internalType":"string",
            "name":"",
            "type":"string"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"string",
            "name":"newMessage",
            "type":"string"
         }
      ],
      "name":"update",
      "outputs":[

      ],
      "stateMutability":"nonpayable",
      "type":"function"
   }
]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Replace with your private key
private_key = "8gdP7Vxqu1ihb5b-_Ezj_iWrUOtAMNYj"

# Account to interact with the contract
w3 = Web3(Web3.HTTPProvider(alchemy_endpoint))  # Ensure you have the correct provider
account = w3.eth.account.privateKeyToAccount(private_key)

def place_bid(amount):
    transaction = contract.functions.placeBid().buildTransaction({
        'from': account.address,
        'gas': 200,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': w3.eth.getTransactionCount(account.address),
    })

    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    return tx_hash

def end_auction():
    transaction = contract.functions.endAuction().buildTransaction({
        'from': account.address,
        'gas': 200,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': w3.eth.getTransactionCount(account.address),
    })

    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    return tx_hash

# Example usage
bid_amount = 1e20  # 0.01 Ether
tx_hash = place_bid(bid_amount)
print(f"Bid placed. Transaction hash: {tx_hash}")

# Uncomment the following line to end the auction
# end_auction()
