import os
import csv

path_ryan_train = "train/Ryan"
path_ryan_test = "test/Ryan"
path_ryan_valid = "valid/Ryan"
path_not_train = "train/notRyan"
path_not_test = "test/notRyan"
path_not_valid = "valid/notRyan"


with open("character.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["class", "filepaths", "labels", "dateset"])
    for root, dirs, files in os.walk(path_ryan_train):
        for filename in files:
            writer.writerow(["1", os.path.join(root, filename), "ryan", "train"])
    for root, dirs, files in os.walk(path_ryan_test):
        for filename in files:
            writer.writerow(["1", os.path.join(root, filename), "ryan", "test"])
    for root, dirs, files in os.walk(path_ryan_valid):
        for filename in files:
            writer.writerow(["1", os.path.join(root, filename), "ryan", "valid"])
    for root, dirs, files in os.walk(path_not_train):
        for filename in files:
            writer.writerow(["0", os.path.join(root, filename), "notRyan", "train"])
    for root, dirs, files in os.walk(path_not_test):
        for filename in files:
            writer.writerow(["0", os.path.join(root, filename), "notRyan", "test"])
    for root, dirs, files in os.walk(path_not_test):
        for filename in files:
            writer.writerow(["0", os.path.join(root, filename), "notRyan", "valid"])
