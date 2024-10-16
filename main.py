import asyncio
from crawl4ai import AsyncWebCrawler
import pandas as pd
import re
from bs4 import BeautifulSoup


async def scrape_full_page(url, crawler):
    try:
        result = await crawler.arun(
            url=url,
            bypass_cache=True
        )

        if result.success:
            print(f"Successfully scraped data from: {url}")
            return result.markdown
        else:
            print(f"Failed to scrape data from: {url}")
            return None
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return None


def create_dataframe_from_html(html_content):
    # Save the HTML content to a file for inspection
    with open('scraped_content.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the table containing the data
    table = soup.find('table', class_='wp-block-table')
    
    if not table:
        print("No table found in the HTML content. Check the 'scraped_content.html' file for the actual content.")
        return None
    
    # Extract headers
    headers = [th.text.strip() for th in table.find_all('th')]
    
    # Extract data rows
    data = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        if len(cells) == len(headers):
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)
    
    if not data:
        print("No valid data rows found after processing. Check the HTML content.")
        return None
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=headers)
    
    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d %b %Y')
    
    # Convert numeric columns to float, replacing '-' with NaN
    numeric_columns = df.columns.drop('Date')
    df[numeric_columns] = df[numeric_columns].replace('-', float('nan')).astype(float)
    
    return df


async def main():
    url = "https://farside.co.uk/bitcoin-etf-flow-all-data/"

    async with AsyncWebCrawler(verbose=True) as crawler:
        print(f"Scraping full page content from: {url}")
        html_content = await scrape_full_page(url, crawler)
        
        if html_content:
            print("\nScraping completed successfully.")
            
            # Create DataFrame from the scraped data
            df = create_dataframe_from_html(html_content)

            if df is not None:
                # Print the DataFrame
                print("\nFirst 5 rows of the DataFrame:")
                print(df.head(5))

                # Save to CSV
                df.to_csv('bitcoin_etf_flow.csv', index=False)
                print("\nData saved to 'bitcoin_etf_flow.csv'")
            else:
                print("\nFailed to create DataFrame from the scraped content.")
        else:
            print("\nFailed to scrape the page.")


if __name__ == "__main__":
    asyncio.run(main())
