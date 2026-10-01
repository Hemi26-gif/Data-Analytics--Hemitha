
# import csv

# with open(r"D:\downloads\Foundation\Foundation\oops\File Handling\data.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"], row["Dept"])

import csv

with open(r"D:\downloads\Foundation\Foundation\File Handling\data.csv","r") as file:

    # reader=csv.reader(file)
    # for row in reader:
    #     print(row)
    # print(file)
    # reader=csv.DictReader(file)
    # for row in reader:
    #         print(row["dept"])

    writer = csv.writer(file)
    writer.writerow(["Logesh","cse"])
    header_rows = ["name","Dept"]

    # writer = csv.DictWriter(file,fieldnames=header_rows)
    # writer.writeheader()
    # writer.writerow({"Name":"selvam","Dept":"cse"})


