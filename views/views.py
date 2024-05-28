import pymysql
from flask_restful import Resource
from flask import *
from functions import *

# Add a member class
# member_signup and member_signin
class MemberSignup(Resource):
    def post(self):
        # get data from client
        data = request.json
        surname= data["surname"]
        others= data["others"]
        gender= data["gender"]
        email= data["email"]
        phone= data["phone"]
        dob= data["dob"]
        status= data["status"]
        password= data["password"]
        location_id= data["location_id"]

        # check if password is valid
        response = passwordvalidity(password)
        if response == True:
            # connect to DB
            connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
            cursor = connection.cursor()
            # instert into database
            sql = "insert into members (surname, others, gender, email, phone, dob, status, password, location_id) values(%s, %s, %s, %s, %s, %s, %s, %s,%s)"
            data = (surname, others, gender, email, phone, dob, status, hash_password(password), location_id)
            # try:
            cursor.execute(sql, data)
            connection.commit( )
            send_sms(phone, "Registration successful")
            return jsonify({ "message": "POST SUCCESSFUL. MEMBER SAVED" })

            # except:
            #     connection.rollback()
            #     return jsonify({ "message": "POST FAILED. MEMBER NOT SAVED" })

        else:
            return jsonify({ "message": response })


class MemberSignin(Resource):
    def post(self):
        # get request from client
        data = request.json
        email = data ["email"]
        password = data ["password"]
        # connect to db
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        
        # check if email exist
        sql = "select* from members where email =%s"
        cursor =connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, email)
        if cursor.rowcount == 0:
            return jsonify({"message":"Email does not exist"})
        else:
            # check password////
            member = cursor.fetchone()
            hashed_password =member['password']
            is_matchpassword = hash_verify(password,hashed_password)
            if is_matchpassword == True:
                return jsonify({"message":"LOG IN SUCCESIFUL"})
            
                # is_matchpassword == False:
            elif is_matchpassword == False:
                return jsonify({ "message":"LOGIN FAILED" })

            else:

                return jsonify({ "message": "Something went wrong" })


class MemberProfile(Resource):
    def post(self):
        data = request.json
        member_id = data["member_id"]
        #  connect to db
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        sql = "select* from members where member_id = %s"
        cursor =connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, member_id)
        count =cursor.rowcount
        if count == 0:
            return jsonify({"message":"Member does not exist"})
        else:
            member = cursor.fetchone()
            return jsonify ({"message": member})

class AddDependant(Resource):
    def post(self):
        data = request.json
        member_id = data ["member_id"]
        surname = data["surname"]
        others = data["others"]
        dob = data["dob"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        cursor= connection.cursor()
        # insert into dependants table
        sql="insert into dependants (member_id, surname, others, dob) values(%s,%s,%s,%s)"
        data = (member_id, surname, others, dob)
        # try:
        cursor.execute(sql,data)
        connection.commit()
        return jsonify({"message":"POST SUCCESSIFUL.Dependant saved"})
        # except:
        #     connection.rollback()
        #     return jsonify({"message":"POST FAILED.Dependant not saved"})
        

        # class ViewDependants(Resource):
        #     def get(self):
        #         data = request.json
        #         member_id=
        #         connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')
        #         sql = "select* from dependants where member =%s"
        #         cursor =connection.cursor(pymysql.cursors.DictCursor)
                