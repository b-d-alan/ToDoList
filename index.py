print()
print()
print()
print("Hello!! I'm Todo!!, your personal assistent here to help you manage your tasks")
import os
import csv

if "log.csv" not in os.listdir():
    with open("log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Id", "Task", "Status"])


def new_task(input):
    with open("log.csv", "r", newline="") as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)
    with open("log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([len(rows), input, "pending"])


def show_tasks(a=None):
    print()
    with open("log.csv", "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            if len(row) != 3:
                print()
                print(row)
                print("row length not equal to 3")
                print()
                continue
            if row[2] == "pending":
                for i in row:
                    print(i, end=" ")
                print()


def task_completed(input):
    data = []
    with open("log.csv", "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        data = [row for row in reader]
    for i in range(len(data)):
        if len(data[i]) != 3:
            print()
            print(data[i])
            print("row length not equal to 3")
            print()
            continue
        if data[i][0] == input:
            data[i][2] = "completed"
    with open("log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Id", "Task", "Status"])
        writer.writerows(data)


def _help(a=None):
    print()
    print("new <task_name>: creates a new task with the name <task_name>")
    print("done <task_id>: marks the task with the id <task_id> as completed")
    print("show: shows all the pending tasks")
    print(
        "cleanup_logs: deletes logs with empty <task_name> and blank lines in the csv file"
    )
    print("exit: shuts down the program")
    print()


def cleanup_csvfile(a=None):
    no_of_rows_deled = 0
    with open("log.csv", "r") as file:
        reader = csv.reader(file)
        reader = list(reader)
        data = [row for row in reader if row != [] and row[1].strip() != ""]
        no_of_rows_deled = len(reader) - len(data)
    with open("log.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Cleanup successful")
    print(no_of_rows_deled, " deleted")


def powering_down(a=None):
    print()
    print("powering down...")
    print("Until later!!!")
    print("Peace!!")
    return "break"


command_keyword = ""
command_argument = ""
command_function_hashing = {
    "new": new_task,
    "done": task_completed,
    "show": show_tasks,
    "_help": _help,
    "cleanup_logs": cleanup_csvfile,
    "exit": powering_down,
}

show_tasks()
while True:
    command = input("enter your command: ")
    if command == "":
        continue
    command_keyword = command.split()[0]
    command_argument = " ".join(command.split()[1:])
    if command_keyword in command_function_hashing:
        if command_function_hashing[command_keyword](command_argument) == "break":
            break
    else:
        print("invalid command", "enter '_help' for help regarding commands", sep="\n")
