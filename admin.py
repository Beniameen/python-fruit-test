# Name:  Margret
# Student Number: 10474901 

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 1, 2019.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to "do nothing".  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.
 
              

# Import the json module to allow us to read and write data in JSON format.
import json

# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.

# Repeatedly prompt for input until an integer is entered.

def inputInt(prompt, errorMessage = 'Invalid input- Try again:'):
    while True:
        value = input(prompt)

        try:
            numResponse = int(value)
        except ValueError:
            print(errorMessage)
            continue
        return numResponse
       



# This function repeatedly prompts for input until a float is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.

#repeatedly re-prompt the user (using the prompt parameter) for input until they enter a float.

def inputFloat(prompt,errorMessage = 'Invalid input- Try again:'):
    while True:
        value = input(prompt)

        try:
            numResponse = float(value)
        except ValueError:
                print(errorMessage)
                continue
            
        return numResponse
    
# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.

# Repeatedly prompt for input until something (not whitespace) is entered.

def inputSomething(prompt,errorMessage = 'Invalid input- Try again:'):
    
     while True:
        value = input(prompt).strip()
        
        if value :
            return value
        else:
            print('input something')


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 4 of the "Functions in admin.py" section of the assignment brief.

# Open "data.txt" in write mode and write the data to it in JSON format.

def saveData(datalist):
        f = open('data.txt', 'w')
        json.dump(datalist, f, indent = 4)
        f.close()
#Set datalist to an empty list

datalist = []
       
# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.


# try to open a file named “data.txt” in read mode, then load the data from the file into a variable named datalist and then close the file. 

try:
    
    f = open('data.txt', 'r')
    datalist = json.load(f)
    f.close()
except:
    print('FileNotFoundError, ValueError')
    
# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Details of admin.py" section of the assignment brief.
# The rest is up to you.

# Print welcome message, then enter the endless loop which prompts the user for a choice.
print('Welcome to the Fruit Test Admin Program.')


while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()
    # prompt them to enter all 5 details of a fruit, beginning with the name.  Place the details into a new dictionary         
    if choice == 'a':
         data = {}
         data ['name'] = (inputSomething('Entre name of fruit:'))
         data [ 'Calories'] = (inputFloat('In 100 grams of '+ data['name']+', how many calories are there?:'))
         data ['Fibre'] = inputFloat('Grams of fibre are there ?: ')
         data ['Sugar'] = inputFloat('Grams of sugar are there ? :')
         data ['Vitamin C'] = inputFloat('Milligrams of Vitamins C are there ?:')
        #Add item to data list and save changes
         datalist.append(data)
         saveData(datalist)
    
   # display the names of all fruit in the data list preceded by their index number, or a “No fruit saved” error message if there is nothing in the list.     
    elif choice == 'l':
        
         if len(datalist)== 0:
             
            print('No fruit saved')
         else:
            print('list of current fruits:')

            for index, da in enumerate (datalist):
                print(' ' +str(index) + ')', da['name'])
         
       
     
    

    elif choice == 's':
       if len(datalist) == 0:
           
            print('No Fruit saved')
       else:
            #Prompt for search term and convert to lowercase
            searchTerm = inputSomething('Entre search term:').lower()
            print('Search results:')
            #Loop through data and print items with search term in name
            for index, data in enumerate (datalist):
                
                if searchTerm in data['name'].lower():
                   print('' ,str( index)+') '+ data['name']) 
                  
               
             
              
                

    elif choice == 'v':
        if len(datalist) == 0:
            print('No Fruit saved')
        else:
            #prompt them for an index number.             
            index = inputInt('Entre fruit index number to veiw: ')
            if index < 0 or index >= len(datalist):
                print('Invalid index number')
            else:
                #print the corresponding fruit’s name and all of its nutritional information. 
        
                data = datalist[index]
                print('Nutritional infromation for 100 grams of', data['name'],':') 
                print('Calories:' , data ['Calories'])
                print('Fibre:' , data ['Fibre'], 'grams')
                print('Sugar:' , data ['Sugar'],'grams')
                print('Vitamin C:' , data ['Vitamin C'],'milligrams')
       

        

    elif choice == 'd':
        if len(datalist) == 0:
            print('No Fruit saved')
        else:
            #prompt them for an index number and then remove the corresponding fruit from the data list
            index = inputInt('Fruit number to delete: ')
            if index < 0 or index >= len(datalist):
                print('Invalid index number')
            else:
                del datalist[index]
                print('Fruit Deleted')
                
                saveData(datalist)
       

        

    elif choice == 'q':
        # print “Goodbye!” and break out of the loop to end the program. 
        print('Goodbye!')
        break
        



    else:
        #If the user enters anything else, print an “Invalid choice” message
        print('Invalid choice')
        
        
