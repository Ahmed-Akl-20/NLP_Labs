import hfst
fst = hfst.HfstInputStream("arabic.hfstol").read()
words = ["تكتب" ,"بكتب","المدرسة","كتاب","كتب"]
for w in words:
    result = fst.lookup(w)
    print(w,result)



    