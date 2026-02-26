
#بنحول اى كلمة للمصدر بتاعها
import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("Teaching"))
print(stemmer.stem("Learned"))