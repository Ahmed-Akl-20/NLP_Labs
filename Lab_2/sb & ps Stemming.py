
#الكود بيحاول يرجّع الكلمة لصيغة أبسط مش الروت بتاعها بس بيختتصرها وعندنا طريقتين مختلفين
import nltk
from nltk.stem import SnowballStemmer,PorterStemmer
sb=SnowballStemmer("english")    #احدث وادق شوية وبيرجع كلمة اقرب للمعنى 
ps=PorterStemmer()               #اقدم وابسط بس احيانا بيقص الكلمة زيادة عن اللزوم
print(sb.stem("generously"))
print(ps.stem("generously"))