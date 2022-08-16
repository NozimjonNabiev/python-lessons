# 34-dars: JSON
# Sana: 16/08/2022
# Muallif: Nozimjon Nabiev

import json

# data = {
#         "Model":"Malibu",
#         "Rang":"Qora",
#         "Yil":2020,
#         "Narx":40000
#         }

# data2 = json.dumps(data, indent=4)
# # print(data2)

# talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}

# with open('data.json', 'w') as file:
#     json.dump(data, file)

# with open('talaba.json', 'w') as fayl:
#     json.dump(talaba_json, fayl)
    

# with open('students.json') as files:
#     students = json.load(files)

# for i in range(3):
#     print(f"Ismi-familiyasi: {students['student'][i]['name']} {students['student'][i]['lastname']}")
#     print(f"{students['student'][i]['year']}-kurs")
#     print(students['student'][i]['faculty'] + " fakulteti talabasi\n")


with open('api-result.json') as file_p:
    python_wiki = json.load(file_p)

print(python_wiki['query']['pages']['13801']['title'].upper())
print(python_wiki['query']['pages']['13801']['extract'])