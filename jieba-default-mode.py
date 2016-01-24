#-*- coding: UTF-8 -*- 
import jieba
import jieba.analyse
import sys
import string
fr = open('./list','r')
#f = open('howhow', 'w') 
feature =  open('howhow_feature', 'w') 
list = []
all_list = set()
while True:
    line = fr.readline()
    line = line.strip('\n')
    if (line.strip() == ''): 
        break
    QQ = './dataset/'+ str(line)
    ffile = open(QQ ,'r')
    s = ffile.readline()
    list.append(s)
    ffile.close()
i = 0
count = 10;

for i in range(len(list)):
    #print "Input：", list[i]
    words = jieba.cut(list[i], cut_all=False)
    w_length =  len(str(list[i]))
    test = w_length/1000
    if ( test < 1 ):
        count  = 10;
    else:
        count = count * test
    words = jieba.analyse.extract_tags(list[i], count)
    for word in words:
        all_list.add(word.encode('utf8'))
	#print word
        #f.write(word.encode('utf8'))
        #f.write(' ')
    #f.write('\n')
list_all = []
for i in range(len(all_list)):
    s = str(all_list.pop()) + str(' ')
    list_all.append(s)
    feature.write(s)
    feature.write('\n')
    #sys.stdout.write(s)

#print len(list_all)

#array = []
#for i in range(0,len(list_all)):
#    array.append(0)
#print len(array)

#QAQ = []
#for i in range(len(list)):
#    words = jieba.cut(list[i], cut_all=False)
#    w_length =  len(str(list[i]))
#    test = w_length/1000
#    if ( test < 1 ):
#        count  = 10;
#    else:
#        count = count * test
#    words = jieba.analyse.extract_tags(list[i], count)
#    for word in words:
#        QAQ.append(word.encode('utf8'))
#    for j in range(0,len(QAQ)):
#        for k in range(0,len(list_all)):
#            if(string.find(QAQ[j],list_all[k]) != -1 ):
#                array[j] += 1
#    print i 
fr.close()

