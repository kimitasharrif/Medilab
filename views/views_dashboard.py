# import required modules
import pymysql
from flask_restful import*
from flask import*
from functions import*
import pymysql.cursors


# jwt packages
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

# lab sign up resource

class LabSignup(Resource):
    def post(self):
        data = request.json
        lab_name= data["lab_name"]
        email = data["email"]
        phone = data["phone"]
        permit_id = data["permit_id"]
        password =  data["password"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        cursor = connection.cursor()
        # sql = "insert into Laboratories  (Lab_name, email, phone,permit_id, password) values(%s,%s,%s,%s,%s)"
        # data = (lab_name, email, phone,permit_id, password)
        # try:
        #     cursor.execute(sql,data)
        #     connection.commit()
        #     return jsonify({"message":"Lab registration success"})
        # except:
        #     connection.rollback()
        #     return jsonify({"message":"LAB NOT REGISTERED"})


        # check_password validity

        rensponse = passwordvalidity(password)
        if rensponse:
            if check_phone(phone):
                # phone is corrrect
                sql = "insert into Laboratories  (Lab_name, email, phone,permit_id, password) values(%s,%s,%s,%s,%s)"
                data = (lab_name, email, encrypt(phone),permit_id, hash_password(password))
                try:
                    cursor.execute(sql,data)
                    connection.commit()
                    code = gen_random
                    send_sms(phone,'''Thank you for joining Medilab. Your secret No:{}. Do not share.'''.format(code))
                    return jsonify({"message":"Lab registration success"})
                except:
                    connection.rollback()
                    return jsonify({"message":"LAB NOT REGISTERED"})



            else:
                # phone not in correct format
                return jsonify({"message":"Invalid format enter +254..."})



        else:
            return jsonify({"message":"rensponse"})    
        
class LabSignin(Resource):
    def post(self):
        data = request.json
        email = data["email"]
        password = data["password"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')  
        sql = " select* from Laboratories where email=%s"
        cursor =connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, email)
        if cursor.rowcount ==0:
            return jsonify ({"message":"No such email"})
        else:
            labs = cursor.fetchone()
            hashed_password =labs['password']
            is_matchpassword = hash_verify(password,hashed_password)
            if is_matchpassword == True:
                #including jwt
                access_token = create_access_token(identity= labs, fresh= True)
                return jsonify({'access_token': access_token,'labs':labs})
            
                # is_matchpassword == False:
            elif is_matchpassword == False:
                return jsonify({ "message":" LAB LOGIN FAILED" })

            else:

                return jsonify({ "message": "Something went wrong" })
            


# view labs profile using lab_id
class LabProfile(Resource):
    @jwt_required(fresh= True)
    def get(self):
        data = request.json
        lab_id =data["lab_id"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab') 
        cursor =connection.cursor(pymysql.cursors.DictCursor) 
        sql = "select* from Laboratories where lab_id = %s"
        cursor.execute(sql,lab_id)
        connection.commit()
        if cursor.rowcount==0:
            return jsonify({"message":"Lab doesn't exist"})
        else:
            labs = cursor.fetchone()
            return jsonify({"message":labs})

        
class Addlabtests(Resource):
    @jwt_required(fresh= True)
    def post(self):
        data = request.json
        lab_id = data["lab_id"]
        test_name = data["test_name"]
        test_description= data["test_description"]
        test_cost = data["test_cost"]
        test_discount = data["test_discount"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        cursor= connection.cursor()
        # insert into dependants table
        sql="insert into lab_tests (lab_id, test_name, test_description,test_cost, test_discount) values(%s,%s,%s,%s,%s)"
        data = ( lab_id, test_name, test_description,test_cost, test_discount)
        try:
            cursor.execute(sql,data)
            connection.commit()
            return jsonify({"message":"POST SUCCESSIFUL.Lab test saved"})
        except:
            connection.rollback()
            return jsonify({"message":"POST FAILED.Lab test not saved"})
        
class ViewLabtests(Resource):
            @jwt_required(fresh= True)
            def get(self):
                data = request.json
                lab_id = data ["lab_id"]
                connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
                sql = "select* from Lab_tests where lab_id = %s"
                cursor =connection.cursor(pymysql.cursors.DictCursor)
                cursor.execute(sql,lab_id)
                if cursor.rowcount ==0:
                    return jsonify({"message":"No Lab test found"})
                else:
                    lab_tests = cursor.fetchall()
                    return jsonify(lab_tests)

    

class ViewLabBookings(Resource):
    @jwt_required(fresh= True)
    def get(self):
        data = request.json
        lab_id = data["lab_id"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        sql = "select* from booking where lab_id = %s"
        cursor =connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql,lab_id)
        if cursor.rowcount ==0:
            return jsonify({"message":"No Lab Bookings found"})
        else:
           booking = cursor.fetchall()
           # associate member id with the bookings
           # we want to loop all the booking
           for bookings in booking:
               member_id = bookings["member_id"]
               # return jsonify(member_id)
               sql = "select* from booking where member_id =%s"
               cursor = connection.cursor(pymysql.cursors.DictCursor)
               cursor.execute(sql, member_id)
               member = cursor.fetchone()
               # results are attached to booing dictionary under key
               bookings['key' ]= member
            #    return jsonify(member)
           
                

           # date and time was not convertible to json  
           # hence we use json.dumps and json.loads 
           import json
            # we pass our booking to json.dumps 
           bookings =json.dumps(booking, indent=1, sort_keys=True, default=str)         
           return json.loads(bookings)



class AddNurse(Resource):
    @jwt_required(fresh= True)
    def post(self):
        data = request.json
        surname= data["surname"]
        others= data["others"]
        gender= data["gender"]
        phone = data["phone"]
        password = data["password"]
        lab_id = data["lab_id"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        cursor = connection.cursor()
        # instert into database
        sql = "insert into nurses (surname, others, gender, lab_id, phone, password) values(%s, %s, %s, %s, %s, %s)"
        data = (surname, others, gender,  lab_id, encrypt(phone), hash_password(password))
        try:
            cursor.execute(sql, data)
            connection.commit( )
            return jsonify({ "message": "POST SUCCESSFUL. NURSE SAVED" })

        except:
            connection.rollback()
            return jsonify({ "message": "POST FAILED. NURSE NOT SAVED" })
        


class ViewNurse(Resource):
    def get(self):
        data =request.json
        nurse_id = data["nurse_id"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        sql = "select* from nurses where nurse_id = %s"
        cursor =connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql,nurse_id)
        if cursor.rowcount ==0:
            return jsonify({"message":" Nurse Not found"})
        else:
            nurse_id = cursor.fetchone()
            return jsonify(nurse_id)


class TaskAllocation(Resource):
    @jwt_required(fresh= True)
    def post(self):
        data = request.json
        nurse_id = data["nurse_id"]
        invoice_no =data["invoice_no"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        sql = "select* from booking where status ='Pending' "
        cursor = connection.cursor( pymysql.cursors.DictCursor)
        cursor.execute(sql)
        count = cursor.rowcount
        if count ==0:
            return jsonify({"message":"No pending tasks"})
        else:
                 
            sql1 = "insert into nurse_lab_allocations (nurse_id,invoice_no)  values(%s,%s)"
            data = (nurse_id,invoice_no)
            cursor1 = connection.cursor()

            try:
                cursor1.execute(sql1,data)
                connection.commit()
                return jsonify({"message":"Task Allocated"})
            except:
                connection.rollback()
                return jsonify({"message":"Task Allocation Failed"})

        


