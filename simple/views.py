from django.shortcuts import render
from watson_developer_cloud import DocumentConversionV1
import json, os

# Create your views here.
def index(request):
#    document_conversion = DocumentConversionV1(
#	    username='9b8f4bc7-9528-4843-b169-f3778bf843b9',
#	    password='6PsBv4mrDBch',
#	    version='2015-12-15'
#	)
	data = {'test':'fail'}
#    config = {
#	'conversion_target': 'ANSWER_UNITS'
#    }
#    with open(('sample.pdf'), 'rb') as document:
#	response = document_conversion.convert_document(document=document, config=config)
#	data['test'] = response.content.decode()
	a = os.getcwd()
	b = os.path.realpath(__file__)
	c = os.path.dirname(os.path.realpath(__file__))
	data['a'] = a
	data['b'] = b
	data['c'] = c
	return render(request, 'simple/index.html', data)