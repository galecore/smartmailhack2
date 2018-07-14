import requests

base_url = "https://e.mail.ru/api/v1/messages/"
email = "&email=smartmail_team3@mail.ru&"
token = "access_token=e5305a9cbb38716fafad3a0de027eafc140c5fb537363830"

def get_all_letters_by_query(query):
    url = base_url + "search?query=" + query + "&limit=1&" + email + token 
    response = requests.get(url).json()["body"]
    count = response["found"]["count"]
    
    ids = list()
    for i in range(0, count, 100):
        url = base_url + "search?query=" + query + "&offset=" + str(i) + "&limit=100&" + email + token 
        print(url)
        messages = requests.get(url).json()["body"]["messages"]
        for m in messages:
            ids.append(m["id"])
    return ids

def get_all_letters_by_id(ids):
    letters = list()
    for id in ids:
        url = base_url + "message?id="+ str(id) + email + token 
        response = requests.get(url).json()["body"]
        from_obj = response["replies"]["to"][0]
        subject = response["subject"]
        body = response["body"]
        date = response["date"]
        letters.append({"from":from_obj, "subject":subject, "body":body, "id":id, "date":date})
    return letters


ids = get_all_letters_by_query("Скидка")
letters = get_all_letters_by_id(ids)

import json
with open("raw_letters.json", 'w') as raw_letters_file:
    json.dump(letters, raw_letters_file)

print("Loaded.")