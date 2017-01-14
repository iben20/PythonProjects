#Create a function that takes in a parameter and can sort it
#Need a global variable of an array to store all of the information

string_library = []
numbers_library = [1,2,3,4,5,7,8,9]

def sorting_function(user_input):
    #check to see if what the user input is a number or a string
    if type(user_input) == int or type(user_input) == float:
        print "You have inputted the number %s." %(user_input)
        if len(numbers_library) == 0:
            numbers_library.append(user_input) #add the input to the library
        
        #need to do binary search
        i = True
        high = len(numbers_library)-1 #end
        low = 0 #start
        while i:
            #Check to see if the length of the divided array is 1
            #This means we've found the place to insert the number
            #divide the array into two and find middle point
            middle = (high + low)/2
            if abs(high-low) == 1:
                numbers_library.insert(high,user_input)
                i = False
            #compare middle point with what the user inputted
            if user_input > numbers_library[middle]:
                #the middle point now becomes the start point
                low = middle + 1
            
            elif user_input < numbers_library[middle]:
                #the middle point now becomes the end point 
                high = middle
        
    elif type(user_input) == str:
        print "You have inputted the string '%s'." %(user_input)
        string_library.append(user_input) #add the input to the library
        
        #sorting the library
        
    else:
        print "Sorry, try again."
  
sorting_function(6)
print numbers_library    