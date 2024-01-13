import mysql.connector
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1Q@z0plm",
    database="library"
)
mycursor=mydb.cursor()
print("Connection Established")

def main():
    
    def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code!=200:
            return None
        return r.json()
    
    option=st.sidebar.selectbox("Are you?",("Choose","Librarian","Patron"))
    if option=="Choose":
        st.title('Library Management System')
        st.subheader('by')
        st.write('Prajwal V Shenoy - PES2UG21CS383')
        st.write('Prerana M - PES2UG21CS398')
        st.markdown('---')

        lottie_coding = load_lottieurl("https://lottie.host/eca2c44a-e9d3-4da8-afa3-521acc2f5bbd/mbNmPybUkI.json")
        st_lottie(lottie_coding, height=500, key="coding")
        
    elif option=="Librarian":      
        st.sidebar.text_input("Enter Username")
        st.sidebar.text_input("Enter Password",type='password')
        user_record =['admin','librariran@1917']
        if st.sidebar.checkbox("login"):
            if user_record is not None :
                st.sidebar.success("Logged in as admin")
                st.subheader("Welcome!")    
                optionlib=st.selectbox("Choose a table?",("Choose","Librarian","Books","Authors","Category","Transactions","Fines","Patron","Supplier","Publisher","Contact"))
                if optionlib=="Librarian":
                    mycursor.execute("select * from librarian_details")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)
                    optionlib1=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optionlib1=="Create":
                        lid=st.text_input("Enter Librarian ID")
                        fname=st.text_input("Enter Fname")
                        lname=st.text_input("Enter Lname")
                        position=st.text_input("Enter Position")                          
                        if st.button("Create"):
                            sql= "insert into librarian_details(id,fname,lname,position) values(%s,%s,%s,%s)"
                            val= (lid,fname,lname,position)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                            
                    elif optionlib1=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        fname=st.text_input("Enter Fname")
                        lname=st.text_input("Enter Lname")
                        position=st.text_input("Enter Position") 
                        if st.button("Update"):
                            sql="update librarian_details set fname=%s,lname=%s,position=%s where id=%s"
                            val=(fname,lname,position,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                    elif optionlib1=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from librarian where id =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")

                elif optionlib=="Books":
                    mycursor.execute("select * from Books")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)
                    optionbook=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optionbook=="Create":
                        location=st.text_input("Enter the location")
                        bid=st.text_input("Enter Book ID")
                        title=st.text_input("Enter Title of the Book")
                        authorid=st.text_input("Enter Author ID of the book")
                        availability=st.text_input("Enter Availability Status")
                        publisherid=st.text_input("Enter Publisher ID of the book")
                        categoryid=st.text_input("Enter Category ID of the book")
                        copies=st.number_input("Enter Number of copies",min_value=0)                          
                        if st.button("Create"):
                            sql= "insert into books(location,book_id,title,author_id,availability_status,publisher_id,category_id,number_of_copies) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            val= (location,bid,title,authorid,availability,publisherid,categoryid,copies)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                            
                    elif optionbook=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        location=st.text_input("Enter the location")
                        title=st.text_input("Enter Title of the Book")
                        authorid=st.text_input("Enter Author ID of the book")
                        availability=st.text_input("Enter Availability Status")
                        publisherid=st.text_input("Enter Publisher ID of the book")
                        categoryid=st.text_input("Enter Category ID of the book")
                        copies=st.number_input("Enter Number of copies",min_value=1)
                        if st.button("Update"):
                            sql="update books set location=%s,title=%s,author_id=%s,availability_status=%s,publisher_id=%s,category_id=%s,number_of_copies=%s where book_id=%s"
                            val= (location,title,authorid,availability,publisherid,categoryid,copies,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                    elif optionbook=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from books where book_id =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")

                elif optionlib=="Authors":
                    mycursor.execute("select * from author")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)
                    optionauthor=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optionauthor=="Create":
                        authorid=st.text_input("Enter author ID")
                        fname=st.text_input("Enter fname")
                        lname=st.text_input("Enter Lname")
                        about=st.text_input("Enter About")
                        published_work=st.text_input("Enter Published work")                    
                        if st.button("Create"):
                            sql= "insert into author(author_id,fname,lname,about,published_work) values(%s,%s,%s,%s,%s)"
                            val= (authorid,fname,lname,about,published_work)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                            
                    elif optionauthor=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        fname=st.text_input("Enter fname")
                        lname=st.text_input("Enter Lname")
                        about=st.text_input("Enter About")
                        published_work=st.text_input("Enter Published work")
                        if st.button("Update"):
                            sql="update author set fname=%s,lname=%s,about=%s,published_work=%s where author_id=%s"
                            val=(fname,lname,about,published_work,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                            
                    elif optionauthor=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from author where author_id =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")
                            
                elif optionlib=="Category":
                    mycursor.execute("select * from category")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)
                    optioncategory=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optioncategory=="Create":
                        categoryid=st.text_input("Enter Category ID")
                        categoryname=st.text_input("Enter Category Name")
                        description=st.text_input("Enter Description")                         
                        if st.button("Create"):
                            sql= "insert into category(category_id,category_name,description) values(%s,%s,%s)"
                            val= (categoryid,categoryname,description)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                            
                    elif optioncategory=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        categoryname=st.text_input("Enter Category Name")
                        description=st.text_input("Enter Description")
                        if st.button("Update"):
                            sql="update category set category_name =%s description=%s where category_id=%s"
                            val=(categoryname,description,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                            
                    elif optioncategory=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from category where category_id =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")
                            
                elif optionlib=="Transactions":
                    mycursor.execute("select * from transactionss")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)
                    optiontransaction=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optiontransaction=="Create":
                        tid=st.text_input("Enter Transaction ID")
                        borrowerid=st.text_input("Enter Borrower ID")
                        bookid=st.text_input("Enter Book ID")
                        duedate=st.text_input("Enter Due Date(yyyy-mm-dd)")
                        returndate=st.text_input("Enter Return Date(yyyy-mm-dd)")                          
                        if st.button("Create"):
                            sql= "insert into transactionss(transaction_id,borrower_id,book_id,due_date,returned_date) values(%s,%s,%s,%s,%s)"
                            val= (tid,borrowerid,bookid,duedate,returndate)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            sql= "UPDATE Books SET number_of_copies = number_of_copies - 1, availability_status = CASE WHEN number_of_copies - 1 = 0 THEN 'Not Available' ELSE availability_status END WHERE book_id =%s"
                            val= (bookid,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                        
                    elif optiontransaction=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        borrowerid=st.text_input("Enter Borrower ID")
                        bookid=st.text_input("Enter Book ID")
                        duedate=st.text_input("Enter Due Date(yyyy-mm-dd)")
                        returndate=st.text_input("Enter Return Date(yyyy-mm-dd)")
                        if st.button("Update"):
                            sql="update transactionss set borrower_id=%s,book_id=%s,due_date=%s,returned_date=%s where transaction_id=%s"
                            val=(borrowerid,bookid,duedate,returndate,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            sql="update fines set returned_date=%s where borrower_id=%s"
                            val=(returndate,borrowerid)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                            
                    elif optiontransaction=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from transactionss where transaction_id =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")
                    
                elif optionlib=="Fines":
                    sql= "UPDATE Fines SET amount = 0.0"
                    mycursor.execute(sql)
                    mydb.commit()
                    sql= "UPDATE Fines SET amount = amount + (DATEDIFF(returned_date, due_date) * 2.00) WHERE returned_date > due_date"
                    mycursor.execute(sql)
                    mydb.commit()
                    mycursor.execute("select * from Fines")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)
                    optionfine=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optionfine=="Create":
                        borrowerid=st.text_input("Enter Borrower ID")
                        amount=st.text_input("Enter Amount")
                        duedate=st.text_input("Enter Due Date(yyyy-mm-dd)")
                        returndate=st.text_input("Enter Return Date(yyyy-mm-dd)")  
                        paiddate=st.text_input("Enter Paid Date(yyyy-mm-dd)")                                                
                        if st.button("Create"):
                            sql= "insert into fines(borrower_id,amount,due_date,returned_date,paid_date) values(%s,%s,%s,%s,%s)"
                            val= (borrowerid,amount,duedate,returndate,paiddate)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                            
                    elif optionfine=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        amount=st.text_input("Enter Amount")
                        duedate=st.text_input("Enter Due Date(yyyy-mm-dd)")
                        returndate=st.text_input("Enter Return Date(yyyy-mm-dd)")  
                        paiddate=st.text_input("Enter Paid Date(yyyy-mm-dd)")
                        if st.button("Update"):
                            sql="update fines set amount =%s,due_date=%s, returned_date=%s,paid_date=%s where borrower_id=%s"
                            val=(amount,duedate,returndate,paiddate,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                            
                    elif optionfine=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from fines where borrower_id =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")
                            
                elif optionlib=="Patron":
                    sql= "UPDATE borrower SET fines = (SELECT CASE WHEN fines.returned_date <= fines.due_date THEN 0 ELSE fines.amount END FROM fines WHERE fines.borrower_id = borrower.borrower_id) WHERE borrower.borrower_id IN ( SELECT fines.borrower_id FROM fines WHERE fines.returned_date IS NULL)"
                    mycursor.execute(sql)
                    mydb.commit()
                    mycursor.execute("select * from borrower")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)                    
                    optionpatron=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optionpatron=="Create":
                        borrowerid=st.text_input("Enter Borrower ID")
                        fname=st.text_input("Enter fname")
                        lname=st.text_input("Enter Lname")
                        amount=st.text_input("Enter Amount")                      
                        if st.button("Create"):
                            sql= "insert into borrower(borrower_id,fname,lname,fines) values(%s,%s,%s,%s)"
                            val= (borrowerid,fname,lname,amount)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                            
                    elif optionpatron=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        fname=st.text_input("Enter fname")
                        lname=st.text_input("Enter Lname")
                        amount=st.text_input("Enter Amount")
                        if st.button("Update"):
                            sql="update borrower set fname=%s,lname=%s,fines=%s where borrower_id=%s"
                            val=(fname,lname,amount,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                            
                    elif optionpatron=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from borrower where borrower_id =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")
                
                elif optionlib=="Supplier":
                    mycursor.execute("select * from supplier")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)
                    optionsupplier=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optionsupplier=="Create":
                        sid=st.text_input("Enter Supplier ID")
                        company=st.text_input("Enter Company Name")
                        fname=st.text_input("Enter fname")
                        lname=st.text_input("Enter Lname")
                        paymentterms=st.text_input("Enter Payment Terms")
                        deliverymethod=st.text_input("Enter Delivery Method")                         
                        if st.button("Create"):
                            sql= "insert into supplier(sid,scompany,fname,lname,payment_terms,delivery_methods) values(%s,%s,%s,%s,%s,%s)"
                            val= (sid,company,fname,lname,paymentterms,deliverymethod)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                            
                    elif optionsupplier=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        company=st.text_input("Enter Company Name")
                        fname=st.text_input("Enter fname")
                        lname=st.text_input("Enter Lname")
                        paymentterms=st.text_input("Enter Payment Terms")
                        deliverymethod=st.text_input("Enter Delivery Method")
                        if st.button("Update"):
                            sql="update supplier set scompany%s,fname%s,lname%s,payment_terms%s,delivery_methods%s where sid=%s"
                            val=(company,fname,lname,paymentterms,deliverymethod,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                            
                    elif optionsupplier=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from supplier where sid =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")
                
                elif optionlib=="Publisher":
                    mycursor.execute("select * from publisher")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)
                    optionpublisher=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optionpublisher=="Create":
                        publisherid=st.text_input("Enter Publisher ID")
                        pname=st.text_input("Enter Publisher Name")
                        publishedwork=st.text_input("Enter Published Work")               
                        if st.button("Create"):
                            sql= "insert into publisher(publisher_id,pname,publishedwork) values(%s,%s,%s)"
                            val= (publisherid,pname,publishedwork)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                            
                    elif optionpublisher=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        pname=st.text_input("Enter Publisher Name")
                        publishedwork=st.text_input("Enter Published Work")
                        if st.button("Update"):
                            sql="update publisher set pname=%s,publishedwork=%s where publisher_id=%s"
                            val=(pname,publishedwork,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                            
                    elif optionpublisher=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from publisher where publisher_id =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")
                
                elif optionlib=="Contact":
                    mycursor.execute("select * from contact")
                    result = mycursor.fetchall()
                    column_names = [col[0] for col in mycursor.description]
                    df = pd.DataFrame(result,columns=column_names)
                    st.dataframe(df)
                    optioncontact=st.selectbox("Want to Create/Edit/Remove a Record?",("Choose","Create","Edit","Remove"))
                    if optioncontact=="Create":
                        contactid=st.text_input("Enter ID of the person")
                        details=st.text_input("Enter Contact details")             
                        if st.button("Create"):
                            sql= "insert into contact(contact_id,contact_details) values(%s,%s)"
                            val= (contactid,details)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Created Successfully!!!")
                            
                    elif optioncontact=="Edit":
                        st.write("Note: Enter the changed value and also the other values like before which arent changed")
                        id=st.text_input("Enter ID where you want to update")
                        details=st.text_input("Enter Contact Detail")
                        if st.button("Update"):
                            sql="update contact set contact_details =%s where contact_id=%s"
                            val=(details,id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Updated Successfully!!!")
                            
                    elif optioncontact=="Remove":
                        st.subheader("Delete a Record")
                        id=st.text_input("Enter ID")
                        if st.button("Delete"):
                            sql="delete from contact where conact_id =%s"
                            val=(id,)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            st.success("Record Deleted Successfully!!!")
            else :
                st.warning("Incorrect Username/Password")
                            
    elif option == 'Patron':
        st.subheader("Welcome, Patron!")
        optionpat=st.selectbox("Which table do you want to choose?",("Choose","Books","Authors","Category"))
        if optionpat=="Books":
            book_name = st.text_input('Enter the name of the book you want to read:')
            mycursor.execute("select * from books where title = %s", (book_name,))
            result = mycursor.fetchall()
            if result is not None:
                for row in result:
                    st.write(row)
            else:
                st.error('Book not found')
            if st.button("Show All Enteries"):
                mycursor.execute("SELECT * FROM books;")
                result = mycursor.fetchall()
                column_names = [col[0] for col in mycursor.description]
                df = pd.DataFrame(result,columns=column_names)
                st.dataframe(df)
        elif optionpat=="Authors":
            auth_name = st.text_input('Enter the name of the author you want to search for:')
            mycursor.execute("select * from author where fname = %s", (auth_name,))
            result = mycursor.fetchall()
            if result is not None:
                for row in result:
                    st.write(row)
            else:
                st.error('Author not found')
            
            if st.button("Show All Enteries"):
                mycursor.execute("SELECT * FROM author")
                result = mycursor.fetchall()
                column_names = [col[0] for col in mycursor.description]
                df = pd.DataFrame(result,columns=column_names)
                st.dataframe(df)
                    
        elif optionpat=="Category":
            category_name = st.text_input('Enter the category:')
            mycursor.execute("select * from books where category_id = %s", (category_name,))
            result = mycursor.fetchall()
            if result is not None:
                for row in result:
                    st.write(row)
            else:
                st.write('Category not found')
            if st.button("Show All Enteries"):
                mycursor.execute("SELECT * FROM category")
                result = mycursor.fetchall()
                column_names = [col[0] for col in mycursor.description]
                df = pd.DataFrame(result,columns=column_names)
                st.dataframe(df)
    
if __name__ == "__main__":
    main()
    