# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist ")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I made up")

height = float(input("Height: "))
weight = float(input("Weight: "))

bmi = weight / height ** 2

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
print(bmi)



# KeyError
# a_diction = {"key":"value"}
# value = a_diction["non_existen_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# Type error
# text = "abc"
# print(text + 5)
