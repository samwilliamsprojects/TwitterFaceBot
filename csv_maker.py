import csv
import os
# Creates the CSV that will map your data for the Tensorflow model

header = ["class", "filepaths", "labels", "dateset"]

with open("characters.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(header)

with open("characters.csv", "a") as f:
    for file in os.listdir("train/Ryan"):
        writer = csv.writer(f)
        writer.writerow(["0", f"train/Ryan/{file}", "Ryan", "train"])

with open("characters.csv", "a") as g:
    for file in os.listdir("train/notRyan"):
        writer = csv.writer(g)
        writer.writerow(["1", f"train/notRyan/{file}", "notRyan", "train"])

with open("characters.csv", "a") as h:
    for file in os.listdir("test/Ryan"):
        writer = csv.writer(h)
        writer.writerow(["0", f"test/Ryan/{file}", "Ryan", "test"])

with open("characters.csv", "a") as p:
    for file in os.listdir("test/notRyan"):
        writer = csv.writer(p)
        writer.writerow(["1", f"test/notRyan/{file}", "notRyan", "test"])

with open("characters.csv", "a") as b:
    for file in os.listdir("valid/Ryan"):
        writer = csv.writer(b)
        writer.writerow(["0", f"valid/Ryan/{file}", "Ryan", "valid"])

with open("characters.csv", "a") as s:
    for file in os.listdir("valid/notRyan"):
        writer = csv.writer(s)
        writer.writerow(["1", f"valid/notRyan/{file}", "notRyan", "valid"])
