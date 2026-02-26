
#أول حرف لازم يكون حرف كابتل [A-Z]
#بعد اول حرف لازم يجيلي حرف او اكتر سمول [a-z]+
import re
sent = "Ahmed ahmed AHMED Ali ALI Mona mohamed Sara SARA"
words = re.findall(r'\b[A-Z][a-z]+\b', sent)
for word in words:
    print(word)



