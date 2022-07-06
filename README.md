# 1INCH Quoter

Python script to read the 1INCH Offchain Oracle smart contract to aggregate quotes across multiple DEXes and fee tiers available on Uniwap v3. The 1inch spot price aggregator is a set of smart contracts that extract price data for tokens traded on DEXes from the blockchain.

Supported DEXes:
- Mooniswap
- 1inch Liquidity Protocol V1.1
- Uniswap V1
- Uniswap V2
- Sushiswap
- Equalizer.fi
- Uniswap V3
- Synthetix
- Chainlink
- Shibaswap

## Environment Details

1INCH Offchain Oracle: `0x07D91f5fb9Bf7798734C3f606dB065549F6893bb`

## Running 1INCH Quoter

Navigate to the project directory:
`cd Project Folder`

Edit run.py to specify your input and output token (e.g. WBTC, USDC):

`quote(INPUT_TOKEN_TICKER, OUTPUT_TOKEN_TICKER, useWrapper)`

Run the script:
`python run.py`

Example Output:

`19280.039817`
