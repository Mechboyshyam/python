text = '''Hi ! My name is Shyam,
I have started learning Python Programming.
I'm loving to learn'''

for character in text:
    print(character)

print(text)
print("Indexing in array")

name = "Shyam"

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

check = "Shyam Vikas @@@"
print(check[0:5])
print(check[7:12])

nm = "Harry"
print(len(nm))
print(nm[-4:-2])
# for upper case
print(check.upper())
# for lower case
print(check.lower())
# for cutting special character from the line or name
print(check.rstrip("@"))
# To replce the name or any word
print(check.replace("@@@","Heartbeat"))
# to split and make a line or array
print(check.split())

# to capitalize a first character of a line 
# this can convert all the letters in the line into lover case and makes 
# only first letter capital of the line
heading = "hello! please capitalize the first character."
print(heading.capitalize())

# center method
ab = "Welcome Shyam"
print(ab.center(50))

# count method
abc = "Shyam Shyam Shyam Shyam"
print(abc.count("Shyam"))