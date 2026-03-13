#وظيفة الكود انه بيجيب قايمة كلمات التوقف في اللغة العربية ويطبعها بنشيلها لانها عادة مبتضفش معنى للكلام 

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')         # السطر ده علشان يحملى قايمة الكلمات بدل ما احملها من التيرمينال 
stopword_list = stopwords.words("arabic")
print(stopword_list)
