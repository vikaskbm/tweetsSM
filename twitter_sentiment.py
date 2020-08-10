from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

text = 'I love my country!!'
# lowercasing and cleaning the input text
text = text.lower()
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

# tokenizing the text using word_tokenize function
text_tokenize = word_tokenize(text)
print(text_tokenize)


# Removing stop words from our text
final_text = []
for word in text_tokenize:
    if word not in stopwords.words('english'):
        final_text.append(word)