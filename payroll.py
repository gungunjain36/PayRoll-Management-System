import mysql.connector
db=mysql.connector.connect(host='localhost',
                           user='root',
                           password='*******',
                           database="PAYROLLMS")
CURSOR=db.cursor()

def Information_Entry():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t||..ENTER EMPLOYEE DETAILS TO REGISTER..||")
    print("\t\t\t\t***************************************************")
    print()
    i=input("\t\t\t\t ENTER EMPLOYEE ID (max. 5 chars.) : ")
    n=input("\t\t\t\t ENTER EMPLOYEE NAME : ")
    dB=input("\t\t\t\t ENTER DATE OF BIRTH( YYYY-MM-DD ) : ")
    j=input("\t\t\t\t ENTER DATE OF JOINING( YYYY-MM-DD ) : ")
    a=input("\t\t\t\t ENTER ADDRESS : ")
    c=input("\t\t\t\t ENTER CITY : ")
    d=input("\t\t\t\t ENTER DEPARTMENT : ")
    D=input("\t\t\t\t ENTER DEPARTMENT ID : ")
    p=input("\t\t\t\t ENTER PHONE NO. : ")
    while len(p)!=10:
        print("\t\t\t\tPLEASE ENTER VALID PHONE NO. !!")
        p=input("\t\t\t\t ENTER PHONE NO. : ")
        
    ad=input("\t\t\t\t ENTER AADHAR NO. : ")
    while len(ad)!=12:
         print("\t\t\t\tPLEASE ENTER VALID AADHAR NO. !!")
         ad=input("\t\t\t\t ENTER AADHAR NO. : ")
    t1=(i,d,D)
    t=(i,n,dB,j,a,c,p,ad)
    sql="INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
    sql1="INSERT INTO department VALUES(%s,%s,%s);"
    CURSOR.execute(sql1,t1)
    CURSOR.execute(sql,t)
    db.commit()
    print()
    print("\t\t\t\t DATA ENTERED SUCCESSFULLY ")
    print()
    print("\t\t\t\t***************************************************")
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()



def  Employee_Details():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t SEARCH FOR AN EMPLOYEE USING ID")
    print("\t\t\t\t***************************************************")
    print()
    
    sq="select * from employee where  emp_id = %s;" 
    e=input("\t\t\t\tENTER EMPLOYEE ID : ")
    t=(e,)
    CURSOR.execute(sq,t)
    record=CURSOR.fetchall()
    if record==[]:
        print("\t\t\t\tSORRY !! NO SUCH EMPLOYEE EXITS")
    for i in record:
        print()
        print("\t\t\t\tEMPLOYEE ID ::                          ", i[0])
        print("\t\t\t\tEMPLOYEE NAME ::                    ", i[1])
        print("\t\t\t\tEMPLOYEE DATE OF BIRTH ::     ", i[2])
        print("\t\t\t\tEMPLOYEE DATE OF JOINING :: ", i[3])
        print("\t\t\t\tEMPLOYEE ADDRESS ::             ", i[4])
        print("\t\t\t\tEMPLOYEE CITY ::                      ", i[5])
        print("\t\t\t\tEMPLOYEE MOBILE NO. ::          ", i[6])
        print("\t\t\t\tEMPLOYEE AADHAR NO. ::         ", i[7])
    print()
    print("\t\t\t\t***************************************************")
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()




def Remove_employee():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t DELETE AN EMPLOYEE USING ID")
    print("\t\t\t\t***************************************************")
    print()
    e=input("\t\t\t\t ENTER EMPLOYEE ID WHOSE RECORD IS TO BE  DELETED : ")
    t=(e,)
    sqpi="select*from employee where emp_id=%s"
    CURSOR.execute(sqpi,t)
    record=CURSOR.fetchall()
    if record==[]:
        print()
        print("\t\t\t\t SORRY! NO SUCH RECORD EXISTS !!")
    else:
        sq="delete from employee where  emp_id = %s;"
        sq1="delete from department where  emp_id = %s;"
        sqd="delete from salary where  emp_id = %s;"
        sql="delete from leave_record where  emp_id = %s;"
        CURSOR.execute(sq,t)
        CURSOR.execute(sq1,t)
        CURSOR.execute(sqd,t)
        CURSOR.execute(sql,t)
        db.commit()
        print()
        print("\t\t\t\tEMPLOYEE DELETED SUCCESSFULLY!!")
        print()
    print("\t\t\t\t***************************************************")
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()


