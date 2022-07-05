import json
from web3 import Web3
from Module.Constants.ONEINCH_OffchainOracle import abi

# Load environment
data = open('./Module/Constants/environment.json')
env = json.loads(data.read())

# Load token data
data = open('./Module/Constants/tokens.json')
tokens = json.loads(data.read())

# Connect to web3 provider
url = env['URL']
web3 = Web3(Web3.HTTPProvider(url))

# Uniswap v3 Quoter Contract
contract_address = env['CONTRACT']
contract = web3.eth.contract(address=contract_address, abi=abi)

def quote(_tokenIn, _tokenOut, _useWrappers):

    ## Web3 connection
    if not web3.isConnected():
        print("Not connected network")
        return

    ## Call the Uniswap v3 Quoter Contract
    _outputRaw = contract.functions.getRate(tokens[_tokenIn]['address'], tokens[_tokenOut]['address'], _useWrappers).call()
    _tokenprice = _outputRaw * (10 ** int(tokens[_tokenIn]['decimals'])) / (10 ** int(tokens[_tokenOut]['decimals'])) / 10**18

    return _tokenprice