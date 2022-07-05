from Module.ONEINCH_OffchainOracle import quote

# Call the Offchain Oracle getRate function provided by the 1INCH Spot Price Aggregator
## inputs: quote(Token, Quote_Token, Use_Wrappers)
## outputs: exchange rate
result = quote("WBTC", "WETH", False)
print(result)