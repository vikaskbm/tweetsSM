import json
import string
from collections import Counter
import matplotlib.pyplot as plt


# getting test input
text = input("ENter data: ")

# convert the input text as lowercase
text_lower = text.lower()
# print(text_lower)

# remove punctuations from input string
cleaned_text = text_lower.translate(str.maketrans('', '', string.punctuation))
# print(cleaned_text)

# tokenizing the words
tokenized_text = cleaned_text.split()
# print(tokenized_text)

# defining the stop words, ie the words that add any meaning to the sentence
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


# removing stop words from input string
final_text = []

for i in tokenized_text:
    if i not in stop_words:
        final_text.append(i)

# print(final_text)

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

# print(emotion_list)

# counting occurance of all the emotions in the input
emotion_count = Counter(emotion_list)
# print(emotion_count)


# plotting data on a graph
fig, ax1 = plt.subplots()
ax1.bar(emotion_count.keys(), emotion_count.values())
# fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()