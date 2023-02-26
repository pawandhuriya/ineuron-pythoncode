# dict1={}
# print(type(dict1))
dict2={}
dict2['name']='Pawan'
dict2['age']=22
dict2['skills']=['Python','Java']
dict2['states_visted']=('UP','Goa')
dict2[45]='Random Key'
# we can add some other dict inot exsiting
dict3={'color':'Black','nationality':'Indian'}
dict2['other details']=dict3


# check len 
# print(len(dict2))
#h ow we can update value in a perticular key
print(dict2['skills'][0])


# print dictnry in dictnry
print(dict2['other details']['nationality'])

#total values of dict2
print(list(dict2.values()))

for k,v in dict2.items():
    print('key is =',k, 'and v is value',v)