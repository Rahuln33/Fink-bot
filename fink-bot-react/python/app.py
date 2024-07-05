# # from bs4 import BeautifulSoup
# # import requests
# # import json

# # def scrape_page(url):
# #     response = requests.get(url)
# #     if response.status_code != 200:
# #         return None
    
# #     soup = BeautifulSoup(response.content, 'html.parser')
    
# #     # Extract text content from the page
# #     text_content = soup.get_text(separator='\n', strip=True)
# #     return text_content

# # def scrape_finkraft():
# #     base_url = 'https://finkraft.ai/'
# #     pages = {
# #         'about': base_url + 'about',
# #         'solutions': base_url + 'solutions',
# #         'compliance': base_url + 'compliance',
# #         'resources': base_url + 'resources',
# #         'contact': base_url + 'contact',
# #         'demo': base_url + 'demo'
# #     }
    
# #     scraped_data = {}
# #     for key, url in pages.items():
# #         scraped_data[key] = scrape_page(url)
    
# #     return scraped_data

# # # Scrape the data and save it to a JSON file
# # scraped_data = scrape_finkraft()
# # with open('finkraft_data.json', 'w') as file:
# #     json.dump(scraped_data, file)

# # # Load the scraped data from the JSON file
# # with open('finkraft_data.json', 'r') as file:
# #     finkraft_data = json.load(file)

# # def search_finkraft_data(query):
# #     results = []
# #     for section, content in finkraft_data.items():
# #         if query.lower() in content.lower():
# #             results.append((section, content))
# #     return results

# # # Example usage: Search for a query in the scraped data
# # query = "AI solutions"
# # search_results = search_finkraft_data(query)
# # for section, content in search_results:
# #     print(f"Section: {section}\nContent: {content}\n")

# from bs4 import BeautifulSoup
# import requests
# import json

# def scrape_page(url):
#     response = requests.get(url)
#     if response.status_code != 200:
#         return None
    
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Extract text content from the page
#     text_content = soup.get_text(separator='\n', strip=True)
#     return text_content

# def scrape_finkraft():
#     base_url = 'https://finkraft.ai/'
#     pages = {
#         'about': [
#             base_url + 'about',
#             base_url + 'about/partners.html',
#             base_url + 'about/offices.html'
#         ],
#         'solutions': [
#             base_url + 'solutions',
#             base_url + 'solutions/airline-&-hotel-gst-itc-automation.html',
#             base_url + 'solutions/gst-invoice-distribution.html',
#             base_url + 'solutions/gst-invoice-automation.html'
#         ],
#         'compliance': [
#             base_url + 'compliance',
#             base_url + 'compliance/compliance-overview.html'
#         ],
#         'resources': [
#             base_url + 'resources',
#             base_url + 'resources/case-studies.html'
#         ],
#         'contact': base_url + 'contact',
#         'demo': [
#             base_url + 'demo',
#             base_url + 'book-a-demo.html'
#         ],
#         'careers': base_url + 'careers/',
#         'social': {
#             'facebook': 'https://www.facebook.com/people/Finkraft/100069918660246/',
#             'twitter': 'https://x.com/finkraft1',
#             'instagram': 'https://www.instagram.com/finkraft.ai/',
#             'linkedin_company': 'https://www.linkedin.com/company/finkraft-ai/',
#             'linkedin_people': 'https://www.linkedin.com/company/finkraft-ai/people/',
#             'linkedin_about': 'https://www.linkedin.com/company/finkraft-ai/about/'
#         }
#     }
    
#     scraped_data = {}
#     for key, urls in pages.items():
#         if isinstance(urls, list):
#             scraped_data[key] = {}
#             for i, url in enumerate(urls):
#                 page_key = f"{key}_{i+1}"
#                 scraped_data[key][page_key] = scrape_page(url)
#         elif isinstance(urls, dict):
#             scraped_data[key] = {}
#             for sub_key, url in urls.items():
#                 scraped_data[key][sub_key] = scrape_page(url)
#         else:
#             scraped_data[key] = scrape_page(urls)
    
#     return scraped_data

# # Scrape the data and save it to a JSON file
# scraped_data = scrape_finkraft()
# with open('finkraft_data.json', 'w') as file:
#     json.dump(scraped_data, file)

# # Load the scraped data from the JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# def search_finkraft_data(query):
#     results = []
#     for section, content in finkraft_data.items():
#         if isinstance(content, dict):
#             for sub_section, sub_content in content.items():
#                 if sub_content and query.lower() in sub_content.lower():
#                     results.append((f"{section} - {sub_section}", sub_content))
#         else:
#             if content and query.lower() in content.lower():
#                 results.append((section, content))
#     return results

