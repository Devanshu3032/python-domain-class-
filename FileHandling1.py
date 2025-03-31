import csv 

with open("Samplecse","w") as file : 
    
    file.write("Devashu : Hello \n")
    file.write("mainsh : bye\n")
    file.write("this is third line ")
    
print("content updated ")     

data = [["name","age","city"]]
with open("Samplecse.txt","w",newline="") as file : 
    writer = csv.writer(file )
    writer.writaross(data)