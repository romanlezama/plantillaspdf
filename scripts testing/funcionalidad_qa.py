# -*- coding: utf-8 -*-
#####
# Made by Roman Lezama
#####
# Script para subir registros a una forma dado su id
#
#
#####
import sys,json, simplejson
import pyexcel
import datetime ,time
import json, simplejson, re
import types
#from datetime import datetime ,time

from linkaform_api import settings
from linkaform_api import upload_file, network
# preprod
from romanlezama_settings import *
# prod
#from proyectosdemo_settings import *
from pci_utils import PCI_Utils

upfile = upload_file.LoadFile(settings)
net = network.Network(settings)
cr = net.get_collections()

p_utils = PCI_Utils()

TEST = True
RECORDS_PASSED = 0
settings.GLOBAL_COMMUNICATION = ""


if __name__ == "__main__":
    print "***************** Ejecutando el script **********************************"
    current_record = simplejson.loads(sys.argv[1])
    USER_ID = current_record['user_id']
    current_record.pop('other_versions')
    current_record = p_utils.drop_fields_for_patch(current_record)
    record_id = current_record['_id']['$oid']
    current_record['answers']['5c63494cc370fa0023ea1c95'] = 'Hola mundo'
    response = lkf_api.patch_record(current_record, record_id)
    current_record['answers']['5c643638c370fa00240b3336'] = 'procesado'
    response = lkf_api.patch_record(current_record, record_id)
