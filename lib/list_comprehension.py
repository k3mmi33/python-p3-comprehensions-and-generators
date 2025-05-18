#!/usr/bin/env python3

def return_evens(num_list):
    # Return a list of even numbers from num_list using a list comprehension
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    # Return a list with an exclamation mark added to each sentence in sentence_list using a list comprehension
    return [sentence + "!" for sentence in sentence_list]
