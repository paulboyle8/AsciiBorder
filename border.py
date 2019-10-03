size = input("Enter width of border in chars (Works best as odd number): ")

size = int(size)

print("Size: " + str(size) + "\n")

print(" ", end = '')
i = 1
while i < (size-2):
  print("_", end = '')
  i += 1
  
print("\n|", end = '')

i = 1
while i < (size-2):
  print("><", end = '')
  i += 2
print("|", end = '')

print("\n|><|", end = '')
i = 1
while i < (size-8):
  print("¯", end = '')
  i += 1
print("|><|", end = '')
    
j = 1
while j < (size/3.25):
    print("\n|><|", end = '')
    i = 1
    while i < (size-8):
      print(" ", end = '')
      i += 1
    print("|><|", end = '')
    j+=1

print("\n|><|", end = '')
i = 1
while i < (size-8):
  print("_", end = '')
  i += 1
print("|><|", end = '')

print("\n|", end = '')

i = 1
while i < (size-2):
  print("><", end = '')
  i += 2
print("|\n", end = '')

print(" ", end = '')
i = 1
while i < (size-2):
  print("¯", end = '')
  i += 1
