with open("testdavidi.txt", "a") as file :
    file.write("01234567890123456789")
    k = file.read

with open("testdavidi.txt","r+") as file :
    file.seek(4)
    file.write("da li brise")

with open("fighters.csv") as file:
    data = file.read()

# Using reader
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) #To skip the headers
    for fighter in csv_reader:
        # Each row is a list
        # Use index to access data
        print(f"{fighter[0]} is from {fighter[1]}") 

# Example where data is cast into a list
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

#Reading/Parsing CSV Using a DictReader:
from csv import DictReader, DictWriter
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name']) #Use keys to access data
        
        
# Version using DictWriter
with open("cats.csv", "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})



import pickle

with open("newpickle.pickle", "wb") as f:
    text = "jimi car!"
    pickle.dump(text, f)

with open("newpickle.pickle", "rb") as f:
    text = pickle.load(f)
    print(text)
    

    
