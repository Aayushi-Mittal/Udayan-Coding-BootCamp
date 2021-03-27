import sys
import wikipedia
import webbrowser
from colored import fg, bg, attr
ques = input('%sEnter a keyword you want to search: %s' % (fg(85), attr(0)))
BaseURL='http://en.wikipedia.org/w/index.php?title='
wikipedia.set_lang("en")
print(f'\n%s%s {ques} %s' % (fg(226), bg(124), attr(0)))
print(wikipedia.summary(ques, sentences=2))
OpenURL=input('%sDo you want to know more? (yes/no) %s' % (fg(204), attr(0)))
if OpenURL=='yes':
    print('%sRedirecting to%s' % (fg(185), attr(0)), (wikipedia.page(ques)).url)
    webbrowser.open(BaseURL+ques)
else:
    exit(0)
