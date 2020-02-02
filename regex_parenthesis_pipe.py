import re

message = '''Hi I am Batman. Lucious designed many thing for me like Batsuit,
Batmobile, Batchopter, Batwheels, Batgun. I am looking for Batgirl now, hehehe'''

batregex = re.compile(r'Bat(man|suit|chopter|wheels|gun)')

mo = batregex.search(message);print(mo.group())

#findall = batregex.findall(message);print(findall)

