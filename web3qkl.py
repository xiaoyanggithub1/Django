import json

from web3 import Web3

# 连接Infura节点
infura_url = "https://goerli.infura.io/v3/45b99daa2fbf42e582b72a2ddb58499f"
w3 = Web3(Web3.HTTPProvider(infura_url))

# 打印节点信息
print(w3.eth)
contract_address = "0xd9145CCE52D386f254917e481eB44e9943F39138"
#  获取智能合约ABI
with  open("contract_abi.json") as f:
    contract_abi = json.load(f)

#  连接智能合约
contract = w3.eth.contract(address=contract_address, abi="contract_abi")

print(contract)