def  Update_record():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t UPDATE EMPLOYEE RECORD")
    print("\t\t\t\t***************************************************")
    print()
    e=input("\t\t\t\t ENTER EMPLOYEE ID WHOSE RECORD IS TO BE UPDATED : ")
    t=(e,)
    sqpi="select*from employee where emp_id=%s"
    CURSOR.execute(sqpi,t)
    record=CURSOR.fetchall()
    if record==[]:
        print()
        print("\t\t\t\t NO SUCH RECORD EXISTS !!")
    
    else:
        sqn="delete from employee where  emp_id = %s;"
        sqm="delete from department where  emp_id = %s;"
    
        CURSOR.execute(sqn,t)
        CURSOR.execute(sqm,t)
        print()
        print("\t\t\t\t ENTER UPDATED DETAILS : ")
        print()
        i=input("\t\t\t\t ENTER EMPLOYEE  ID : ")
        n=input("\t\t\t\t ENTER EMPLOYEE  NAME : ")
        dB=input("\t\t\t\t ENTER  DATE OF BIRTH( YYYY-MM-DD ) : ")
        j=input("\t\t\t\t ENTER DATE OF JOINING( YYYY-MM-DD ) : ")
        a=input("\t\t\t\t ENTER  ADDRESS : ")
        c=input("\t\t\t\t ENTER CITY : ")
        d=input("\t\t\t\t ENTER  DEPARTMENT : ")
        D=input("\t\t\t\t ENTER DEPARTMENT ID : ")
        p=input("\t\t\t\t ENTER PHONE NO. : ")
        while len(p)!=10:
            print("\t\t\t\tPLEASE ENTER VALID PHONE NO. !!")
            p=input("\t\t\t\t ENTER PHONE NO. : ")
        
        ad=input("\t\t\t\t ENTER AADHAR NO. : ")
        while len(ad)!=12:
            print("\t\t\t\tPLEASE ENTER VALID AADHAR NO. !!")
            ad=input("\t\t\t\t ENTER AADHAR NO. : ")
        t1=(e,d,D)
        t=(i,n,dB,j,a,c,p,ad)
        sql="INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
        sql1="INSERT INTO department VALUES(%s,%s,%s);"
        CURSOR.execute(sql1,t1)
        CURSOR.execute(sql,t)
        db.commit()
        print()
        print("\t\t\t\t EMPLOYEE RECORD UPDATED SUCCESSFULLY !! ")
    print()
    print("\t\t\t\t***************************************************")
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()



def Enter_Attendance():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t EMPLOYEE ATTENDANCE ENTRY ")
    print("\t\t\t\t***************************************************")
    print()
    i=input("\t\t\t\t ENTER EMPLOYEE ID (max. 5 chars.) : ")
    n=int(input("\t\t\t\t ENTER TOTAL WORKING DAYS ::   "))
    d=int(input("\t\t\t\t ENTER TOTAL DAYS EMPLOYEE PRESENT ::   "))
    j=(n-d)
    a=int(input("\t\t\t\t ENTER LEAVE DEDUCTIONS: "))
    t=(i,n,d,j,a)
    sql="INSERT INTO leave_record VALUES(%s,%s,%s,%s,%s);"
    CURSOR.execute(sql,t)
    db.commit()
    print()
    print("\t\t\t\t DATA ENTERED SUCCESSFULLY !!")
    print()
    print("\t\t\t\t***************************************************")
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()


