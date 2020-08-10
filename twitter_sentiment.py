from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

text = 'I love my country!!'
# lowercasing and cleaning the input text
text = text.lower()
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

# tokenizing the text using word_tokenize function
text_tokenize = word_tokenize(cleaned_text)
print(text_tokenize)