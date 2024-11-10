# Crypto ETF Data Scraper

### Developed By:

Anders Kiss 

---

A Python script for scraping cryptocurrency **Exchange-Traded Fund (ETF)** data. An ETF is an investment fund traded on stock exchanges that holds assets like stocks, bonds, or commodities; they typically track an index, charge low fees, and offer liquidity. This script tracks the flows (million, USD) for Bitcoin ($BTC) ETF's, like BlackRock's $IBIT and Fidelity's $FBTC, which offer investors exposure through regular brokerage accounts without managing crypto wallets or keys. Flows refer to the movement of money into (inflows) or out of (outflows) investment products. Specifically, positive flows indicate investors are buying shares whereas negative flows show indicate selling.

## Description

This script (`script_scrape_farside.py`) is designed to scrape and collect data about cryptocurrency ETFs from financial data sources. It helps track and analyze ETF performance and metrics related to various cryptocurrencies.

## Why Track Crypto ETFs?

Tracking cryptocurrency ETFs is crucial for several reasons:

- **Institutional Adoption**: ETFs represent a major step in cryptocurrency's integration into traditional finance, offering regulated exposure to digital assets
- **Market Impact**: ETF trading volumes and flows can significantly influence cryptocurrency prices and market sentiment
- **Investment Accessibility**: ETFs provide a familiar, regulated vehicle for investors to gain crypto exposure without direct cryptocurrency ownership
- **Price Discovery**: ETF prices and premiums/discounts to NAV offer valuable market signals
- **Regulatory Insights**: Changes in ETF holdings and regulations can indicate broader crypto market trends
- **Portfolio Management**: ETF data helps investors optimize their crypto exposure within traditional investment frameworks

## Prerequisites

- Python 3.x
- Required Python packages (install via pip):
  ```bash
  pip install -r requirements.txt
  ```

## Environment Setup

### Using Conda

1. Create a new conda environment:
```bash
conda create -n crypto_etf_env python=3.9
```

2. Activate the environment:
```bash
conda activate crypto_etf_env
```

3. Install required packages:
```bash
conda install pandas requests beautifulsoup4
# Add any additional packages your script requires
```

### Alternative: Using requirements.txt
If you prefer using pip with a requirements.txt file:
```bash
conda activate crypto_etf_env
pip install -r requirements.txt
```

## Usage

```bash
python script_scrape_farside.py
```

## Features

- Scrapes cryptocurrency ETF data from financial sources
- Collects key metrics such as:
  - Price
  - Volume
  - Assets Under Management (AUM)
  - Performance metrics

## Data Sources
    - https://farside.co.uk/


