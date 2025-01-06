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
from freedictionaryapi.clients.sync_client import DictionaryApiClient

with open('word.csv', 'r') as rf:
    csv_reader = DictReader(rf)
    with open('word-with-meaning-2.csv', 'w') as wf:
        csv_writer = DictWriter(wf, fieldnames=['WORD', 'Phonetic Symbol', 'Meaning'])
        csv_writer.writeheader()
        phonetic = 'N/A'
        definition = 'N/A'
        for row in csv_reader:
            if row["WORD"] is not None and row["WORD"] != "":
                #response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(row["WORD"]))

                with DictionaryApiClient() as client:
                    print("word: {}".format(row["WORD"]))
                    parser = client.fetch_parser(row["WORD"].lower())
                word = parser.word
                print(word)
                phonetic = word.phonetics[0].text
                print(phonetic)
                defination_list = []
                for meaning in word.meanings:
                    print(meaning.part_of_speech)
                    for definition in meaning.definitions:
                            print(definition)
                print("---------------------------------------------------")
            
                #  response.status_code == 200:
                #     data = response.json()
                #     phonetic = data[0].get('phonetic', 'N/A')
    
                #     meaning = data[0].get('meanings', 'N/A') if data[0].get('meanings') is not None and data[0].get('meanings').__len__() > 0 else 'N/A'
                #     if meaning is not None and meaning != 'N/A':
                #         definition = meaning[0].get('definitions')[0].get('definition', 'N/A')
                #     print(f"{row['WORD']}: {phonetific}")
                #     print(f"{row['Meaning']}: {definition}")
                #     print("---------------------------------------------------")
                # else:
                #     print(f"{row['WORD']}: Not found")
                # word= row['WORD']
                csv_writer.writerow({
                'WORD': word.word,
                'Phonetic Symbol': phonetic,
                'Meaning': 'N/A'
                })


    