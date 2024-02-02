import requests
import pdfkit

def fetch_sec_filing_html(ticker, filing_type, output_path):
    # Fetch SEC filing in HTML format
    url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={ticker}&type={filing_type}&dateb=&owner=exclude&count=40"
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"SEC filing HTML saved at: {output_path}")
    else:
        print(f"Failed to fetch SEC filing HTML for {ticker}")

def convert_html_to_pdf(input_path, output_path):
    # Convert HTML to PDF
    pdfkit.from_file(input_path, output_path)
    print(f"PDF successfully created at: {output_path}")

def main():
    ticker = input("Enter stock ticker: ")
    filing_type = input("Enter filing type (e.g., 10-K, 10-Q): ")
    output_html_path = "sec_filing.html"
    output_pdf_path = "sec_filing.pdf"

    fetch_sec_filing_html(ticker, filing_type, output_html_path)
    convert_html_to_pdf(output_html_path, output_pdf_path)

if __name__ == "__main__":
    main()
