from selenium import webdriver
from bs4 import BeautifulSoup
from xhtml2pdf import pisa

def modify_layout(html_content):
    # Parse HTML content
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Example: Change background color of all <div> elements
    div_elements = soup.find_all("div")
    for div in div_elements:
        div["style"] = "background-color: lightblue;"

    # Example: Change font size of all <p> elements
    p_elements = soup.find_all("p")
    for p in p_elements:
        p["style"] = "font-size: 14px;"

    # Return modified HTML content
    return str(soup)

def convert_html_to_pdf(html_content, output_path):
    # Define CSS styles for formatting
    css = """
    body {
        font-family: Arial, sans-serif;
        font-size: 12px;
        line-height: 1.5;
        margin: 20px;
    }
    h1 {
        color: #333333;
        font-size: 24px;
        text-align: center;
    }
    """

    # Convert HTML to PDF with custom options
    options = {
        "css": css,
        "encoding": "utf-8",
        "page-size": "A4",
        "margin-top": "20mm",
        "margin-right": "20mm",
        "margin-bottom": "20mm",
        "margin-left": "20mm",
    }
    with open(output_path, "wb") as output_file:
        pisa_status = pisa.CreatePDF(html_content, dest=output_file, **options)
    if pisa_status.err:
        print(f"Failed to convert HTML to PDF: {pisa_status.err}")
    else:
        print(f"PDF successfully created at: {output_path}")

def main():
    url = "https://www.sec.gov/ixviewer/ix.html?doc=/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm"
    output_path = "output.pdf"

    # Use Selenium to fetch fully rendered HTML content
    driver = webdriver.Chrome()  # Provide path to your chromedriver if not in PATH
    driver.get(url)
    html_content = driver.page_source

    # Modify layout of HTML content
    modified_html = modify_layout(html_content)

    # Convert modified HTML to PDF
    convert_html_to_pdf(modified_html, output_path)

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    main()
