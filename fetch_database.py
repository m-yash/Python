import pymysql

#create connection
#add your inputs as ("hostname","username","password","database name")
con = pymysql.connect("","","","") 

#create object
cur = con.cursor()

#execute command
#considering id = 1 for example
exe = cur.execute("select firstname, lastname from student where id = 1")

data = cur.fetchall()

#here the output will be in a tuple like ('firstname','lastname')
print(data)  

#use the index method
for i in data:  
    firstname = i[0]
    lastname = i[1]

print(firstname,lastname)
con.commit()
con.close()

