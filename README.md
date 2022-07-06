# 1INCH Quoter

Python script to read the 1INCH Offchain Oracle smart contract to aggregate quotes across multiple DEX's and fee tiers available on Uniwap v3. The 1inch spot price aggregator is a set of smart contracts that extract price data for tokens traded on DEXes from the blockchain.

Supported DEX's are below:
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

Uniswap v3 Quoter Contract: `0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6`

## Running Uniswap v3 Quoter

Navigate to the project directory:
`cd Project Folder`

Edit run.py to specify your input and output token (e.g. WBTC, USDC):

`quote(INPUT_TOKEN_TICKER, OUTPUT_TOKEN_TICKER, INPUT_TOKEN_AMOUNT)`

Run the script:
`python run.py`

Example Output:

`{'0.3%': 19280.039817, '1.0%': 19112.449151}`
