#!/usr/bin/env python
import sys
import random
import string
import twitter

api = twitter.Api(consumer_key = '1qwziCIuZeYnDgdUcjJbg', 
                consumer_secret='qIMK2kORwJMLWb9wWGM9PSdvQpMToI5TNAuDQoVw', 
                access_token_key='1554230311-hOTyc8nthz27gDp7bOeDqwNsU9KNxRs1R3afZR4', 
                access_token_secret='JKZxjuRo2PIBkczG68F27do4ERTbQSzFwuJZDrW8')

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of markov chains."""
    # Since we have split every word in the text in indivivual strings
    # Cycle through the individual strings to create tupules as keys in dict
    # Add word that comes after each tupule to list
    # Cycle through text that is split into indivdiual strings to find any duplicate tupules
    # If duplicates are found, populate list with additional words that follow the tupule
    # Convert string of input text into a dictionary

    dict_markov = {}
    # n_gram = input("How many n_grams would you like?")

    for index in range(len(corpus)-2):
        key = (corpus[index], corpus[index + 1])
        value = corpus[index + 2]
        # Set_default returns the value for the key
        # But if there is no key:value pair then puts in keys with [] 
        # Then appends to the list already present or makes a new list
        dict_markov.setdefault(key, []).append(value)
        # dict_markov[key].append(value)
    return dict_markov

def find_random_value(d, dict_key):
    ran_val = random.choice(d[dict_key])
    return ran_val

def combine(string1, string2):
    string3 = string1 + " " + string2
    return string3 

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # Randomly go through through created dictionary
    # Select a key to print - except last key
    key = random.choice(chains.keys())
    final_string = " ".join(key)
    # string.upper(final_string[0])
    # lst = [final_string[0].upper + final_string[1:]]
    # final_string = " ".join(lst)
    # print final_string

    while len(final_string) < 130:
        random_value = find_random_value(chains, key)
        final_string = combine(final_string, random_value)
        
        key = (key[1], random_value)

    return final_string


    # This only works if the tupule has ONLY two elements
    # Need to update with a loop if tupule has > 2 elements
    # tupule_elements = combine(random_key[0],random_key[1]) 
    # Select an element from key's value list to print ie. random_value
    # final_string = combine(tupule_elements,random_value)
    # print tupule_with_value

    # new_random_tuple = (random_key[1], random_value)
    # num_characters = 0
    # for i in range(20):
    # while num_characters + len(val) < 140:

        # if new_random_tuple in chains:
            # val = find_random_value(chains,new_random_tuple)
            # while len(combine(final_string,val)) < 140:
            #     final_string = combine(final_string,val)
            #     new_random_tuple = (new_random_tuple[1], val)
            #     val = find_random_value(chains,new_random_tuple)
            # while i in final_string <=140:
            #     continue
            # else:
            #     break
        # return final_string



    # Jessica = find_random_value(chains, new_random_tupule)
    # print combine(tupule_with_value,Jessica)


    # Find a key that starts with the second element of the current tupule 
    # Print that new tupule  
    # To start make it cycle 5 times

    # Cycle back through
    # Set limit to < 140 characters

def main():
    script = sys.argv
    # filename1, filename2 
    # text1 = open(filename1).read()
    # text2 = open(filename2).read()
    # api2 = twitter.Api()
    text_twitter1 = api.GetUserTimeline(screen_name='@bexcitement')
    # text1 = open(text_twitter1).read()
    tweet_texts = []
    for tweet in text_twitter1:
        tweet_texts.append(tweet.text)

    initial_text = " ".join(tweet_texts)
    input_text = initial_text.split()
    print initial_text
    print input_text

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    status = api.PostUpdate(random_text)
    # print status.text



if __name__ == "__main__":
    main()
