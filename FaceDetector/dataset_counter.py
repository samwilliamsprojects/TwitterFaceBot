import os

i = 0
for file in os.listdir("train/Ryan"):
    i += 1
j = 0
for file in os.listdir("train/notRyan"):
    j += 1
k = 0
for file in os.listdir("test/Ryan"):
    k += 1
m = 0
for file in os.listdir("test/notRyan"):
    m += 1
n = 0
for file in os.listdir("valid/Ryan"):
    n += 1
v = 0
for file in os.listdir("valid/notRyan"):
    v += 1
print("files in training for Ryan: " + str(i) + " and not Ryan: " + str(j))
print("files in testing for Ryan: " + str(k) + " and not Ryan: " + str(m))
print("files in validation for Ryan: " + str(n) + " and not Ryan: " + str(v))
