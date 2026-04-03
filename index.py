print("Hello!! I'm Todo!!, your personal assistent here to help you manage your tasks")
import os 
import csv
if "log.csv" not in os.listdir():
    with open("log.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(["task","status"])