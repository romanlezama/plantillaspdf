# coding: utf-8
#!/usr/bin/python

#####
# Made by Jose Patricio VM
#####
# Settings de configuracion de OP
#####

from linkaform_api import settings, utils
import requests, simplejson, sys, json

#settings.mongo_hosts = 'db2.linkaform.com:27017,db3.linkaform.com:27017,db4.linkaform.com:27017'
settings.mongo_hosts = '10.138.2.178:27018'
#mongo_hosts = "127.0.0.1"
#settings.mongo_replicaSet = 'linkaform_replica'
settings.mongo_replicaSet = ''
settings.MONGO_READPREFERENCE='secondary'

settings.MAX_POOL_SIZE = 50
settings.WAIT_QUEUE_TIMEOUT = 1000
settings.MONGODB_URI = 'mongodb://%s/?replicaSet=%s&readPreference=%s'%(settings.mongo_hosts, settings.mongo_replicaSet, settings.MONGO_READPREFERENCE)

config = {
    'USERNAME' : 'roman.lezama@linkaform.com',
    'PASS' : '654321',
    'COLLECTION' : 'form_answer',
    #'HOST' : 'db3.linkaform.com',
    'MONGODB_URI':settings.MONGODB_URI,
    #'MONGODB_PASSWORD': mongodb_password_here
    'MONGODB_PORT':27017,
    'MONGODB_HOST': 'localhost',
    'PROTOCOL' : 'https', #http or https
    'HOST' : 'qa.linkaform.com',
    'PORT' : 27017,
    'USER_ID' : 3422,
    'ACCOUNT_ID' : 3422,
    'KEYS_POSITION' : {},
    'USE_JWT': True,
    'IS_USING_APIKEY' : False,
    'JWT_KEY':'',
    'AUTHORIZATION_EMAIL_VALUE' : 'roman.lezama@linkaform.com',
    'AUTHORIZATION_TOKEN_VALUE' : '7d3bde3c53d7e189ed7dda80dad246de7f7e81a2'
}

LOGIN_URL = "https://qa.linkaform.com/api/infosync/user_admin/login/"
session = requests.Session()
reqst = session.post(LOGIN_URL, data = simplejson.dumps({"password": config['PASS'], "username": config['USERNAME']}))
config['JWT_KEY'] = reqst.json()['jwt']

# EL JWT NO ESTÁ FUNCIONANDO --> NO TRAE EL JWT EN jwt_recover
'''jwt_recover = sys.argv
print "********** jwt_recover: ", jwt_recover
user_id_rec = json.loads(jwt_recover[1])['user_id']
jwt_complete = jwt_recover[2]
jwt_rec = json.loads(jwt_complete)
config['JWT_KEY'] = jwt_rec["jwt"].split(' ')[1]'''

settings.config.update(config)
lkf_api = utils.Cache(settings)

#PRODUCCION
#FORM_ID_REPORTE_DE_ORDENES_DE_ORDEN_DE_SERVICIO_SUR = 19537
#DESARROLLO
#FORM_ID_CERTIFICADO_DE_CONTROL_DE_PLAGAS_LA_PAZ = 35878
