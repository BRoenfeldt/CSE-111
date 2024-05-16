"""Braden Roenfeldt
Brother Keers
12:45
"""

import random

def main():
    #Calls the make_sentence function 6 times
    for i in range(6):
        #Randomly picks a quantity and tense each time it loops to create new sentences
        quantity = random.randint(0,1)
        tense = random.choice(["past", "present", "future"])
        generatedSentence = make_sentence(quantity, tense)
        print(f"{generatedSentence}")
        addToText(generatedSentence)
        

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    #Calls the functions to get the determiner, noun, and verb
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    #Returns the sentence with the determiner, noun, and verb
    sentence = f"{determiner} {noun} {verb} {preposition.lower()}."
    return sentence

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    #List of prepositions
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    #Randomly chooses a preposition
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    #Calls the functions to get the preposition, determiner, and noun
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    #Returns the prepositional phrase with the preposition, determiner, and noun
    phrase = f"{preposition} {determiner} {noun}"
    return phrase

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    #checks quantity; Returns a random determiner based on the quantity
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    word = word.capitalize()
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    #List is created for each quantity
    #Checks the quantity; Returns a random noun based on the quantity
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
        chosen_word = random.choice(words)
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
        chosen_word = random.choice(words)
    return chosen_word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    #List is created for each tense and quantity
    #Checks the tense and quantity; Returns a random verb based on the tense and quantity
    if quantity == 1 and tense == "present":
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        chosen_word = random.choice(words)
    elif quantity != 1 and tense == "present":
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
        chosen_word = random.choice(words)
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
        chosen_word = random.choice(words)
    elif tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
        chosen_word = random.choice(words)
    return chosen_word

def addToText(sentence):
    """
    Writes the generated sentences to a text file named sentences.txt
    Args:
        None

    Returns:
        None
    """
    with open("sentences.txt", "a") as file:
        file.write(f"{sentence}\n")

#Main funtion if statement for importing
if __name__ == "__main__":
    main()