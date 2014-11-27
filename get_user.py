# -*- coding: utf-8 -*-
def get_user_list(filename):
	fr=open('static/manage_upload/%s.txt'%(filename))
	
	user_list=[]

	for line in fr.readlines():
	 try:
		user_list.append(line.strip().split(' ')[2])
		#print line.strip().split(' ')[2]
	 except:
		pass
	user_list=list(set(user_list))
	fr.close()
	return user_list

def get_talktive(filename):
    user_list=get_user_list(filename)
    fr=open('static/manage_upload/%s.txt'%(filename))
    talk_dic={}
    for i in user_list:
       talk_dic[i]=0
	
    for line in fr.readlines():
	 try:
		
		talk_dic[line.strip().split(' ')[2]]+=1
	 except:
		pass

    return talk_dic

def sortDic(Dict):
   	return sorted(Dict.items(),key=lambda e:e[1],reverse=True)  

def write_talktive(user_list_sort,filename):
   #fr1=open('/Users/hakuri/Desktop/wechart_manage_sort.txt','a')
   fr1=open('static/result/%s.txt'%(filename),'w')
   dic={}
   num=1
   for i in user_list_sort:
       try:	
       	
        fr1.write('第%d名:'%(num)+str(i[0])+'        '+str(i[1])+'\n')	
        num+=1 
       except:
       	pass
    
def put_out(filename): 
    write_talktive(sortDic(get_talktive(filename)),filename) 
    
#put_out('wechart')
