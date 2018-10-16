#write a code to check if a variable starts with specific word
#If it does not starts with specifc word, then find the word that it starts with

words = "my name is balaji"
if words.startswith("my"):
    print "starts with word - my "
else:
    print "starts with word - ", words.split()[0]
