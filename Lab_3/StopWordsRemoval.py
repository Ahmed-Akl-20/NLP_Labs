#الكود ده بيقسم الجملة سواء عربي او انجليزى لكلمات علشان يشيل منها كلمات التوقف

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer

# تحميل الموارد المطلوبة
nltk.download('stopwords')
nltk.download('punkt')

# كلمات التوقف لكل لغة
arabic_stopwords = set(stopwords.words("arabic"))
english_stopwords = set(stopwords.words("english"))

# النصوص
arabic_text = "خرج محمد الى المدرسة على دراجته هذا اول يوم له في المدرسة"
english_text = "John went to school on his bike this was his first day at school"

# إنشاء Tokenizer
tokenizer = WordPunctTokenizer()

# تقسيم النصوص وحذف كلمات التوقف
arabic_filtered = " ".join([word for word in tokenizer.tokenize(arabic_text) if word not in arabic_stopwords])
english_filtered = " ".join([word for word in tokenizer.tokenize(english_text) if word.lower() not in english_stopwords])

# طباعة النتائج
print("Arabic filtered:", arabic_filtered)
print("English filtered:", english_filtered)