def Attendance():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t EMPLOYEE ATTENDANCE REPORT ")
    print("\t\t\t\t***************************************************")
    print()
    e=input("\t\t\t\t ENTER EMPLOYEE ID WHOSE ATTENDANCE REPORT IS TO BE SHOWN : ")
    sq="select * from leave_record where  emp_id = %s;" 
    t=(e,)
    CURSOR.execute(sq,t)
    record=CURSOR.fetchall()
    if record==[]:
        print("\t\t\t\t SORRY! DATA UNAVAILABLE")
    
    for i in record:
        print()
        print("\t\t\t\t EMPLOYEE ID ::                                         ", i[0])
        print("\t\t\t\t TOTAL WORKING DAYS ::                         ", i[1])
        print("\t\t\t\t TOTAL DAYS EMPLOYEE PRESENT ::      ", i[2])
        print("\t\t\t\t TOTAL ABSENT DAYS ::                            ", i[3])
        print("\t\t\t\t EMPLOYEE LEAVE DEDUCTIONS ::              ", i[4])
    print()
    print("\t\t\t\t***************************************************")
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()



def  Enter_salary():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t EMPLOYEE SALARY ENTRY ")
    print("\t\t\t\t***************************************************")
    print()
    i=input("\t\t\t\t ENTER EMPLOYEE ID :: ")
    j=input("\t\t\t\t ENTER DEPARTMENT ID OF THE EMPLOYEE :: ")
    b=int(input("\t\t\t\t ENTER BASIC SALARY OF THE EMPLOYEE :: "))
    da=int(input("\t\t\t\t ENTER DA OF THE EMPLOYEE :: "))
    ta=int(input("\t\t\t\t ENTER TA OF THE EMPLOYEE :: "))
    hra=int(input("\t\t\t\t ENTER HRA OF THE EMPLOYEE :: "))
    ma=int(input("\t\t\t\t ENTER MA OF THE EMPLOYEE :: "))
    bn=int(input("\t\t\t\t ENTER BONUS OF THE EMPLOYEE :: "))
    ld=int(input("\t\t\t\t ENTER LEAVE DEDUCTIONS IF ANY :: "))
    pf=int(input("\t\t\t\t ENTER PF :: "))
    pt=int(input("\t\t\t\t ENTER PT :: "))
    g=(b+da+ta+hra+ma+bn)
    ts=(g-(ld+pf+pt))
    t=(i,j,b,da,ta,hra,ma,bn,ld,pf,pt,g,ts)
    sql="INSERT INTO salary VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    CURSOR.execute(sql,t)
    db.commit()
    print()
    print("\t\t\t\t DATA ENTERED SUCCESSFULLY !!")
    print()
    print("\t\t\t\t***************************************************")
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()
    


def Salary():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t SEARCH FOR SALARY DETAILS OF THE EMPLOYEE USING EMPLOYEE ID  ")
    print("\t\t\t\t***************************************************")
    print()
    e=input("\t\t\t\t ENTER EMPLOYEE ID WHOSE SALARY REPORT IS TO BE SHOWN : ")
    t=(e,)
    sqi="select*from salary where emp_id=%s;"
    
    CURSOR.execute(sqi,t)
    rm=CURSOR.fetchall()
    if rm==[]:
        print()
        print("\t\t\t\t SORRY! DATA UNAVAILABLE")
    
    for i in rm:
        print()
        print("\t\t\t\t EMPLOYEE DEPARTMENT ID ::              ", i[1])
        print("\t\t\t\t BASIC PAY  ::                                           ", i[2])
        print("\t\t\t\t BONUSES  ::                                             ", i[7])
        print("\t\t\t\t LEAVE DEDUCTIONS  ::                           ", i[8])
        print("\t\t\t\t GROSS SALARY::                                     ", i[11])
        print()
        print("\t\t\t\t***************************************************")
        print()
        print("\t\t\t\t NET SALARY :                                           ", i[12])
    print()
    print("\t\t\t\t***************************************************")
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()
    

