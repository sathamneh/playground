# Simple PDF OCR function, only scans the 1st page of PDF file.
# Uses pytesseract to perform OCR on a PDF
#
# Use it at your own risk. 
# The provided code is reusable and offered "as-is" without any warranties. 
# Attribution to the author is at your discretion.
# find this code and other at: https://github.com/sathamneh/playground 

#'''
# make sure you have Tesseract installed
# https://tesseract-ocr.github.io/tessdoc/Installation.html
#
# requirements:
# pip install pdf2image Pillow pytesseract
#'''


import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import logging

def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path, first_page=1, last_page=1)
    
    return images[0]

def ocr_image(image):
    try:
        # Check if the input is a valid image
        if not isinstance(image, Image.Image):
            raise ValueError("Invalid image provided. Expected a PIL.Image.Image object.")
        
        # Perform OCR on the image
        text = pytesseract.image_to_string(image)
        logging.debug(f"Extracted Text:\n{text}")
        
        return text
    except Exception as e:
        # Log the error and return an error message
        logging.error(f"OCR failed: {e}")
        return "OCR failed due to an error."


def main(pdf_path):
    try:
        image = pdf_to_image(pdf_path)
        logging.debug(f"PDF_TO_IMAGE: Processing {pdf_path}")
        text = ocr_image(image)
        logging.debug(f"OCR_IMAGE: Processing {image}")
        print("Extracted Text:\n", text)
        
        
        logging.debug(f"EXTRACT_PATENT_INFO: Processing {text}")
       
        return text
    except Exception as e:
        logging.error(f"An error occurred while processing the PDF: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main("your_pdf_file.pdf")
    