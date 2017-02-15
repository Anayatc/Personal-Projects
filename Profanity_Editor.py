import urllib


def read_text():
    quotes = open('/Users/Anayat/Desktop/movie_quotes.txt')
    contents = quotes.read()
    quotes.close()
    check_profanity(contents)


def check_profanity(text_to_check):
    check_text = str('http://www.wdylike.appspot.com/?q=') + str(text_to_check)
    connection = urllib.urlopen(check_text)
    output = connection.read()
    connection.close()
    if 'true' in output:
        print('Profanity Alert!!')
    elif 'false' in output:
        print('This document has no curse words!')
    else:
        print('Could not scan the document properly')

print(read_text())

#   this program checks documents for profanity and will alert the user if they have unitentionally mistyped a word
#   and inadvertently cursed.