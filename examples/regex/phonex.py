import re, sys
f = file('./phone_and_emails.txt')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# print re.findall('\d{3}-\d{4}', text)
# print re.findall(phoneRegex, text)
# print re.match(phoneRegex, text).groups()

for line in f.readlines():
    print re.match(phoneRegex, line).group()

f.close()
