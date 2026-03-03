
#بيقسم الجملة ل توكنز ودى ابسط حاجه فيها 
#كل كلمة تعتبر توكن وكل قوس سواء فتحه او قفلة توكن بردو وكل علامة ترقيم بردو توكن
import nltk
from nltk.tokenize import WordPunctTokenizer
text="Natural Language Processing (NLP) is nothing !"
tokenizer=WordPunctTokenizer()
tokens = tokenizer.tokenize(text)
print("Word Tokens : ",tokens)
