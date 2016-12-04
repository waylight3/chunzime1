from watson_developer_cloud import DocumentConversionV1
import json

document_conversion = DocumentConversionV1(
	username='7f95d9a2-dbf2-4b6b-bc9f-1b96fad8ad1b',
	password='EhxVdVQX7Dyr',
	version='2015-12-15'
)

config = {
	'conversion_target': 'ANSWER_UNITS'
}

with open(('sample.pdf'), 'rb') as document:
	response = document_conversion.convert_document(document=document, config=config)
	print(json.dumps(response.content.decode(), indent=2))