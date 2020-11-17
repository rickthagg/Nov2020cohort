# # 1. Create a dictionary called zodiac with the following inforation.
# # Each key is the name of the zodiac

# zodiac = {

#     'Aries': 'The Warrior', 'Taurus': 'The Builder', 'Gemini': 'The Messenger', 'Cancer': 'The Mother', 'Leo': 'The King', 'Virgo': 'The Analyst', 'Libra': 'The Judge', 'Scorpio': 'The Magician', 'Sagittarius': 'The Gypsy', 'Capricorn': 'The Father', 'Aquarius': 'The Thinker', 'Pisces': 'The Mystic'
# }
# time = zodiac['Taurus']
# print(time)

# # 1a. Retrieve information about your zodiac from the zodiac dictionary
# zodiac = {

#     'Aries': 'The Warrior', 'Taurus': 'The Builder', 'Gemini': 'The Messenger', 'Cancer': 'The Mother', 'Leo': 'The King', 'Virgo': 'The Analyst', 'Libra': 'The Judge', 'Scorpio': 'The Magician', 'Sagittarius': 'The Gypsy', 'Capricorn': 'The Father', 'Aquarius': 'The Thinker', 'Pisces': 'The Mystic'
# }
# time = zodiac['Leo']
# print(time)

# 2. Given the following dictionary

# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }


# phonebook_dict["Kareem"] = "938-489-1234"
# 2a. Print Elizabeth's phone number
# Elizabeth_num = phonebook_dict['Elizabeth']
# print(Elizabeth_num)

# 2b. Add a entry to the dictionary: Kareem's number is 938-489-1234.
# phonebook_dict['Kareem'] = '938-489-1234'
# print(phonebook_dict)

# 2c. Delete Alice's phone entry.
# del phonebook_dict['Alice']
# print(phonebook_dict)
# 2d. Change Bob's phone number to '968-345-2345'.
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)
# 2e. Print all the phone entries.


# 3. Nested dictionaries

# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#         {
#             'name': 'Jasmine',
#             'email': 'jasmine@yahoo.com',
#             'interests': ['photography', 'tennis']
#         },
#         {
#             'name': 'Jan',
#             'email': 'jan@hotmail.com',
#             'interests': ['movies', 'tv']
#         }
#     ]
# }
# 3a. Write a python expression that gets the email address of Ramit.
# ram_email = ramit['email']
# print(ram_email)
# # 3b. Write a python expression that gets the first of Ramit's interests.
# interest_1 = ramit['interests'][0]
# print(interest_1)
# # 3c. Write a python expression that gets the email address of Jasmine.
# jas_email = ramit['friends'][0]['email']
# print(jas_email)
# # 3d. Write a python expression that gets the second of Jan's two interests.
# jan_int = ramit['friends'][1]['interests'][1]
# print(jan_int)

# 4. Letter Summary
# Write a letter_histogram function that takes a word as its input,
# and returns a dictionary containing the tally of how many times
# each letter in the alphabet was used in the word. For example:

# >>>letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}


# def histogram(some_word):
#     count = {}
#     for letter in some_word:
#         if letter not in count:
#             count[letter] = 1
#         else:
#             count[letter] += 1
#     return count


# print(histogram('Timeless'))
# Code above not working (keep going)

# Claude's Answer


# def histogram(word):
#     count = {}
#     for i in word:
#         if i not in count:
#             count[i] = 1
#         else:
#             count[i] += 1
#     return count


# print(histogram("banana"))

# # Zach's Answer


def histogram(string):
    test_dictionary = {}
    for letter in string:
        test_dictionary[letter] = test_dictionary.get(letter, 0) + 1
    return test_dictionary


print(histogram('banana'))


# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to be')

# Hint use the split method
