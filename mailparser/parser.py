import re
import json
import datetime

raw_letters = None
with open("raw_letters.json", 'r') as raw_letters_file:
    raw_letters = json.load(raw_letters_file)
timestamp_regex = r"(по|до) (((\d\d?) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря))|(\d\d?\.\d\d?(.(\d\d)?\d\d)?))"

month_to_number = {"января":"01", "февраля":"02", "марта":"03",
                   "апреля":"04", "мая":"05", "июня":"06", "июля":"07", "августа":"08", 
                   "сентября":"09", "октября":"10", "ноября":"11", "декабря":"12"}

def extract_date(text, start, end):
    str_date = text[start:end][3:]

    for p in month_to_number:
        str_date = str_date.replace(p, month_to_number[p])
    if len(str_date.split()) == 2:
        str_date = ".".join((str_date + " 2018").split())
    return str_date

def get_letter_data(raw_letter):
    from_date = datetime.datetime.fromtimestamp(raw_letter["date"]).strftime('%d.%m.%Y')
    to_date = None
    text = None
    
    date_match = re.search(timestamp_regex, raw_letter["body"]["text"])
    if date_match:
        text = raw_letter["body"]["text"]
        start, end = date_match.span()
        to_date = extract_date(text, start, end)
    else:
        return None
    return {"from":from_date, "to":to_date, "text":'...'}


def get_direct_letter_link(raw_letter):
    return "https://e.mail.ru/message/" + raw_letter["id"]

def get_company_info(raw_letter):
    company = raw_letter["from"]["name"]
    picture = raw_letter["from"]["avatars"]["50x50"]
    return company, picture

def process_letters(raw_letters):
    letters = list()
    for raw_letter in raw_letters:
        company, picture = get_company_info(raw_letter)
        data = get_letter_data(raw_letter)
        link = get_direct_letter_link(raw_letter)
        subject = raw_letter["subject"]
        letter = { "company":company, "picture":picture, "data":data, "link":link, "subject":subject}
        letters.append(letter)
    letters = filter_dates(letters)
    return letters

def filter_dates(letters):
    return list(filter(lambda x: x["data"], letters))

def order_by_companies(letters):
    unique_companies = set(i["company"] for i in letters)
    ordered = {key:[] for key in unique_companies}
    for letter in letters:
        ordered[letter["company"]].append(letter)
    return ordered

letters = process_letters(raw_letters)
with open("letters.json", 'w') as letters_file:
    json.dump(letters, letters_file)
    
print("Parsed.")