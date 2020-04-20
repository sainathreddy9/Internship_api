from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_marshmallow import Marshmallow
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired


#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Baral123!@database-1.cxct8w2slfwz.us-east-1.rds.amazonaws.com/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Rjalla@localhost/intern_api'
db = SQLAlchemy(app)

ma = Marshmallow(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=False)
    emailID = db.Column(db.String(100), unique=False)
    country = db.Column(db.String(40), unique=False)
    query = db.Column(db.Text, unique=False)
    
    def __init__(self,
                 name,
                 emailID,
                 country,
                 query
    ):
        self.name = name
        self.emailID = emailID
        self.country = country
        self.query = query

class ContactSchema(ma.Schema):
    class Meta:
        fields = (
            'name',
            'emailID',
            'country',
            'query'
        )
contact_schema = ContactSchema(many = True)

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=False)
    emailID = db.Column(db.String(100), unique=False)
    phoneNum = db.Column(db.String(25), unique=False) 
    country = db.Column(db.String(40), unique=False)
    fromLang = db.Column(db.String(40), unique=False)
    toLang = db.Column(db.String(40), unique=False)
    packageType = db.Column(db.Integer, unique=False)
    contentSize = db.Column(db.Integer, unique=False)
    query = db.Column(db.Text, unique=False)
    
    def __init__(self,
                 name,
                 emailID,
                 phoneNum,
                 country,
                 fromLang,
                 toLang,
                 packageType,
                 contentSize,
                 query
    ):
        self.name = name
        self.emailID = emailID
        self.phoneNum = phoneNum
        self.country = country
        self.fromLang = fromLang
        self.toLang = toLang
        self.packageType = packageType
        self.contentSize = contentSize
        self.query = query

class QuoteSchema(ma.Schema):
    class Meta:
        fields = (
            'name',
            'emailID',
            'phoneNum',
            'country',
            'fromLang',
            'toLang',
            'packageType',
            'contentSize',
            'query'
        )
quote_schema = ContactSchema(many = True)


class Register(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=False)
    emailID = db.Column(db.String(100), unique=False)
    phoneNum = db.Column(db.String(25), unique=False)
    country = db.Column(db.String(40), unique=False)
    pref1 = db.Column(db.String(2), unique=False)
    pref2 = db.Column(db.String(2), unique=False)
    pref3 = db.Column(db.String(2), unique=False)
    lang1 = db.Column(db.String(40), unique=False)
    lang2 = db.Column(db.String(40), unique=False)
    lang3 = db.Column(db.String(40), unique=False)
    longDesc = db.Column(db.Text, unique=False)
    
    def __init__(self,
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
    ):
        self.name = name
        self.emailID = emailID
        self.country = country
        self.phoneNum = phoneNum
        self.pref1 = pref1
        self.pref2 = pref2
        self.pref3 = pref3
        self.lang1 = lang1
        self.lang2 = lang2
        self.lang3 = lang3
        self.longDesc = longDesc

class RegisterSchema(ma.Schema):
    class Meta:
        fields = (
            'name',
            'emailID',
            'phoneNum',
            'country',
            'pref1',
            'pref2',
            'pref3',
            'lang1',
            'lang2',
            'lang3',
            'longDesc'
        )
register_schema = ContactSchema(many = True)