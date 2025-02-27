import os
import requests
from bs4 import BeautifulSoup

def get_page_pdf(url, output_file):
    # Check if the URL is reachable
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return
    
    # Parse HTML with BeautifulSoup for cleanup
    soup = BeautifulSoup(response.text, 'html.parser')
    for script in soup(['script', 'style']):
        script.decompose()  # Remove unwanted elements
    cleaned_html = str(soup)
    
    # Save cleaned HTML to a temp file
    temp_html_file = "temp.html"
    with open(temp_html_file, "w", encoding="utf-8") as file:
        file.write(cleaned_html)
    
    # Use Chrome to generate a PDF
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    chrome_command = (
        f'"{chrome_path}" --headless --disable-gpu --print-to-pdf="{output_file}" "{temp_html_file}"'
    )
    
    os.system(chrome_command)
    os.remove(temp_html_file)
    
    print(f"PDF saved to {output_file}")

if __name__ == "__main__":
    url = input("Enter the URL: ").strip()
    output_file = "output.pdf"
    get_page_pdf(url, output_file)
