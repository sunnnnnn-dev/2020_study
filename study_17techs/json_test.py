import json

## 1 - load json
def open_json_file(filename):
    try:
        with open(filename, encoding='UTF-8') as file:
            return json.load(file)
    except (ValueError,FileNotFoundError) as e:
        print('JSON 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
        return None

json_data = open_json_file('message1.json')
if not json_data:
    exit(0) # 더 이상 로직을 진행할 수 없으므로 종료

## 2 - control error
def json_catch_unknown(filename,unknown_key):
    json_data = open_json_file(filename)
    try:
        unknown_value = json_data[unknown_key]
        print(f'{unknown_key}={unknown_value}')
    except KeyError:
        print(f'key-{unknown_key}는 존재하지 않습니다.')

json_catch_unknown('message1.json', 'test_key')

def json_detect_unknown(filename,unknown_key):
    json_data = open_json_file(filename)
    if unknown_key in json_data:
        unknown_value = json_data[unknown_key]
        print(f'{unknown_key}={unknown_value}')
    else:
        print(f'key-{unknown_key}는 존재하지 않습니다.')

json_detect_unknown('message1.json', 'test_key')

## 3 - create json
def create_json_file(filename,json_object):
    # ensure_ascii=True 인 경우에는 아스키 코드가 아닌 모든 문자열을 \uXXXX로 표기
    # ex. "str": "\ubb38\uc790\uc5f4 \uac12"
    with open(filename, 'w', encoding='UTF8') as file:
        json.dump(json_object, file, ensure_ascii=False, indent='\t', sort_keys=True)

json_object = {
    u'number': 12345,
    u'pi': 3.14,
    u'str': u'문자열 값',
    u'null_key': None,
    u'object': {
        u'str2': u'문자열 값 2',
        u'object2': {
            u'number2': 12345
        }
    },
    u'num_array': [1, 2, 3, 4, 5],
    u'str_array': [u'one', u'two', u'three', u'four', u'five']
}
create_json_file('test_by_sunn.json', json_object)