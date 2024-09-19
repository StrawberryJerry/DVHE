import json
import random

fc=open('dataset/CHTD/CHTD-onto/onto_all.json','w',encoding='utf8')
fcrel=open('dataset/CHTD/CHTD-onto/onto_relations.txt','w',encoding='utf8')
fcent=open('dataset/CHTD/CHTD-onto/onto_entities.txt','w',encoding='utf8')
fs=open('dataset/CHTD/CHTD-cross/cross_all.json','w',encoding='utf8')
fe=open('dataset/CHTD/CHTD-ins/ins_all.json','w',encoding='utf8')
ferel=open('dataset/CHTD/CHTD-ins/ins_relations.txt','w',encoding='utf8')
feent=open('dataset/CHTD/CHTD-ins/ins_entities.txt','w',encoding='utf8')
fd=open('dataset/CHTD/CHTD-ins/drug_list.txt','w',encoding='utf8')

with open('dataset/CHTD/list_data.json','r',encoding='utf8') as f:
    json_data=json.load(f)
    D=json_data['药品化学名']
    D.extend(json_data['药品类别'])
    D.extend(json_data['药品类型'])

with open('dataset/CHTD/data.json','r',encoding='utf8') as f:
    json_data=json.load(f)
    E=json_data['logic_entity']
    random.shuffle(E)
    C=json_data['logic_concept']
    C.extend(json_data['subclass'])
    random.shuffle(C)
    S=json_data['instance']
    random.shuffle(S)

onto_rel=[]
onto_ent=[]
for item in C:
    fc.write(json.dumps(item).encode('utf-8').decode('unicode_escape')+'\n')
    if item['subject'] not in onto_ent:
        onto_ent.append(item['subject'])
    if item['relation'] not in onto_rel:
        onto_rel.append(item['relation'])
    if item['object'] not in onto_ent:
        onto_ent.append(item['object'])
    for key in item.keys():
        if key!='N' and key!='subject' and key!='relation' and key!='object':
            if key not in onto_rel:
                onto_rel.append(key)
            for v in item[key]:
                if v not in onto_ent:
                    onto_ent.append(v)
for rel in onto_rel:
    fcrel.write(rel+'\n')
for ent in onto_ent:
    fcent.write(ent+'\n')
DS=[]
D3=[]
for item in S:
    #fs.write(json.dumps(item).encode('utf-8').decode('unicode_escape')+'\n')
    if item['object'] not in DS:
        DS.append(item['object'])
    if item['subject'] not in D3:
        D3.append(item['subject'])

ins_rel=[]
ins_ent=['病人']
DE=[]
for item in E:
    item['subject']='病人'
    if item['relation'] not in ins_rel:
        ins_rel.append(item['relation'])
    if item['object'] not in ins_ent:
        ins_ent.append(item['object'])
    if item['object'] not in DE:
        DE.append(item['object'])
    for key in item.keys():
        if key!='N' and key!='subject' and key!='relation' and key!='object':
            if key not in ins_rel:
                ins_rel.append(key)
            if type(item[key])!=list:
                item[key]=[item[key]]
            for v in item[key]:
                if v not in ins_ent:
                    ins_ent.append(v)
    fe.write(json.dumps(item).encode('utf-8').decode('unicode_escape')+'\n')   


D1=list(set(D)-set(ins_ent)-set(DS))
ins_ent.extend(D1)
ins_ent=list(set(ins_ent))

for item in D1:
    obj=dict()
    obj['N']=2
    obj['subject']=item
    obj['relation']="instance_of"
    obj['object']=item
    S.append(obj)

random.shuffle(S)
for item in S:
    fs.write(json.dumps(item).encode('utf-8').decode('unicode_escape')+'\n')

D2=list(set(D)-set(DS))
D4=list(set(D2)|set(DE))
D4=list(set(ins_ent)&set(D4))

             
for rel in ins_rel:
    ferel.write(rel+'\n')
for ent in ins_ent:
    feent.write(ent+'\n')   

for item in D4:
    fd.write(item+'\n') 




print('done')
