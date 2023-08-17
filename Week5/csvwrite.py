import csv
f=open('c:\\sqlite3\\csv\\student.csv','w',newline='')
w=csv.writer(f)
header=['ID','NAME','CITY','CONTACT']
w.writerow(header)
line=[[1,'Heer','Tarsadi',9087658976],[2,'Hanee','Mota',8789765543],[3,'Riya','Sarbhon',9854345654],[4,'Hiyaaa','Surat',9876543234],[5,'Krishna','Navsari',9878987677]]
w.writerows(line)





