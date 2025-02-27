# PDF GENERATOR in Python

## Take in a URL and produce a PDF of the site

For this script, we will use Python to make a request to a URL, utilize headless Chrome to print to PDF.

## First Step

- Make sure the Google Chrome executable is in the PATH and can be called from the command line.
- This step varies by OS, so check online for the best method for your system.
- You’ll know it works when you can type `chrome` in the command line or terminal and the browser opens.
- If you can’t get this to work in the PATH, you can modify the script to include the full path to Chrome or use Selenium for headless Chrome functionality.

## Create the Python File and Set Up Code

### Install Required Dependencies

Run the following command to install dependencies if you haven’t already:

```sh
pip install requests beautifulsoup4
```

### Import the Necessary Modules

Create a Python file, e.g., `pdf_generator.py`, and include the following imports:

```python
import os
import requests
from bs4 import BeautifulSoup
```

### Implement the Script Logic

- Make a request to the URL.
- Use BeautifulSoup to clean up the HTML.
- Save the cleaned HTML as a temporary file.
- Use headless Chrome to generate a PDF from the saved HTML file.

## Running the Script

Run the script from the command line:

```sh
python pdf.py
```

Enter the desired URL when prompted. The script will generate a PDF and save it as `output.pdf`.

## Troubleshooting

- **Chrome is not found**: Ensure Chrome is installed and added to your system PATH.
- **Invalid URL**: Make sure you enter a valid, reachable URL.
- **PDF not generated**: Check if the script has permission to write files and if Chrome executed correctly.

This script provides a simple way to convert web pages to PDFs using Python and headless Chrome. Happy coding! 🚀