def update_salary():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t UPDATE SALARY DETAILS OF THE EMPLOYEE USING EMPLOYEE ID  ")
    print("\t\t\t\t***************************************************")
    print()
    e=input("\t\t\t\t ENTER EMPLOYEE ID WHOSE SALARY  IS TO BE UPDATED : ")
    sq="select*from salary where emp_id=%s;"
    t=(e,)
    CURSOR.execute(sq,t)
    m=CURSOR.fetchall()
    if m==[]:
        print()
        print("\t\t\t\tSORRY !! RECORD UNAVAILABLE ")
    else:
        sqn="delete from salary where  emp_id = %s;"
        CURSOR.execute(sqn,t)
        db.commit()
        print()
        print("\t\t\t\t ENTER UPDATED DETAILS : ")
        print()
        j=input("\t\t\t\t ENTER EMPLOYEE  DEPARTMENT ID : ")
        b=int(input("\t\t\t\t ENTER BASIC SALARY OF THE EMPLOYEE :: "))
        da=int(input("\t\t\t\t ENTER DA OF THE EMPLOYEE :: "))
        ta=int(input("\t\t\t\t ENTER TA OF THE EMPLOYEE :: "))
        hra=int(input("\t\t\t\t ENTER HRA OF THE EMPLOYEE :: "))
        ma=int(input("\t\t\t\t ENTER MA OF THE EMPLOYEE :: "))
        bn=int(input("\t\t\t\t ENTER BONUS OF THE EMPLOYEE :: "))
        ld=int(input("\t\t\t\t ENTER LEAVE DEDUCTIONS IF ANY :: "))
        pf=int(input("\t\t\t\t ENTER PF :: "))
        pt=int(input("\t\t\t\t ENTER PT :: "))
        g=(b+da+ta+hra+ma+bn)
        ts=(g-(ld+pf+pt))
        t=(e,j,b,da,ta,hra,ma,bn,ld,pf,pt,g,ts)
        sql="INSERT INTO salary VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        CURSOR.execute(sql,t)
        db.commit()
        print()
        print("\t\t\t\t RECORD UPDATED SUCCESSFULLY !!")
       
  
    print()
    print("\t\t\t\t***************************************************")
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()



def payslip():
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t GENERATE PAYMENT SLIP OF THE EMPLOYEE  ")
    print("\t\t\t\t***************************************************")
    print()
    e=input("\t\t\t\t ENTER EMPLOYEE ID WHOSE PAYMENT SLIP IS TO BE GENERATED : ")
    t=(e,)
    sql="select* from employee where emp_id=%s;"
    CURSOR.execute(sql,t)
    re=CURSOR.fetchall()
    if re==[]:
        print("\t\t\t\t EMPLOYEE NOT FOUND ")

    for i in re:
        print()
        print("\t\t\t\t EMPLOYEE ID                          :: " , i[0])
        print("\t\t\t\t EMPLOYEE NAME                   :: " , i[1])
        print("\t\t\t\t DATE OF JOINING                   :: " , i[3])

    sqr="select* from department where emp_id=%s;"
    CURSOR.execute(sqr,t)
    m=CURSOR.fetchall()
    for i in m:
         print("\t\t\t\t DEPARTMENT                         :: " , i[1])
         print("\t\t\t\t DEPARTMENT ID                    :: " , i[2])
         print()
    sqn="select* from leave_record where emp_id=%s;"
    CURSOR.execute(sqn,t)
    p=CURSOR.fetchall()   
          
    for i in p:
        print("\t\t\t\t TOTAL WORKING DAYS             :: " , i[1])
        print("\t\t\t\t TOTAL ATTENDANCE DAYS      :: " , i[2])
        print("\t\t\t\t TOTAL ABSENT DAYS               ::", i[3])

    sqp="select* from  salary where emp_id=%s;"
    CURSOR.execute(sqp,t)
    z=CURSOR.fetchall()   
          
    for i in z:
        print("\t\t\t\t BASIC PAY                                  :: " , i[2])
        print("\t\t\t\t DA                                               :: " , i[3])
        print("\t\t\t\t TA                                                :: " , i[4])
        print("\t\t\t\t HRA                                             :: " , i[5])
        print("\t\t\t\t MA                                               :: " , i[6])
        print("\t\t\t\t BONUSES                                   :: " , i[7])
        print("\t\t\t\t LEAVE DEDUCTIONS                 :: " , i[8])
        print("\t\t\t\t PF                                                :: " , i[9])
        print("\t\t\t\t PT                                                :: " , i[10])
        print("\t\t\t\t GROSS SALARY                         :: " , i[11])
        print()
        print("\t\t\t\t***************************************************")
        print("\t\t\t\t NET SALARY                          :: " , i[12])    
    print()
    print("\t\t\t\t***************************************************")
    print("\t\t\t\t\t\t THANK YOU !! ")
    print("\t\t\t\t***************************************************")
    print()
    con=input("\t\t\t\t DO YOU WANT TO CONTINUE (Y/N) ?? :  " )
    if con=="Y" or con=="y":
        main()


