import json
import csv 

employee = [["Name", "Age", "job"],
            ["Juice", 21, "Freestyler"],
            ["Roger", 16, "Student"],
            ["Kanye", 48, "Rapper"]]

file_path = "/home/roger/Desktop/output.json" 

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent= 4)
        print(f"json file '{file_path}' was created ")
except FileExistsError:
    print("That file already exists!")
except ValueError:
    print("Write the mode of the file")








