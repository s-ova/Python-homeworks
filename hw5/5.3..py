import string
user_input = input("Enter a string to convert into a hashtag: ")
cleaned_words = ''.join(c for c in user_input if c not in string.punctuation).split()
hashtag = "#" + ''.join(word.capitalize() for word in cleaned_words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print("Generated Hashtag:", hashtag)
