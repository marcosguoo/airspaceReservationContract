from web3 import Web3
# Connect to Ganache, make sure ganache is running
w3 = Web3(Web3.HTTPProvider("https://eth-sepolia.g.alchemy.com/v2/8gdP7Vxqu1ihb5b-_Ezj_iWrUOtAMNYj"))

#Check Connection
t=w3.is_connected()
print(t)

# Get private key 
Private_key_Wallet_2 =  '57debafa21a5d67114f8a48966babbec29ad555ce514075481a60e4f893af5d0'

# Create a signer wallet
PA=w3.eth.account.from_key(Private_key_Wallet_2)

# Get public address from a signer wallet
#Public_Address=PA.address
#print(Public_Address)
