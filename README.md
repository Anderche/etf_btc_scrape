# Crypto ETF Data Scraper

A Python script for scraping cryptocurrency ETF data.

## Description

This script (`script_scrape_farside.py`) is designed to scrape and collect data about cryptocurrency ETFs from financial data sources. It helps track and analyze ETF performance and metrics related to various cryptocurrencies.

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
  - [Add specific metrics based on your script's functionality]

## Data Sources
    - https://farside.co.uk/


