# EthMoneyMaker

Requirements:

pip install coincurve

pip install safe_pysha3

pip install web3

pip install tqdm

git clone github.com/oliverwindas/EthMoneyMaker
cd EthMoneyMaker
source /path/to/file/EthMoneyMaker/bin/activate
./openethereum --chain mainnet --jsonrpc-interface all --jsonrpc-port 8545 --ws-interface all --ws-port 8546 --pruning fast
python EthMoneyProject.py
