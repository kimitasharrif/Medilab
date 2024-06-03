# nurse sign in resource
# surname and password to log in
import pymysql
from flask_restful import*
from flask import*
from functions import*
import pymysql.cursors


# jwt packages
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

class Nurse_Signin(Resource):
    @jwt_required(fresh= True)
    def get(self):
        data = request.json
        surname = data["surname"]
        password = data["password"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')  
        sql = " select* from nurses where surname=%s"
        cursor =connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, surname)
        if cursor.rowcount ==0:
            return jsonify ({"message":"No such surname"})
        else:
            nurses = cursor.fetchone()
            hashed_password =nurses['password']
            is_matchpassword = hash_verify(password,hashed_password)
            if is_matchpassword == True:
                #including jwt
                access_token = create_access_token(identity= nurses, fresh= True)
                return jsonify({'access_token': access_token,'nurses':nurses})
            
                # is_matchpassword == False:
            elif is_matchpassword == False:
                return jsonify({ "message":" NURSE LOGIN FAILED" })

            else:

                return jsonify({ "message": "Something went wrong" })
            

class NurseProfile(Resource):
    @jwt_required(fresh= True)
    def get(self):
        data = request.json
        surname =data["surname"]
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab') 
        cursor =connection.cursor(pymysql.cursors.DictCursor) 
        sql = "select* from nurses where surname = %s"
        cursor.execute(sql,surname)
        connection.commit()
        if cursor.rowcount==0:
            return jsonify({"message":"Nurse not found"})
        else:
            nurses = cursor.fetchone()
            return jsonify({"message":nurses})
        


class ChangePassword(Resource):
    @jwt_required(fresh= True)
    def put(self):
        data = request.json 
        nurse_id = data["nurse_id"]
        current_password = data["current_password"] 
        new_password = data["new_password"]
        confirm_password = data["confirm_password"]    
        connection = pymysql.connect(host='localhost', user='root',password='',database='Medilab')  
        sql = "select* from nurses where nurse_id=%s"
        cursor =connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, nurse_id)
        if cursor.rowcount ==0:
            return jsonify({"message":"Nurse not found"})
        else:
            nurse =cursor.fetchone()
            hash_password= nurse["password"]
            return jsonify(hash_password)

