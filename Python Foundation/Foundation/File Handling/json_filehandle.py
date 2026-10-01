
import json

with open(r"D:\downloads\Foundation\Foundation\File Handling\stud_data.json","r") as j_file:

    student=json.load(j_file)
    print(student["marks"]["SQL"])