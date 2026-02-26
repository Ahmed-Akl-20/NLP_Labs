
#الكلمة لازم تبدأ بحرف او اكتر كابتل [A-Z]+
#بعد كدا ممكن يجيلي حروف كابتل او ارقام مش هتفرق المهم ان الكلمة تبدأ بحرف كابتل (?:[A-Z]|[0-9])*
import re 
sent = "AHMED ahmed AHMED55 55AHMED AhMED aHmed  "
words = re.findall(r'\b[A-Z]+(?:[A-Z]|[0-9])*\b' ,sent)
for word in words :
    print(word)