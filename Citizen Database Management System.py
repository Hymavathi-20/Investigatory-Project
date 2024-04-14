
import mysql.connector as sql
con=sql.connect(host='localhost',password='Hyma@SQL',user='root',database='Citizen_Database')
if con.is_connected():
     print()

c=con.cursor()




# CREATING DATABASE
def create_dbase():
     q='create database Citizen_Database;'
     c.execute(q)
     c.execute('use Citizen_Database;')

# CREATING TABLE
def create_table():
    s='Create table Citizen_data(Unique_ID varchar(20),Name varchar(30),DOB varchar(20),Gender varchar(5),Aadhar_ID varchar(20),Voter_ID varchar(20));'
    c.execute(s)
    print('Table citizen_data created')





#### MAIN MODULUES

# SELECTS ALL CONTENTS FROM THE TABLE
def show():
    q='select * from Citizen_data;'
    c.execute(q)
    res=c.fetchall()
    print('-'*70)
    print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format('Unique_ID','Name','DOB','Gender','Aadhar_ID','Voter_ID'))
    print('-'*70)
    for v in res:
         unid, nm, dob, gen, aid, vid = v
         print ("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(unid, nm, dob, gen, aid, vid))
    print('-'*70)


# INSERT NEW RECORDS IN TABLE
def insert():
    unid=str(input('Enter Unique ID        : '))
    nm=str(input('Enter Name             : '))
    dob=str(input('Enter DOB  (DD/MM/YY)  : '))
    gen=str(input('Enter gender  (M/F)    : '))
    adh=str(input('Enter Aadhar no        : '))
    votid=str(input('Enter Voter ID         : '))
    
    val=[unid,nm,dob,gen,adh,votid]
    query=('insert into Citizen_data values(%s,%s,%s,%s,%s,%s)')
    c.execute(query,val)
    con.commit()


# DELETES A RECORD
def delete():
    a=str(input('Enter the Unique ID of record to be deleted:'))
    b=str(input('Please confirm the Unique ID:'))
    if a==b:
         q=('delete from Citizen_data where Unique_ID= %s')
         c.execute(q,list(a))
         print('Record deleted successfully')
         con.commit()


# SELECTS A SPECIFIC RECORD       
def search():
    print('1:Unique_ID      2:Name')
    print()
    ch=int(input('Enter your choice for search:'))
    
    if ch==1:
        unid=list(input('Enter Unique_ID:'))
        print()
        q='select * from Citizen_data where Unique_ID= %s;'
        c.execute(q,unid)
        res=c.fetchall()
        for i in range(len(res)):
             print(res[i],end='')
        print()

    elif ch==2:
        nm=input('Enter Name to search:')
        print()
        q='select * from Citizen_data where Name= %s'
        c.execute(q,[nm])
        res=c.fetchall()
        for i in range(len(res)):
             print(res[i],end='')
        print()

    else:
        print('Invalid choice.')


# COUNT
def count():
     print('1:Name')
     print('2:DOB')
     print('3:Gender')
     ch=int(input('Enter your choice:'))
     if ch==1:
          q='select Name,count(*) from citizen_data group by Name;'
     elif ch==2:
          q='select DOB,count(*) from citizen_data group by DOB;'
     elif ch==3:
          q='select GENDER,count(*) from citizen_data group by GENDER;'
     else:
          print('Invalid choice')
     c.execute(q)
     res=c.fetchall()
     for i in res:
          print(i,'\n')
     print()


# SELECTS A COULMN DATA
def search_clm():
     print('1:Unique_ID')
     print('2:Name')
     print('3:DOB')
     print('4:Gender')
     print('5:Aadhar ID')
     print('6:Voter ID')
     print()
     ch=int(input('Select the colunm to be searched:'))
     if ch==1:
          q='select unique_id from Citizen_data;'
     elif ch==2:
          q='select NAME from Citizen_data;'
     elif ch==3:
          q='select DOB from Citizen_data;'
     elif ch==4:
          q='select gender from Citizen_data;'
     elif ch==5:
          q='select aadhar_id from Citizen_data;'
     elif ch==6:
          q='select voter_id from Citizen_data;'
     else:
          print('Invalid choice')
     c.execute(q)
     res=c.fetchall()
     for i in res:
          print(i,'\n')


# UPDATING THE DATA IN TABLE
def update():
     unid=str(input('Enter Unique_ID to be updated:'))
     print('1:Name')
     print('2:DOB')
     print('3:Gender')
     print('4:Aadhar ID')
     print('5:Voter ID')
     ch=int(input('Enter column to be updated :'))
     if ch==1:
          nm=str(input('Enter updated name:'))
          q='update Citizen_data set Name= %s where Unique_ID= %s;'
          c.execute(q,[nm,unid])

     elif ch==2:
          dob=str(input('Enter updated DOB:'))
          q='update Citizen_data set DOB= %s where Unique_ID= %s;'
          c.execute(q,[dob,unid])

     elif ch==3:
          gen=str(input('Enter updated Gender:'))
          q='update Citizen_data set Gender= %s where Unique_ID= %s;'
          c.execute(q,[gen,unid])

     elif ch==4:
          adh=str(input('Enter updated Aadhaar NO:'))
          q='update Citizen_data set Aadhar_ID= %s where Unique_ID= %s;'
          c.execute(q,[adh,unid])

     elif ch==5:
          vot=str(input('Enter updated Voter NO:'))
          q='update Citizen_data set Voter_ID= %s where Unique_ID= %s;'
          c.execute(q,[vot,unid])
     else:
          print('Invalid choise')
     con.commit()



# TO STORE DATA IN A VARIABLE
def use_data():
     unid=list(input('Enter Unique_ID:'))
     q='select * from Citizen_data where Unique_ID= %s;'
     c.execute(q,unid)
     res=c.fetchall()
     return res






### HOME PAGE MODULUE

def login():
     print('_'*80)
     print()
     print('WELCOME TO CITIZEN DATA TABLE!!')
          
     while True:
          print('_'*80)
          print()
          print('OPERATIONS:')
          print()
          print('1:Show Citizen details')
          print('2:Add data')
          print('3:Delete data')
          print('4:Update data')
          print('5:Search record')
          print('6:Show column')
          print('7:Count')
          print('8:Use data')
          print('9:FAQ')
          print('10:Exit')
          print()
          print('_'*80)
          print()
          ch=int(input('Please enter your choice of operation:'))
          print()

          if ch==1:
               print('CITIZEN DETAILS:')
               print()
               show()
               
          elif ch==2:
               print('ADDING DATA:')
               print()
               n=int(input('Enter how many records to be added:'))
               no=1
               for i in range(n):
                    print('RECORD NO:',no)
                    print()
                    insert()
                    print()
                    no+=1
               print('New records added:')
               print()
               show()
               
          elif ch==3:
               print('DELETE DATA:')
               print()
               delete()
               show()

          elif ch==4:
               print('UPDATA DATA:')
               print()
               update()
               show()
               print()
               print('Record Updated')
               
          elif ch==5:
               print('SEARCH DATA BY RECORD:')
               print()
               search()

          elif ch==6:
               print('SHOW DATA BY COLUMN:')
               print()
               search_clm()

          elif ch==7:
               print('COUNT:')
               print()
               count()

          elif ch==8:
               use_data()
               
          elif ch==10:
               print('Thanks for your coorporation.')
               print('Have a great day please visit again.')
               break
          else:
               print('Invalid choice please try again.')
               

            
#print('--------------------------------------------------------------------------------')              
#print('************************ CITIZEN DATA MANAGEMENT SYSTEM ************************')
#print('--------------------------------------------------------------------------------')



### MAIN CODE

               
print('-'*80)
print('*'*24,'CITIZEN DATA MANAGEMENT SYSTEM','*'*24)
print('-'*80)
print()
print('WELCOME TO CITIZEN DATABASE!!')
print()
print('TO CONTINUE PLEASE SELECT ONE OPERATION:')
print()
print('1:Login')
print('2:Exit')
print()
ch=int(input('Enter your choice:'))
print()

if ch==1:
     
    print('Please enter Log in details')
    print()
    user_name=str(input('Enter user name:'))
    password=str(input('Enter your password:'))
    if user_name=='1' and password=='123':
        print()
        print('Logged in Successfully')
        login()
    else:
         print('Invalid username or password')


elif ch==2:
     print('Thanks for your coorperation.')
     print('Have a great day please visit again.')

















'''
def show_():
    q='select * from Citizen_data;'
    c.execute(q)
    res=c.fetchall()
    l=[['Unique_ID','Name','DOB','Gender','Aadhar_ID','Voter_ID']]
    l.extend(list(res))
    for i in l:
        print(i,'\n')


def count_():
     s=str(input('Enter column name:'))
     q='select %s,count(*) from citizen_data group by %s;' %(s,s)
     c.execute(q)
     res=c.fetchall()
     for i in res:
          print(i,'\n')

def search_clm_():
     s=input('Enter colunm name:')
     q='select %s from Citizen_data;'
     c.execute(q,[s])
     res=c.fetchall()
     for i in res:
          print(i,'\n')

'''
