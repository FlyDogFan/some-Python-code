import dbhash
db = dbhash.open('dbhashtemp','c')
db['��ʩ'] = '��ʩ�ɴ'
db['����'] = '��������'
db['�Ѿ�'] = '�Ѿ�����'
print "û�н����κβ�����"
for k,v in db.iteritems():
    print k,v
if db.has_key('��ʩ'):
    del db['��ʩ']
print "ɾ����ʩ��Ӧ�����ݣ�"
for k,v in db.iteritems():
    print k,v  
db.close()
    
