#While taking Machine learning course on CodeCademy we need to make three portfolio projects.
#This is the first project making simple analyzations from health insurance data.

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


#difference in cost between smokers and non-smokers

smokstat_price = list(zip(charges, smoker))

non_smoker_cost = [cost for cost, smoker_status in smokstat_price if smoker_status == "no" ]
smoker_cost = [cost for cost, smoker_status in smokstat_price if smoker_status == "yes"]

cost_non = round(sum(non_smoker_cost),2)
cost_yes = round(sum(smoker_cost), 2)

cost_dif = sum(smoker_cost) - sum(non_smoker_cost)
cost_dif = round(cost_dif, 2)


avg_non = numpy.average(non_smoker_cost)
avg_non = round(avg_non, 2)
avg_smok = numpy.average(smoker_cost)
avg_smok = round(avg_smok, 2)
how_many_more = round(avg_smok/avg_non, 2)

print("The difference in insurance cost between smokers and non-smokers is: " + str(cost_dif) + " (smokers have lower sum of costs)." + " But we need to remember that in our dataset is around 800 less smokers than non-smokers.")
print("Total insurance cost for all 274 smokers is: " + str(cost_yes) + ".")
print("Total insurance cost for all 1064 non-smokers is: " + str(cost_non) + ".")
print("Average insurance cost for non-smokers is: " + str(avg_non) + ".")
print("Average insurance cost for smokers is: " + str(avg_smok) + ". And this is: " + str(how_many_more) + " higher than for non-smokers.")

#Are smokers havier than non-smokers
smok_bmi = list(zip(bmi, smoker))

non_smoker_bmi = [bmi for bmi, smoker_stat in smok_bmi if smoker_stat == "no"] 
smoker_bmi = [bmi for bmi, smoker_stat in smok_bmi if smoker_stat == "yes"] 

avg_bmi_smoker = numpy.average(non_smoker_bmi)
avg_bmi_smoker = round(avg_bmi_smoker, 2)
avg_bmi_nonsmoker = numpy.average(smoker_bmi)
avg_bmi_nonsmoker = round(avg_bmi_nonsmoker)

print("Non-smokers have average BMI: " + str(avg_bmi_smoker))
print("Smokers have average BMI: " + str(avg_bmi_nonsmoker))

