
#الكود ده بيعمل تبسيط للكلمة (prefix + root + suffix)

def returnRoot (word):
    start=["re","un","in"]
    end=["ing","ness","en"]
    for s in start:
        if word.startswith(s):
            root = word[len(s):]
            for e in end :
                if root.endswith(e):
                    return(s,root[:-len(e)],e)    #انا اسف بس دى سهت على حضرتك 
    return(word)
print(returnRoot("unhappiness"))            