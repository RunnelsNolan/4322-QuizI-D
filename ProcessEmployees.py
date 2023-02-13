'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

RAISE_RATE = .1
#open the file
infile = open('employee_data.csv', 'r')
reader = csv.reader(infile, delimiter = ',')
next(reader)


#create an empty dictionary
new_salary_dict = {}

#use a loop to iterate through the csv file
for row in reader:
    full_name = row[1] + ' ' + row[2]
    salary = float(row[5])
    department = row[3]
    title = row[4]
    #check if the employee fits the search criteria
    if department == 'Marketing' and title == 'CSR':
        print('Manager Name: ', full_name, ' Current Salary: $', format(salary, ',.2f'), sep = '')
        new_salary = salary + (salary * RAISE_RATE)
        new_salary_dict[full_name] = new_salary

    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for person in new_salary_dict:
    full_name = person
    final_salary = float(new_salary_dict[person])
    print('Manager Name: ', full_name, ' New Salary: $', format(final_salary, ',.2f'))

infile.close()


   



          
        

        
    
