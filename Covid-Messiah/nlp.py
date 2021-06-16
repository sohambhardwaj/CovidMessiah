import dialogflow
import os
from google.api_core.exceptions import InvalidArgument


DIALOGFLOW_PROJECT_ID = 'covid-helper-bot-ixvu'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'covid-helper-bot-ixvu-99fe8fc1c8f2.json'
SESSION_ID = 'current-user-id-1'

def natlangpro(string):
	text_to_be_analyzed = string
	session_client = dialogflow.SessionsClient()
	session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
	text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
	query_input = dialogflow.types.QueryInput(text=text_input)
	try:
	    response = session_client.detect_intent(session=session, query_input=query_input)
	except InvalidArgument:
	    raise
	keyword=[]
	city=""
	res=str(response.query_result.fulfillment_text)
	res=res.split()
	keyword.append(res[0])
	keyword.append(res[1])
	if len( str(response.query_result.parameters.fields['geo-city'].list_value) )==0:
		city=""
	else:
		city=str(response.query_result.parameters.fields['geo-city'].list_value.values[0].string_value)
		keyword.append(city)
	
	return keyword
