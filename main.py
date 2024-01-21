# This program is by Yoyo Liu 
# Completed April 2021 
# Uploaded to Github 1/21/2024

import string #import string
sentence = input('Enter a phrase and find out it it is a palindrome: \n')# let user input a sentence

after_taken_out_space = sentence.translate({ord(c): None for c in string.whitespace})#take spaces out of the string

after_taken_out_punctuation = after_taken_out_space.translate(str.maketrans('', '', string.punctuation))

after_lowercased = after_taken_out_punctuation.lower()

after_transform = after_lowercased [::-1] #transform the input so it is backward

if after_transform == after_lowercased:
  print("This is a palindrome")
else:
  print("This is not a palindrome")
print ("Thank you for using this program! Run again if you want to test another phrase! Bye bye!")

''' 
Reference: https://careerkarma.com/blog/python-remove-punctuation/#:~:text=There%20are%20numerous%20ways%20to,filter%20out%20from%20a%20string. (remove punctuation)

https://www.journaldev.com/23763/python-remove-spaces-from-string (remove space)

'''