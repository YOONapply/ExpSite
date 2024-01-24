import json

def userDataLoad():
    with open("./data/userData.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def userDataDump(result):
    data = userDataLoad()
    data.append(result)

    with open("./data/userData.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(data)  # 디버깅용 출력