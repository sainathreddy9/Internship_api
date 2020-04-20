from flask import Flask, request, redirect, jsonify, make_response, g
from models import db
from models import Quote, Contact, Register, quote_schema, contact_schema, register_schema
import urllib.request

from app import app
import os, sys, traceback

@app.route('/postquery', methods=['POST'])
def postQuery():
    try:
        name = 'def'
        emailID = 'def@gmail.com'
        country = 'apa'
        query = 'aa'
        
        if 'name' in request.form:
            name = request.form['name']
        
        if 'emailID' in request.form:
            emailID = request.form['emailID']
            
        if 'country' in request.form:
            country = request.form['country']
            
        if 'query' in request.form:
            query = request.form['query']

        queryObj = Contact(
            name,
            emailID,
            country,
            query
        )
        db.session.add(queryObj)
        db.session.commit()
        return jsonify({'message' : 'Query Posted Successfully'}), 201
        
    except:
        print (traceback.format_exc())
        sys.stdout.flush()

        return jsonify({'message': 'Unexpected Error occurred when posting query. Please try again'}), 405
        
    
@app.route('/req-quote', methods=['POST'])
def reqQuote():
    try:
        name = 'abc'
        emailID = 'abc@gmail.com'
        phoneNum = '8845555'
        country = 'aba'
        fromLang = 'eng'
        toLang = 'eng'
        contentType = 0
        contentSize = 0
        query = 'aa'
        
        if 'name' in request.form:
            name = request.form['name']
        
        if 'emailID' in request.form:
            emailID = request.form['emailID']
            
        if 'phoneNum' in request.form:
            phoneNum = request.form['phoneNum']
            
        if 'country' in request.form:
            country = request.form['country']
            
        if 'fromLang' in request.form:
            fromLang = request.form['fromLang']
            
        if 'toLang' in request.form:
            toLang = request.form['toLang']
            
        if 'contentType' in request.form:
            contentType = request.form['contentType']
            
        if 'contentSize' in request.form:
            contentSize = request.form['contentSize']
            
        if 'query' in request.form:
            query = request.form['query']

        quoteObj = Quote(
            name,
            emailID,
            phoneNum,
            country,
            fromLang,
            toLang,
            contentType,
            contentSize,
            query
        )
        db.session.add(quoteObj)
        db.session.commit()
        return {'message' : 'Request Posted Successfully'}, 201
        
    except:
        print (traceback.format_exc())
        sys.stdout.flush()

        return jsonify({'message': 'Unexpected Error occurred when posting request. Please try again'}), 405

@app.route('/register', methods=['POST'])
def registerUser():
    try:
        name = ''
        emailID = ''
        country = ''
        lang1 = ''
        lang2 = ''
        lang3 = ''
        longDesc = ''
        phoneNum = ''
        pref1 = ''
        pref2 = ''
        pref3 = ''
        
        if 'name' in request.form:
            name = request.form['name']
        
        if 'emailID' in request.form:
            emailID = request.form['emailID']
            
        if 'phoneNum' in request.form:
            phoneNum = request.form['phoneNum']
            
        if 'country' in request.form:
            country = request.form['country']
        
        if 'pref1' in request.form:
            pref1 = request.form['pref1']
            
        if 'pref2' in request.form:
            pref2 = request.form['pref2']
            
            
        if 'pref3' in request.form:
            pref3 = request.form['pref3']
            
            
        if 'lang1' in request.form:
            lang1 = request.form['lang1']
            
        if 'lang2' in request.form:
            lang2 = request.form['lang2']
            
        if 'lang3' in request.form:
            lang3 = request.form['lang3']
    
        if 'longDesc' in request.form:
            longDesc = request.form['longDesc']
            
        registerObj = Register(
            name,
            emailID,
            phoneNum,
            country,
            pref1,
            pref2,
            pref3,
            lang1,
            lang2,
            lang3,
            longDesc
        )
        db.session.add(registerObj)
        db.session.commit()
        return {'message' : 'Request Posted Successfully'}, 201
    except:
        print (traceback.format_exc())
        sys.stdout.flush()

        return jsonify({'message': 'Unexpected Error occurred when posting request. Please try again'}), 405


