# from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_text
import os
import re
import json

#Test
def extract_text_from_pdf(pdf_path):
    output = {}
    match_flg = False
    try:
        text = extract_text(pdf_path)
        lines = text.split('\n')
        pattern = re.compile('(Step)(\s*-\s*)(\d+)\s*[:\[\(]\s*([^:\[\)]+)\s*[^\]\)]*')
        for data in lines:
            if data == '':
                continue
            if match_flg:
                output.get('Step ' + match.group(3)).append(data)
                match_flg = False
            match = re.search(pattern, data)
            if match:
                output['Step '+match.group(3)] = [match.group(4)]
                match_flg = True
        return output
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

def generate_output_json(data, file_path):
    output_file_path = "output.json"
    json_file = file_path+output_file_path
    print("Json file path::", json_file)
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    file_base_path = os.getcwd()
    input_file_path = "\\pdfscrap_01\\Input\\"
    output_file_path = "\\pdfscrap_01\\Output\\"
    input_file_complete_path = file_base_path + input_file_path
    output_file_complete_path = file_base_path + output_file_path
    pdf_file_name = "Devops.pdf"
    pdf_file = os.path.join(input_file_complete_path, pdf_file_name)
    output_path = "output_data"
    pdf_data = extract_text_from_pdf(pdf_file)
    json_file_write = generate_output_json(pdf_data, output_file_complete_path)
    print("Output::",pdf_data, json_file_write)
