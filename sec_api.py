import requests

def generate_pdf_from_sec_filing(cik, accession_number, output_path):
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key

    url = f"https://api.sec-api.io/filings/{cik}/{accession_number}/render"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    params = {
        "type": "pdf"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"PDF successfully created at: {output_path}")
    else:
        print(f"Failed to generate PDF: {response.text}")

def main():
    cik = "320193"  # Example CIK for Apple Inc.
    accession_number = "000032019323000106"  # Example accession number
    output_path = "output.pdf"

    generate_pdf_from_sec_filing(cik, accession_number, output_path)

if __name__ == "__main__":
    main()
