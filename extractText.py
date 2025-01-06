import PyPDF2
from csv import DictWriter 

def extract_text_from_pdf(pdf_file, output_txt_file):
    """
    Extracts text from a PDF file and saves it to a text file.

    :param pdf_file: Path to the PDF file.
    :param output_txt_file: Path to the output text file.
    """
    try:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)
            print(f"Total Pages in PDF: {total_pages}\n")

            # Open a text file to save the output
            with open(output_txt_file, 'w', encoding='utf-8') as output_file:
                header_list = ['WORD', 'Phonetic Symbol', 'Meaning']
                dw = DictWriter(output_file, delimiter=',',  
                        fieldnames=header_list) 
                dw.writeheader() 
                for page_num in range(total_pages):
                    page = reader.pages[page_num]
                    text = page.extract_text().split(" ")
                    for word in text:
                        
                        if len(word.strip()) > 1 and word.strip().isalpha():
                            print("word: {} length: {}".format(word.strip(), len(word.strip())))
                            #output_file.writer(f"{word.strip()}\n")
                            dw.writerow({
                                'WORD': f"{word.strip()}\n",
                                'Phonetic Symbol': '',
                                'Meaning': ''
                                })
                    
            print(f"Text extracted and saved to {output_txt_file}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__=='__main__':
    pdf_path = "Letter R.pdf"
    output_path = "Letter R.csv"
    extract_text_from_pdf(pdf_path, output_path)