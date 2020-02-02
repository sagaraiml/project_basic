# To find number from text 

import re

message = 'hi there i have 5 sim cards , numbers +91-8956231478, +91-8596741236, +91-3261548796' 

#NumberRegex=re.compile(r'\d\d\d\d\d\d\d\d\d\d') #created Regex object and pattern is 8956895689

#NumberRegex=re.compile(r'\+\d\d-\d\d\d\d\d\d\d\d\d\d') #created Regex object and the pattern is +91-8989568989

NumberRegex=re.compile(r'(\+\d\d)-(\d\d\d\d\d\d\d\d\d\d)') #created Regex object and the pattern is (+91)-(8989568989)

mo = NumberRegex.search(message) #creates a match object for Regex object

print(mo.group()) #this group() mrthod will return 1st pattern found in string format

try:
    print('we have country code as : ' + mo.group(1)) #this willl find country code alone

except:
    print('no group in pattern')
    
print(NumberRegex.findall(message)) #findall method of Regex object will return all matched pattern in list format
