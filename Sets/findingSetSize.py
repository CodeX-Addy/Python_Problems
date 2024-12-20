import sys

# sample Sets
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "X", "Geek2", "Y", "Geek3", "Z"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

print("Size of Set1: " + str(sys.getsizeof(Set1)) + "bytes")
print("Size of Set2: " + str(sys.getsizeof(Set2)) + "bytes")
print("Size of Set3: " + str(sys.getsizeof(Set3)) + "bytes")
