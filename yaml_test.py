import yaml # -- need pyyaml api

## 1 - load yaml
def open_yaml_file(filename):
    try:
        with open(filename, encoding='UTF8') as file:
            return yaml.load(file, Loader=yaml.SafeLoader)
    #except yaml.parser.ParserError as e:
    except (ValueError,FileNotFoundError) as e:
        print('YAML 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
        return None

yaml_data = open_yaml_file('message1.yaml')
if not yaml_data:
    exit(0) # 더 이상 로직을 진핼할 수 없으므로 종료

## 2 - create yaml
def create_yaml_file(filename,yaml_object):
    # yaml : UTF-16 지원
    # allow_unicode=False 인 경우에는 아스키 코드가 아닌 모든 문자열을 \uXXXX로 표기
    # ex. str2: "\uBB38\uC790\uC5F4 \uAC12 2"
    with open(filename, 'w', encoding='UTF8') as file:
        yaml.dump(yaml_object, file, allow_unicode=True)

yaml_object = {
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
create_yaml_file('test_by_sunn.yaml', yaml_object)

## 3 - anchor & alias
yaml_data = open_yaml_file('realapp_config2.yaml')
print(yaml_data)