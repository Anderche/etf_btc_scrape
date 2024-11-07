import asyncio
from crawl4ai import AsyncWebCrawler

# Define constants for URLs
URLS = {
    'bitcoin': "https://farside.co.uk/bitcoin-etf-flow-all-data/",
    'ethereum': "https://farside.co.uk/ethereum-etf-flow-all-data/"
}

async def scrape_full_page(url, crawler):
    try:
        result = await crawler.arun(
            url=url,
            bypass_cache=True
        )

        if result.success:
            print(f"Successfully scraped data from: {url}")
            print("\nFull page content:")
            print(result.markdown)
            return result.markdown
        else:
            print(f"Failed to scrape data from: {url}")
            return None
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return None

def get_user_choice():
    while True:
        choice = input("Which ETF data would you like to scrape? (bitcoin/ethereum): ").lower()
        if choice in URLS:
            return choice
        print("Invalid choice. Please enter 'bitcoin' or 'ethereum'.")

async def main():
    # Get user choice
    asset = get_user_choice()
    url = URLS[asset]

    print(f"\nSelected: {asset.upper()} ETF data")
    async with AsyncWebCrawler(verbose=True) as crawler:
        print(f"Scraping full page content from: {url}")
        content = await scrape_full_page(url, crawler)
        
        if content:
            print("\nScraping completed successfully.")
        else:
            print("\nFailed to scrape the page.")

if __name__ == "__main__":
    asyncio.run(main())


