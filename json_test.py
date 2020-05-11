import json

def open_json_file(filename):
    with open(filename, encoding='UTF-8') as file:
        try:
            return json.load(file)
        except ValueError as e:
            print('JSON 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None

json_data = open_json_file('message1.json')
if json_data:
    print(json_data)