def main():
    con="y"
    while con=="y" or con=="Y":
        print()
        print()
        print("\t\t\t||-------------------------------------------------------------------------------------------------||")
        print("\t\t\t\t|-------------------PAYROLL MANAGEMENT SYSTEM-------------------|")
        print("\t\t\t||-------------------------------------------------------------------------------------------------||")
        print("\t\t\t\t\t|---------------------TASKS----------------------|")
        print()
        print()
        print("\t\t\t\t\t(1).       ||        REGISTER A NEW EMPLOYEE                                                                                ||")
        print("\t\t\t\t\t(2).      ||        SEARCH FOR AN EMPLOYEE BASIC DETAILS                                                      ||") 
        print("\t\t\t\t\t(3).      ||        REMOVE AN EMPLOYEE                                                                                          ||")  
        print("\t\t\t\t\t(4).      ||        UPDATE EMPLOYEE BASIC INFO                                                                            ||")
        print("\t\t\t\t\t(5).      ||        ENTER ATTENDANCE INFO OF AN EMPLOYEE                                                      ||")
        print("\t\t\t\t\t(6).      ||        SEARCH FOR  ATTENDANCE-LEAVE DETAILS OF AN EMPLOYEE                      ||")
        print("\t\t\t\t\t(7).      ||        ENTER SALARY DETAILS OF AN EMPLOYEE                                                         ||")  
        print("\t\t\t\t\t(8).      ||        SHOW SALARY AND DEDUCTIONS INFO OF AN EMPLOYEE                                ||")  
        print("\t\t\t\t\t(9).      ||        UPDATE SALARY OF AN EMPLOYEE                                                                       ||")
        print("\t\t\t\t\t(10).     ||        DISPLAY PAYMENT SLIP OF AN EMPLOYEE                                                          ||")
        print()
        print("\t\t\t||-------------------------------------------------------------------------------------------------||")
        print("\t\t\t\t\t      ||***************************************************************||")
        con="n"
    
    print()
    print()
  

    e=int(input("\t\t\t\t\t\t ENTER THE TASK NO. TO ACCESS : "))
      
    if e==1:
        Information_Entry()
    elif e==2:
        Employee_Details()
    elif e==3:
        Remove_employee()
    elif e==4:
        Update_record()
    elif e==5:
        Enter_Attendance()
    elif e==6 :
        Attendance()
    elif e==7:
        Enter_salary()
    elif e==8:
        Salary()
    elif e==9:
        update_salary()
    elif e==10:
        payslip()
    else:
        e=input("PLEASE ENTER CORRECT CHOICE  ::  ")
      
main()
