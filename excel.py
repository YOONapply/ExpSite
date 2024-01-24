import csv
import json
import funtionJson as fJ

# 주어진 JSON 데이터
json_data = fJ.userDataLoad()

# JSON 데이터를 CSV로 변환
csv_data = [["name", "stuId", "snsId", "email",  "schedule", "stuM"]]
for item in json_data:
    csv_data.append([item["name"], item["stuId"], item["snsId"], item["email"], item["schedule"], item["stuM"]])

# CSV 파일로 저장
with open("./data/data.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(csv_data)
