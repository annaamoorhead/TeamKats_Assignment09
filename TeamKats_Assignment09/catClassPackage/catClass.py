#catClass.py

# Name: Gillian Howard, Anna Moorhead
# Email: howardgy@mail.uc.edu, moorheaa@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/4/2024
# Course/Section: IS 4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: Executing an API call using a URL.

# Brief Description of what this module does: Creates the cat class and defines the functions we
# need to fetch a random cat fact from our API, parse to a json dictionary, and print the random cat fact. 
# Citations:
# Anything else that's relevant:

import requests
import json

class catFactsAPI:
    def __init__(self):
        '''
        Initializes the CatFactsAPI object with the base URL for 
        fetching random cat facts.
        '''
        self.base_url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2'
        
    def fetch_random_cat_fact(self):
        '''
        Fetches a random cat fact from the Cat Facts API.
        @return A random cat fact if available and has the word 'cat' in it, 
        otherwise prints "No random cat fact available"
        '''
        response = requests.get(self.base_url)
        if response.status_code == 200:
            cat_fact = response.json()
            for fact in cat_fact:
                text = fact.get('text', '').lower()
                # Check if the word 'cat' is present in the fact
                if 'cat' in text:
                    return text
                else:
                    return print("No random cat fact available")
                
    def parse_to_json(self):
        '''
        Parses the random cat fact into a JSON dictionary.
        @return A dictionary containing the random cat fact
        '''
        fact = self.fetch_random_cat_fact()
        if fact:
            json_data = {"Here's a random cat fact": fact}
            return json.dumps(json_data)
       
    def print_random_cat_fact(self):
        '''
        Prints the random cat fact in JSON format
        '''
        fact = self.parse_to_json()
        print(fact)
