# from openpyxl import load_workbook

# wb = load_workbook(filename = 'Word Meaning Phonetic.xlsx')
# sheet = wb.active

# sheet_title = sheet.title 
  
# print("active sheet title: " + sheet_title)

# rows_to_delete = ['', ' ']
# column_b = range(1, sheet.max_row)
# for i in reversed(column_b):
#     if sheet.cell(i, 2).value in rows_to_delete:
#         print(f'Deleting Row: {sheet.cell(i,2).row}')
#         sheet.delete_rows(sheet.cell(i,2).row)

# wb.save('Word Meaning Phonetic.xlsx')

from csv import DictReader, DictWriter 
import requests

with open('Letter R.csv', 'r') as rf:
    csv_reader = DictReader(rf)
    with open('Letter R-final.csv', 'w') as wf:
        csv_writer = DictWriter(wf, fieldnames=['WORD', 'Phonetic Symbol', 'Meaning'])
        csv_writer.writeheader()
        
        header = {"x-rapidapi-key":"cd03b92573mshfd6e5ff9e8e036fp1a7b42jsna41ec9d4479d"}
        for row in csv_reader:
            phonetic = 'N/A'
            definition = 'N/A'
            if row["WORD"] is not None and row["WORD"] != "":
                response = requests.get("https://wordsapiv1.p.rapidapi.com/words/{}".format(row["WORD"].strip().lower()), headers=header)
                
                if response.status_code == 200:
                    data = response.json()
                    if "pronunciation" in data and len(data["pronunciation"]) == 0 and isinstance(data["pronunciation"], dict):
                        phonetic = 'N/A'
                    elif "pronunciation" in data and len(data["pronunciation"]) > 0 and isinstance(data["pronunciation"], dict):
                        try:
                            phonetic = data["pronunciation"]["all"] if "pronunciation" in data and "all" in data["pronunciation"] else 'N/A'
                        except KeyError:
                            phonetic = data["pronunciation"]["verb"] if "pronunciation" in data and "verb" in data["pronunciation"] else 'N/A'

                    else:
                        phonetic = data["pronunciation"] if "pronunciation" in data else 'N/A'
                        
                    defination = data["results"][0].get('definition', 'N/A') if "results" in data and data["results"] is not None and data["results"].__len__() > 0 else 'N/A'
    
                    print(row["WORD"])
                    print("phonetic : {}".format(phonetic))
                    print("definition : {}".format(defination))
                    print("---------------------------------------------------")
                else:
                    print(f"{row['WORD']}: Not found")
                csv_writer.writerow({
                'WORD': row["WORD"].lower(),
                'Phonetic Symbol': phonetic,
                'Meaning': defination
                })
                


    