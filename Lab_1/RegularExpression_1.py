
#الكلمة لازم تبدأ بحرف او اكتر كابتل [A-Z]+
import re 
sent = "This APPLICATION Is FOR The SESSION That I Did NOT Attend IN The LAB"
words = re.findall(r'\b[A-Z]+\b' ,sent)
for word in words :
    print(word)