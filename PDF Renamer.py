# Read PDF files for the applicant name and rename the file according to their name. Only works with specific files from my old appartment complex.

import PyPDF2
import os
import os.path
from os import path

lower_bound = int(input("Enter the lower bound for the Application Number: "))
upper_bound = int(input("Enter the upper bound for the Application Number: "))
print()

for counter in range(lower_bound, upper_bound + 1):
    pdf_name = 'Application (' + str(counter) + ').pdf'
    print("Original name: ", pdf_name)

    file_obj = open(pdf_name, 'rb')

    pdf_reader = PyPDF2.PdfFileReader(file_obj)

    page = pdf_reader.getPage(0)

    text_file = open('Applicant.txt', 'w+')

    page_text = page.extractText()

    text_file.write(page_text)

    text_file.close()

    stringText = ''
    count = 0

    text_file = open ('Applicant.txt', 'r')
    for line in text_file:
        for part in line.split(':'):
            count += 1
            stringText += part
            stringText += '\n'
            stringText += str(count)
            stringText += ') '
    text_file.close()

    text_file = open('Applicant.txt', 'w')
    text_file.write(stringText)
    text_file.close()

    text_file = open ('Applicant.txt', 'r')
    stringLine = ''
    found = False
    for line in text_file:
        if (found == False and "6)" in line):
            stringLine += line
            break
    #print(stringLine)
    applicant_name = stringLine.replace("Applicant Type", "")
    #print(applicant_name)
    applicant_name = applicant_name.replace("6) ", "")

    applicant_name = applicant_name.rstrip("\n\r")
    file_obj.close()
    
    if path.exists(applicant_name + '.pdf'):
        print("File already exists!")
        
    else:
        os.rename(pdf_name, applicant_name + '.pdf')
        print("Renamed to: ", applicant_name + '.pdf')
        
    print()

    


            








