# HEY :)
# HEYYYY :)
# Reading the whole file into 1 string

import csv


text_file = "textfile.txt"
data_source = "./stock-data./AAPL_data.csv"
output_file = "stockdata.txt"


print("File contents in one string: ")
with open (text_file, "r") as file:
  my_string = file.read()
file.close()
print(my_string)

print("------------------------------------------\n")

# Reading a file into a list of lines
print("Reading line by line into a list: ")
linesArray = []
with open (text_file, "r") as file:
  for line in file:
    linesArray.append(line.strip())
print(linesArray)

print("------------------------------------------\n")

with open (text_file, "r") as file:
    lines = [line.strip() for line in file.readlines()]
print(f'Using readlines: {lines}')    

print("------------------------------------------\n")

# Different way
print("Another way: ")
temp = open(text_file,'r').read().split('\n')
print(temp)

print("------------------------------------------\n")

# Reading csv file
with open (data_source, "r") as file:
    lines = [line.strip().split(",") for line in file.readlines()]
print(f'Using readlines: {lines}') 

# Either read into a collection (line by line) OR split the string by new lines

# Writing a file
with open (output_file, "w") as file:
    writer = csv.writer(file)
    writer.writerow(lines[1])
file.close()


#Date=0
#Open=1
#High=2
#Low=3
#Close=4
#Volume=5
#Name=6

# List of Dictionaries? 

'''
dict = {
   "columns"={
    "Date"=0,
    "Open"=1,
    "High"=2,
    "Low"=3,
    "Close"=4,
    "Volume"=5,
    "Name"=6
  },
  #"APPL"= [{'Date' : '2018-02-07', '163.085', '163.4'', '159.0685', '159.54', '51608580', 'AAPL'}, {}]
  #GOOG"={}
  #
}

# lines[0][Date]

# To check date, i increments from loop: lines[i][0]
'''
