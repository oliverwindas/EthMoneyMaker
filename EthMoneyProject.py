from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from etherscan import Etherscan

eth = Etherscan("832DM6Z5K5TYCJ16RUKSV3FXEC51UQH6P5")


private_key = keccak_256(token_bytes(32)).digest()
public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
addr = keccak_256(public_key).digest()[-20:]
bal = eth.get_eth_balance(address=("0x" + addr.hex()))


print('Private_key:', private_key.hex())
print('ETH addr: 0x' + addr.hex())
print('Balance: ' + bal)
