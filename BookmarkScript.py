import re

"""
linksFirefox = re.findall('"((http|ftp)s?://.*(python).*?)"', All_Bookmarks_Firefox)
( - starts a group of characters to match
(http|ftp) - | is an alteration operator, http 'or' ftp. Parenthesees will group characters.
s? - matching optional character, here 's' = hhtps or ftps
:// - will look exactly for '://' alll are NOT metacharacters so will be matched exactly
.* - any character except new line which can be matched zero or more times,
instead of exactly once
(python) - group of characters to match, here 'python'
.*? - any character except new line which can be matched zero or more times,
instead of exactly once, here optional
) - ends a group of characters to match

"""

with open('bookmarksFirefox.html','r', encoding='utf-8') as Source_Bookmark_File_Firefox:
    All_Bookmarks_Firefox = Source_Bookmark_File_Firefox.read()
#Source_Bookmark_File_Firefox.close()

linksFirefox = re.findall('"((http|ftp)s?://.*(python).*?)"', All_Bookmarks_Firefox)

with open('bookmarksChrome.html','r', encoding='utf-8') as Source_Bookmark_File_Chrome:
    All_Bookmarks_Chrome = Source_Bookmark_File_Chrome.read()
#Source_Bookmark_File_Chrome.close()

linksChrome = re.findall('"((http|ftp)s?://.*(python).*?)"', All_Bookmarks_Chrome)

for i in linksFirefox:
    print('<a href="'+i[0]+'">' + str(i[0]) + '</a></br>')
    
print('-------------------')

for ii in linksChrome:
    print('<a href="'+ii[0]+'">' + str(ii[0]) + '</a></br>')