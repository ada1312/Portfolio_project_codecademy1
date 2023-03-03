#Packages 
import csv
import pandas as pd
import numpy

#Import file 
df = pd.read_csv(r'C:\Users\ajdic\Desktop\Portfolio 1\insurance.csv')
print(df)

# initialize empty lists for each column
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

#adding each in a list/ storing into lists
age = df['age'].tolist()
sex = df['sex'].tolist()
bmi =  df['bmi'].tolist()
children = df['children'].tolist()
smoker = df['smoker'].tolist()
region = df['region'].tolist()
charges = df['charges'].tolist()


#average age of patients with numpy
average_age = numpy.average(age)
average_age = round(average_age, 2)
print("Average age of a patient is: " + str(average_age) + " years.")

#Where does individuals comes from 
def individuals_from(a):
    location = {}
    for j in a:
        if j in location:
            location[j] += 1
        else:
            location[j] = 1
    return location

num_location = individuals_from(region)
print(num_location)


#How many smokers are in insurance base 
def smoker_status(smoker):
    status = {}
    for i in smoker:
        if i in status:
            status[i] += 1
        else:
            status[i] = 1
    return status

print(smoker_status(smoker))


#average age of the parent
#combining two lists 
age_children = list(zip(age, children))

#in dictionary
parent_age = {}

for item in age_children:
    parent_age[item[0]] = item[1]

#print(parent_age)


# Get a list of tuples containing the age and number of kids for each person in the dictionary
ages_with_kids = [age for age, num_kids in age_children if num_kids > 0]

if len(ages_with_kids) > 0:
    # Calculate the average age of people with kids
    avg_age_with_kids = sum(ages_with_kids) / len(ages_with_kids)
    avg_age_with_kids = round(avg_age_with_kids, 2)
    print("The average age of people with kids in insurance list is: " + str(avg_age_with_kids))
else:
    print("No person in the list has kids")


