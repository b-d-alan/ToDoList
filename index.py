print("Hello!! I'm Todo!!, your personal assistent here to help you manage your tasks")
import os 
import csv
if "log.csv" not in os.listdir():
    with open("log.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(["id","task","status"])
def new_task(input):
    with open("log.csv","a") as f:
        reader = csv.reader(f):
        rows=[]
        for row in reader:
            rows.append(row)
        writer= csv.writer(f)
        writer.writerow([len(rows),f"{input.split()[1:]}","pending"])
def show_tasks():
    with open("log.csv","r") as f:
        reader=csv.reader(f)
        for row in reader:
            if row[2]=="pending":
                print(row)
def task_completed(input):
    data=[]
    with open("log.csv","r") as f:
        reader=csv.reader(f)
        for row in reader:
            data.append(row)
    for i in range(len(data)):
        if data[i][0]==input.split()[1]:
            data[i][2]="completed"
    with open("log.csv","w") as f:
        writer=csv.writer(f)
        writer.writerows(data)
while True:
    show_tasks()
    input=input("enter your command: ")
    if input.startswith("new_task"):
        new_task(input)
    elif input.startswith("done"):
        task_completed(input)
    elif input=="quit":
        break