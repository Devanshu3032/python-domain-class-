# # with open ( "ces.txt","r") as file : 
# #     # content = file.read()
# #     # print(content)
#     for line in file:
#         print(line.split()) 
          
with open("ces.txtn", "a") as file:
    # Write new content to the file
    file.write("\nThis is the new content being added!")

print("Content added successfully!")
    