def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n :
            word_len.append(x)
    return word_len
print("Program memfilter string yang terdiri dari 4 huruf.")
print ("Original string : Pada hari minggu, teknik dan industry belajar di rumah fakultas, UMG")
print()
print ("Kata yang lebih dari 4 huruf, antara lain : ",long_words(4,"Pada hari minggu, teknik dan industry belajar di rumah fakultas, UMG"))