# # Example usage: Search for a query in the scraped data
# query = "AI solutions"
# search_results = search_finkraft_data(query)
# for section, content in search_results:
#     print(f"Section: {section}\nContent: {content}\n")

import os
import jwt
import fitz  # PyMuPDF
from pyzbar.pyzbar import decode
from PIL import Image
import io
import pandas as pd
import ast
import requests
import logging


# Configure logging without timestamp
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def extract_qr_codes_from_pdf(pdf_path):
    qr_data_list = []
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        
        # Variable to track if an error has been logged for this PDF
        error_logged = False
        
        # Iterate through each page
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            images = page.get_images(full=True)
            
            # Iterate through each image
            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                
                # Convert bytes to an image
                if image_bytes and len(image_bytes) > 0:
                    try:
                        image = Image.open(io.BytesIO(image_bytes))
                        # Decode the QR code
                        decoded_objects = decode(image)
                        for obj in decoded_objects:
                            qr_data = obj.data.decode("utf-8")
                            qr_data_list.append(qr_data)
                    except Exception as e:
                        # Log error if it hasn't been logged already
                        if not error_logged:
                            logging.error(f"Error extracting QR codes from {pdf_path}: {e}")
                            error_logged = True
                else:
                    logging.warning(f"Empty or invalid image bytes for page {page_num}, image index {img_index}")
            
    except Exception as e:
        logging.error(f"Error opening PDF {pdf_path}: {e}")
    finally:
        if pdf_document:
            pdf_document.close()
    return qr_data_list

def process_jwt_data(jwt_data, s3_url):
    try:
        decoded_token = jwt.decode(jwt_data, options={"verify_signature": False})
        logging.info(f"Decoded JWT token: {decoded_token}")
        data = ast.literal_eval(decoded_token['data'])
        return {
            'S3_URL': s3_url,
            'SellerGstin': data.get('SellerGstin', ''),
            'BuyerGstin': data.get('BuyerGstin', ''),
            'DocNo': data.get('DocNo', ''),
            'DocTyp': data.get('DocTyp', ''),
            'DocDt': data.get('DocDt', ''),
            'TotInvVal': data.get('TotInvVal', ''),
            'ItemCnt': data.get('ItemCnt', ''),
            'MainHsnCode': data.get('MainHsnCode', ''),
            'Irn': data.get('Irn', ''),
            'IrnDt': data.get('IrnDt', ''),
        }
    except jwt.exceptions.DecodeError as e:
        logging.error(f"Error decoding JWT token: {e}")
        return None

def download_file_from_s3(s3_url, output_directory):
    try:
        # Extract file name from URL
        file_name = s3_url.split('/')[-1]
        # Create local file path
        local_file_path = os.path.join(output_directory, file_name)
        # Download file from S3
        response = requests.get(s3_url, stream=True)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        # Save file locally
        with open(local_file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        logging.info(f"Downloaded: {file_name}")
        return local_file_path
    except requests.exceptions.RequestException as e:
        logging.error(f"Error downloading {s3_url}: {e}")
        return None

def download_files_from_csv(csv_file, output_directory):
    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    # Load CSV file
    try:
        df = pd.read_csv(csv_file)
    except pd.errors.EmptyDataError:
        logging.error(f"CSV file '{csv_file}' is empty or could not be read.")
        return

    # Ensure 'S3_URL' column exists
    if 'S3_URL' not in df.columns:
        logging.error("CSV file does not contain 'S3_URL' column.")
        return

    # List to store extracted data
    extracted_data = []
    
    # Iterate through each S3 URL
    for index, row in df.iterrows():
        s3_url = row['S3_URL']
        pdf_path = download_file_from_s3(s3_url, output_directory)
        if pdf_path:
            qr_codes = extract_qr_codes_from_pdf(pdf_path)
            for qr_code in qr_codes:
                jwt_data = qr_code.strip()
                if jwt_data.startswith('eyJ'):  # Assuming JWT token starts with 'eyJ'
                    jwt_info = process_jwt_data(jwt_data, s3_url)  # Pass both jwt_data and s3_url
                    if jwt_info:
                        extracted_data.append(jwt_info)
    
    # Convert extracted data to DataFrame
    extracted_df = pd.DataFrame(extracted_data)
    # Save to CSV file
    csv_output_file = 'extracted_data.csv'
    extracted_df.to_csv(csv_output_file, index=False)
    logging.info(f"Extracted data saved to {csv_output_file}")

if __name__ == "__main__":
    csv_file = 'sample.csv'  # Replace with your CSV file path
    output_directory = 's3_files'  # Output directory where files will be saved

    # Download files from S3 URLs listed in CSV and extract JWT data
    download_files_from_csv(csv_file, output_directory)
