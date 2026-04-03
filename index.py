print("Hello!! I'm Todo!!, your personal assistent here to help you manage your tasks")
import os 
import csv
if "log.csv" not in os.listdir():
    with open("log.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(["task","status"])
def new_task(input):
    with open("log.csv","a") as f:
        writer= csv.writer(f)
        writer.writerow([f"{input.split()[1:]}","pending"])
def show_task():
    with open("log.csv","r") as f:
        reader=csv.reader(f)
        for row in reader:
            if row[1]=="pending":
                print(row[0])