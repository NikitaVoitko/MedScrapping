import requests
import os
from bs4 import BeautifulSoup


# Function to scrape text from a single page
def scrape_page(url,):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # Find all <p> tags and extract the text inside them
        paragraphs = soup.find_all('p')
        # Extract text from each paragraph and return as a single string
        page_text = '\n'.join(
            [paragraph.get_text() for paragraph in paragraphs]
        )
        return page_text
    else:
        print(f"Failed to fetch HTML content from {url}")
        return None


def write_files(start_page, end_page, 
                base_url="https://pro.uptodatefree.ir/Show/",
                output_dir="text_files"):
    os.makedirs(output_dir, exist_ok=True)

    for page_number in range(start_page, end_page + 1):
        url = f"{base_url}{page_number}"
        page_text = scrape_page(url)
        if page_text:
            file_path = os.path.join(output_dir,
                                     f'extracted_text_page_{page_number}.txt')
            with open(file_path, 'w') as f:
                f.write(page_text)
                print(f"Text extracted from page {page_number} "
                      f"and saved to {file_path}")
