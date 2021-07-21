import time
import trino
import pytest
import requests
   


    
conn = trino.dbapi.connect(host='localhost', port=4000, user='admin' )
    
# A SUCCESSFULL GET REQUEST
url_ping = "http://localhost:80/ping"
response_ping = requests.get(url_ping)
    
    
#AN UNSUCCESSFULL POST REQUEST
url_submit = "http://localhost:80/submit"
myobj = {"msg": "submit"}
response_submit = requests.post(url_submit, data = myobj)

    
    
cur1 = conn.cursor()
cur1.execute("SELECT * FROM resurface.data.message WHERE request_url = 'http://localhost/ping' ")
rows1 = cur1.fetchall()
columns1 = dict([desc[:2] for desc in cur1.description])
conn.close()
        
   
cur2 = conn.cursor()
cur2.execute("SELECT * FROM resurface.data.message WHERE request_url = 'http://localhost/submit' ")
rows2 = cur2.fetchall()
columns2 = dict([desc[:2] for desc in cur2.description])
conn.close()
        
columns = columns1
rows = rows1
        


def test_empty():    
	assert len(rows) > 0

def test_columns():	
	assert columns["id"] == "varchar"
	assert columns["agent_category"] == "varchar"
	assert columns["agent_device"] == "varchar"
	assert columns["agent_name"] == "varchar"
	assert columns["graphql_operation"] == "varchar"
	assert columns["graphql_operation_name"] == "varchar"
	assert columns["host"] == "varchar"
	assert columns["interval_millis"] == "bigint"
	assert columns["request_body"] == "varchar"
	assert columns["request_content_type"] == "varchar"
	assert columns["request_headers"] == "varchar"
	assert columns["request_json_type"] == "varchar"
	assert columns["request_method"] == "varchar"
#assert rows[0][12] == "GET"
	assert columns["request_params"] == "varchar"
	assert columns["request_url"] == "varchar"
#assert rows[0][14] == "http://localhost/ping"
#assert rows2[0][14] == "http://localhost/submit"
	assert columns["request_user_agent"] == "varchar"
	assert columns["response_body"] == "varchar"
#assert rows[0][15] == "{"msg": "pong"}"
	assert columns["response_code"] == "varchar"
#assert rows[0][17] == "200"
#assert rows2[0][17] == "404"
	assert columns["response_content_type"] == "varchar"
#assert rows[0][18] == "application/json"
#assert rows2[0][18] == "text/html"
	assert columns["response_headers"] == "varchar"
	assert columns["response_json_type"] == "varchar"
#assert rows[0][20] == "OBJECT"
	assert columns["response_time_millis"] == "bigint"
	assert columns["size_request_bytes"] == "integer"
	assert columns["size_response_bytes"] == "integer"
        
def test_get_200():
	assert rows[0][12] == "GET"
	assert rows[0][14] == "http://localhost/ping"
	assert rows[0][17] == "200"
#	assert rows[0][18] == "application/json"
	assert rows[0][20] == "OBJECT"
        
def test_post_404():
	assert rows2[0][12] == "POST"
	assert rows2[0][14] == "http://localhost/submit"
	assert rows2[0][17] == "404"
#	assert rows2[0][18] == "text/html"
	
	
'''
COLUMNS
'id': 'varchar',
 'agent_category': 'varchar',
 'agent_device': 'varchar',
 'agent_name': 'varchar',
 'graphql_operation': 'varchar',
 'graphql_operation_name': 'varchar',
 'host': 'varchar',
 'interval_millis': 'bigint',
 'request_body': 'varchar',
 'request_content_type': 'varchar',
 'request_headers': 'varchar',
 'request_json_type': 'varchar',
 'request_method': 'varchar',
 'request_params': 'varchar',
 'request_url': 'varchar',
 'request_user_agent': 'varchar',
 'response_body': 'varchar',
 'response_code': 'varchar',
 'response_content_type': 'varchar',
 'response_headers': 'varchar',
 'response_json_type': 'varchar',
 'response_time_millis': 'bigint',
 'size_request_bytes': 'integer',
 'size_response_bytes': 'integer'
 
ROWS
['c66928e9-7b3b-4719-bf24-d1d37ac4bc9e',
  'Unknown',
  'Unknown',
  'Python-Requests',
  None,
  None,
  '572e2ccefc44',
  4,
  None,
  None,
  '[["host","localhost"],["accept-encoding","gzip, deflate"],["accept","*/*"],["connection","keep-alive"]]',
  None,
  'GET',
  '[]',
  'http://localhost/ping',
  'python-requests/2.22.0',
  '{"msg":"pong"}',
  '200',
  'application/json; charset=utf-8',
  '[["x-powered-by","Express"],["content-length","14"],["etag","W/\\"e-iBi3XUufBylnoseozcoWz+s0EIA\\""],["set-cookie","connect.sid\\u003ds%3ADR9IQh00xO8E__6R0rBJS5J3H-_4UzpB.elQm34w3RJ6h9PFQW2L9MCMAis0qYnDZq%2BiVhAghOTs; Path\\u003d/; Expires\\u003dWed, 21 Jul 2021 17:48:57 GMT; HttpOnly"]]',
  'OBJECT',
  1626889677781,
  123,
  290]

-------------------------------
response_ping.__getstate__()

{'_content': b'{"msg":"pong"}',
 'status_code': 200,
 'headers': {'X-Powered-By': 'Express', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '14', 'ETag': 'W/"e-iBi3XUufBylnoseozcoWz+s0EIA"', 'Set-Cookie': 'connect.sid=s%3A-DF-dS3EywwvAkEH6AqeTjWLVZyBger2.3cZ8ASlcp7CSSyz7RbFFAXdildLZc720cmbHeBE9BA4; Path=/; Expires=Wed, 21 Jul 2021 17:50:15 GMT; HttpOnly', 'Date': 'Wed, 21 Jul 2021 17:49:15 GMT', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=5'},
 'url': 'http://localhost:80/ping',
 'history': [],
 'encoding': 'utf-8',
 'reason': 'OK',
 'cookies': <RequestsCookieJar[Cookie(version=0, name='connect.sid', value='s%3A-DF-dS3EywwvAkEH6AqeTjWLVZyBger2.3cZ8ASlcp7CSSyz7RbFFAXdildLZc720cmbHeBE9BA4', port=None, port_specified=False, domain='localhost.local', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=1626889815, discard=False, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)]>,
 'elapsed': datetime.timedelta(microseconds=4852),
 'request': <PreparedRequest [GET]>}

---------------------------------
response_submit.__getstate__()

{'_content': b'{"detail": "/submit not found"}',
 'status_code': 404,
 'headers': {'Server': 'gunicorn', 'Date': 'Wed, 21 Jul 2021 17:43:12 GMT', 'Connection': 'close', 'Content-Type': 'application/json', 'X-Frame-Options': 'DENY', 'Content-Length': '31', 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'same-origin'},
 'url': 'http://localhost:80/submit',
 'history': [],
 'encoding': None,
 'reason': 'Not Found',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=14894),
 'request': <PreparedRequest [POST]>}
 
 
'''        

