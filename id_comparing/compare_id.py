import re
#open file
with open('EPO_CN_XML_list.txt','r',encoding='utf-8') as raw: 
    text = raw.read()
#regular expression for id
idlist=[]
text = re.sub('[.]', '', text)
reObj = re.compile('CN+\d+\w')
idlist = reObj.findall(text)
#write ids in a new file 
fileObject = open('EPO_id.txt', 'w')
for element in idlist:
	fileObject.write(element)
	fileObject.write('\n')
fileObject.close()

#open id files
f = open("EPO_id.txt", "r")
file = open("chinese_patents_id.txt", "r")

#read id in lines
CNKI_id=[]
EPO_id=[] 
for line in f.readlines():                       
    line = line.strip()
    EPO_id.append(line)

for line in file.readlines():                       
    line = line.strip()
    CNKI_id.append(line)

#find intersection id of epo and cnki id
intersection_id = list(set(EPO_id).intersection(set(CNKI_id)))
#find difference id of cnki and intersection id
difference_id = list(set(CNKI_id).difference(set(intersection_id)))

#write difference id in a new file
fileObject = open('difference_id.txt', 'w')
for element in difference_id:
	fileObject.write(element)
	fileObject.write('\n')
fileObject.close()