#This function returns all the entities from the Contact table
# URL:- "http://0.0.0.0:5000/getContacts"

@app.route('/getContacts', methods=['GET'])
def getContacts():
    try:

        contacts = db.session.query(Contact).all()

        results = [
            {
                "name": contact.name,
                "country": contact.country,
            } for contact in contacts]
    
        return {"contacts": results}, 201

    except:
        print(traceback.format_exc())
        sys.stdout.flush()

        return jsonify({'message': 'Unexpected Error occurred when requesting. Please try again'}), 405


#This function returns the entity from the Contact table for a given "ID"
# URL:- "http://0.0.0.0:5000/getContacts/1" where 1 is the id

@app.route('/getContacts/<int:id>', methods=['GET'])
def getContact(id):
    try:

        contact = db.session.query(Contact).get(id)

        result = [
            {
                "id": contact.id,
                "name": contact.name,
                "country": contact.country
            }]

        return {"contact": result}, 201

    except AttributeError as error:

        return jsonify({'Warning': "No Contact available for ID : " + str(id) + ""}), 404

    except:
        print(traceback.format_exc())
        sys.stdout.flush()

        return jsonify({'Error': 'Unexpected Error occurred when requesting. Please try again'}), 405


#This function returns the entity from the Contact table for a given "ID"
# URL:- "http://0.0.0.0:5000/getQuotes"

@app.route('/getQuotes', methods=['GET'])
def getQuotes():
    try:

        quotes = db.session.query(Quote).all()

        results = [
            {
                "name": quote.name,
                "country": quote.country
            } for quote in quotes]

        return {"quotes": results}, 201

    except:
        print(traceback.format_exc())
        sys.stdout.flush()

        return jsonify({'message': 'Unexpected Error occurred when requesting. Please try again'}), 405


#This function returns the entity from the Contact table for a given "ID"
# URL:- "http://0.0.0.0:5000/getQuotes/1" where 1 is the id

@app.route('/getQuotes/<int:id>', methods=['GET'])
def getQuote(id):
    try:

        quote = db.session.query(Quote).get(id)

        result = [
            {
                "id": quote.id,
                "name": quote.name,
                "country": quote.country
            }]

        return {"quote": result}, 201

    except AttributeError as error:

        return jsonify({'Warning': "No Quote available for ID : " + str(id) +""}), 404
    except:
        print(traceback.format_exc())
        sys.stdout.flush()

        return jsonify({'Error': 'Unexpected Error occurred when requesting. Please try again'}), 405


#This function returns the entity from the Contact table for a given "ID"
# URL:- "http://0.0.0.0:5000/getRegisters"

@app.route('/getRegisters', methods=['GET'])
def getRegisters():
    try:

        registers = db.session.query(Register).all()

        results = [
            {
                "name": register.name,
                "country": register.country
            } for register in registers]

        return {"registers": results}, 201
    except:
        print(traceback.format_exc())
        sys.stdout.flush()

        return jsonify({'message': 'Unexpected Error occurred when requesting. Please try again'}), 405


#This function returns the entity from the Contact table for a given "ID"
# URL:- "http://0.0.0.0:5000/getRegisters/1" where 1 is the id

@app.route('/getRegisters/<int:id>', methods=['GET'])
def getRegister(id):
    try:

        register = db.session.query(Register).get(id)

        result = [
            {
                "name": register.name,
                "country": register.country
            }]
        return {"registers": result}, 201

    except AttributeError as error:

        return jsonify({'Warning': "No Register available for ID : " + str(id) + ""}), 404

    except:
        print(traceback.format_exc())
        sys.stdout.flush()

        return jsonify({'Error': 'Unexpected Error occurred when requesting. Please try again'}), 405

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port='5000')
    #app.run(host='127.0.0.1', port='5000')