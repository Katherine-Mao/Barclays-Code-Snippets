import requests
from xhtml2pdf import pisa

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

    # Fetch HTML content from URL
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        # Convert HTML to PDF
        convert_html_to_pdf(html_content, output_path)
    else:
        print(f"Failed to fetch HTML content from {url}")

if __name__ == "__main__":
    main()
