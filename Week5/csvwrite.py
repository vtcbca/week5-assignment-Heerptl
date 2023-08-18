import csv
f=open('c:\\sqlite\\sqlite3\\csv\\student4.csv','w',newline='')
w=csv.writer(f)
# WRITE A HEADER ROW
header=['ID','NAME','CITY','CONTACT']
w.writerow(header)
# WRITE 5 RECORDS DIRECTLY
line=[[1,'Heer','Tarsadi',9087658976],[2,'Hanee','Mota',8789765543],[3,'Riya','Sarbhon',9854345654],[4,'Hiyaaa','Surat',9876543234],[5,'Krishna','Navsari',9878987677]]
w.writerows(line)
# GET 5 USER INPUT
l=[]
for i in range(5):
    sid=int(input("Enter Id:"))
    sname=input("Enter Name:")
    city=input("Enter City:")
    no=int(input("Enter Contact No:"))
    s=[sid,sname,city,no]
    l.append(s)
line.extend(l)
f.close()
with open('c:\\sqlite\\sqlite3\\csv\\student4.csv','w',newline="") as f:
    w=csv.writer(f)
    w.writerow(header)
    w.writerows(line)
f.close()
with open('c:\\sqlite\\sqlite3\\csv\\student4.csv', 'r',errors='ignore') as f:
    r = csv.reader(f)
    for row in r:
        print(row)
f.close()
