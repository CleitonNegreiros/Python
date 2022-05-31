# Gradebook

subjects = input('Please insert your subjects, separated by commas: ')
sbjct_splitted = subjects.split(',')
print("So your subjects are: " + str(sbjct_splitted))
grades = []
for index in range(0, len(sbjct_splitted)):
    grades.append(input('Please insert grade for ' + sbjct_splitted[index] + " : "))

print(grades)

gradebook = {}
for index in range(0, len(grades)):
    gradebook[sbjct_splitted[index]] = (grades[index])

print(gradebook)

for key, value in gradebook.items():
    print("Your grade for subject " + key + " is: " + value)