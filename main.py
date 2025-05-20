'''
SPECT AI - Interview Take Home Assignment
Author: Ian Mendoza Juarez
Date: May 20, 2025
'''
from openai import OpenAI 
import pandas as pd
#import os Irrelevant for this task since only devs will see this.
#openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
client.files.create(
    file = open("pdfFilePath", "rb"),
    purpose = "user_data"
)






# Possible variables:
# extractedData = [] Somewhere that stores the Product Name and Manufacturer Name. Page num as well, but later.
# Need some sort of map to avoid logging duplicates. i.e. prodMap {} with the Key being Product Name and Manu. Value = which page numbers they can be found?

#Reference, basic start to learning how to use OpenAI api : "https://www.youtube.com/shorts/ZkFKF-ohsKk"
#https://platform.openai.com/docs/quickstart?api-mode=responses
#I think i found the magic sauce https://platform.openai.com/docs/guides/pdf-files?api-mode=responses



def PLACEHOLDER(pdfFilePath):
    #Iterate through each page
    for pageNum in pdfFilePath: #from page 1 (index 0) to the last page (pdfFilePath.pageCount - 1)

         
    #Extract Data following constraints. Bonus, page number tracking. Learn OpenAI APi and how to use it effectively.
    #Kaboom, CSV output


    return dataCSV
'''
Parameters:
Input: pdfPath
Output: CSV file
'''
