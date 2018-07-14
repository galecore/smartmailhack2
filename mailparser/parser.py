import re
import json

raw_letters = None
with open("raw_letters.json", 'r') as raw_letters_file:
    raw_letters = json.load(raw_letters_file)

def get_company_info(raw_letter):
    company = raw_letter["from"]["name"]
    picture = raw_letter["from"]["avatars"]["50x50"]
    return company, picture

def get_letter_data(raw_letter):
    return {"from":"...", "to":"...", "text":"..."}

def get_direct_letter_link(raw_letter):
    return "https://e.mail.ru/message/" + raw_letter["id"]

def process_letters(raw_letters):
    letters = list()
    for i, raw_letter in enumerate(raw_letters):
        print("Current letter: " + str(i))
        company, picture = get_company_info(raw_letter)
        data = get_letter_data(raw_letter)
        link = get_direct_letter_link(raw_letter)
        letter = { "company":company, "picture":picture, "data":data, "link":link }
        letters.append(letter)
    return letters

letters = process_letters(raw_letters)
with open("letters.json", 'w') as letters_file:
    json.dump(letters, letters_file)

print("Parsed.")