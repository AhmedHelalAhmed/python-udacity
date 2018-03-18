import urllib
def read_text():
    quotes = open("./movie_quotes.txt")
    contents_of_file = quotes.read()
    #print contents_of_file
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    #print output
    connection.close()
    if "true" in output :
        print "Profanity Alert!!"
    elif "false" in output :
        print "This document has no curse words!"
    else:
        print "Could not scan the document properly."

read_text()



#https://docs.python.org/2/library/functions.html#open
#http://www.wdylike.appspot.com/?q=shot
"""
This is a cool api to check the profane words in contents.
It could be used to scan emails, documents and even public comments
"""
#https://en.wikipedia.org/wiki/Query_string
#https://docs.python.org/2/library/urllib.html