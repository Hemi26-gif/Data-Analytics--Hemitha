file=open(r,"r")
print(file.read())

with open(r"D:\downloads\Foundation\Foundation\oops\File Handling\file.txt","r") as file:
    content=file.read()
    print(content)

with open(r"D:\downloads\Foundation\Foundation\oops\File Handling\file.txt","r+") as file:
    content=file.write("Raj")
    print(content)

lines = ["Logesh\n", "Loki\n", "Logu\n"]

with open(r"D:\downloads\Foundation\Foundation\oops\File Handling\file.txt", "w") as file:
    file.writelines(lines)

with open(r"D:\downloads\Foundation\Foundation\oops\File Handling\file.txt", "r") as file:
    lines = file.readlines()
    print(lines)