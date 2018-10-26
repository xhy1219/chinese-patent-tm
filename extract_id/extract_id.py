import re
#open file
with open('breastcancer_gene_biomarker.txt','r',encoding='utf-8') as raw: 
    text = raw.read()
#find ids 
idlist=[]
reObj = re.compile('(?<=\W)CN+\d+\w')
idlist = reObj.findall(text)
#write ids in a new file 
fileObject = open('chinese_patents_id.txt', 'w')
for element in idlist:
	fileObject.write(element)
	fileObject.write('\n')
fileObject.close()
