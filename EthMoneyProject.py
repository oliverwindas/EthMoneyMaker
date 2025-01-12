from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from web3 import Web3

# Replace with your local node URL
local_node_url = 'http://127.0.0.1:8551'
web3 = Web3(Web3.HTTPProvider(local_node_url))

# Check if connected to Ethereum network
if web3.isConnected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect to Ethereum network")

private_key = keccak_256(token_bytes(32)).digest()
public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
addr = keccak_256(public_key).digest()[-20:]
address = "0x" + addr.hex()
balance_wei = web3.eth.get_balance(address)


print('Private_key:', private_key.hex())
print('ETH addr: 0x' + addr.hex())
print('Balance: ' + balance_wei)
