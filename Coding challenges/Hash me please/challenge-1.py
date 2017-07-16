import requests 
import re
import hashlib

session_id = "b3gg0od4c55m8cr70tf07lpdv5"
cookies = {"PHPSESSID": session_id}
task_page = requests.get('https://ringzer0team.com/challenges/13/', cookies=cookies).text
message_pattern = "----- BEGIN MESSAGE -----<br />\r\n\t\t(.*)<br />\r\n\t\t----- END MESSAGE -----"
message = re.search(message_pattern, task_page, re.DOTALL).group(1)
task_hash = hashlib.sha512(message.encode('utf-8')).hexdigest()
response = requests.get('https://ringzer0team.com/challenges/13/' + str(task_hash), cookies=cookies).text
flag = re.search("<div class=\"alert alert-info\">(.*)</div>", response).group(1)
print(flag)