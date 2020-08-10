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

# NLP emotion algorithm.
with open('emotion.json', encoding='UTF-8') as file:
    emotions = json.load(file)

emotion_list = []
for word in final_text:
    if word in emotions:
        if isinstance(emotions[word], (list)):
            emotion_list.extend(emotions[word])
        else:
            emotion_list.append(emotions[word])

# count occurance of all the emotions in the input
emotion_count = Counter(emotion_list)
print(emotion_count)


# plotting data on a graph
fig, ax1 = plt.subplots()
ax1.bar(emotion_count.keys(), emotion_count.values())
fig.autofmt_xdate()
plt.show()