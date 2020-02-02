""""
input = abcdlxyzmno
output =
method =abcdlxyzzmno >> lxyzmno >> lmno >> 0

"""
import logging
logging.basicConfig(filename='logfunc.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('---------Start-----------')

def minus(data, want):
    data = list(set(data) - set(want)) #new data list is produced
    return data

def find(data):
    want = []

    logging.debug('this is data: {}\nwant: {}'.format(data, want))
    
    for i in range(len(data) - 1):
        logging.debug('{} iteration \nvalues of\ndata[i+1] {}\n  data[i] {}'.format(i+1, data[i+1], data[i]))
        
        if data[i+1] - data[i] == 1:

            logging.debug('want b4 append {}'.format(want))
            
            if data[i] not in want:
                want.append(data[i])
            if data[i+1] not in want:
                want.append(data[i+1])

            logging.debug('want after append {}'.format(want))
        else:
            #no consecative term hence breaking loop
            return want

str = list('abcdlxyzmno')
data = [ord(x) for x in str]

while True:
    want = find(data) #this will give consecative number ka list
    if len(want) > 0:#if want is not empty will reduce data
        data = minus(data, want) #data list gets reduced by minus the want list
        
        logging.debug('modified data : {}'.format(data))
    else:
        break #when we can improve

ch = [chr(x) for x in data] #conversion to character again

op = ('').join(ch) #making it strin

print(op)
logging.debug('---------Finish-----------')
