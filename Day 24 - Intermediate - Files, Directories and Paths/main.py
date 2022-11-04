# reading files 

with open("../../../../my_file.txt") as file:
    content = file.read()
    print(content)

# # write to files
# with open("/users/amanor/Desktop/my_file.txt", mode='w') as file:
#     file.write("My name is Enoch Tetteh Amanor \nI'm 24 years old \nI live at Weija")