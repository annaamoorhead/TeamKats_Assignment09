#main.py

# Name: Sonali Goyal
# Email: goyalsd@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/4/2024
# Course/Section: IS 4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: Executing an API call using a URL.

# Brief Description of what this module does: instantiates the cat class and calls the method
# Citations:
# Anything else that's relevant: Not all facts in the API are related to cats, 
#so when a cat fact is not available it will let us know. 
#You may need to run it multiple times to be able to see our awesome cat fact.



from catClassPackage.catClass import *

if __name__== "__main__":
    cat_api = catFactsAPI() #Instantiate the class
    printRandomCatFacts = cat_api.print_random_cat_fact()  # Invoke the method
    