from lxml import etree # -- need lxml api : 기본 XML 라이브러리와 달리 부분 읽기 기능 지원

## 1 - load xml
def open_xml_file(filename):
    try:
        with open(filename, encoding='UTF8') as file:
            return etree.parse(file, parser=etree.XMLParser(encoding='utf-8'))
    except (KeyError,FileNotFoundError) as e:
        print('XML 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
        return None

xml_tree = open_xml_file('message1.xml')
if not xml_tree:
    #print(etree.tounicode(xml_tree, pretty_print=True))
    exit(0) # 더 이상 로직을 진핼할 수 없으므로 종료

## 2 - read xml : use XPath
def read_xpath(tree, xpath):
    tags = tree.xpath(xpath) # 배열 반환 ex. [<Element number at 0x1b883ca38c8>]
    if tags and len(tags) > 0: # tags에 대한 null 검사 포함
        return True, tags[0] # tags[0] - 배열 요소 1개만 반환
    else:
        return False, None

root_tree = xml_tree.getroot()
print('root={0}'.format(root_tree.tag)) # root=message

exist, number_t = read_xpath(xml_tree, '/message/number')
if not exist:
    pass # exit(0) 대신 사용
else:
    print('number={0}'.format(number_t.text)) # number=12345

_, pi_t = read_xpath(xml_tree, '/message/pi')
print('pi={0}'.format(pi_t.text)) # pi=3.14

_, str_t = read_xpath(xml_tree, '/message/str')
print('str={0}'.format(str_t.text))

for attr in str_t.attrib:
    print('str attribute: {0}={1}'.format(attr, str_t.attrib[attr]))

exist, null_t = read_xpath(xml_tree, '/message/null_tag')
assert exist # -- exist 값이 항상 실존하도록 assert 처리
print('null_tag={0}'.format(null_t.text))

_, object_t = read_xpath(xml_tree, '/message/object')
_, str2_t = read_xpath(object_t, 'str2')
print('str2={0}'.format(str2_t.text))

# -- 최상위 트리에서 시작하는 것이 아니기에 '/'로 시작하지 않음
_, number2_t = read_xpath(object_t, 'object2/number2')
print('number2={0}'.format(number2_t.text))

_, number2_t = read_xpath(object_t, '/message/object/object2/number2')
print('number2={0}'.format(number2_t.text))

_, num_array_t = read_xpath(xml_tree, '/message/num_array')
for element in num_array_t.xpath('element'):
    print('element={0}'.format(element.text))
    for attr in element.attrib:
        print('\telement attribute: {0}={1}'.format(attr, element.attrib[attr]))

_, str_array_t = read_xpath(xml_tree, 'message/str_array')
for element in num_array_t.xpath('element'):
    print('str element={0}'.format(element.text))

## 3 - read xml : use iterator
def read_all(tree, xpath):
    for tag in tree:
        if len(tag) > 0:
            # 객체 또는 배열 요소인 경우
            read_all(tag, '{0}/{1}'.format(xpath, tag.tag))
        else:
            if tag.text:
                print('{0}/{1}={2}'.format(xpath, tag.tag, tag.text))
            else:
                print('{0}/{0}'.format(xpath, tag.tag))

# iterator 기반 접근
exist, root_tree = read_xpath(xml_tree, '/message')
assert exist
read_all(root_tree, root_tree.tag)

## 4. create XML
def to_xml(tree, dict_object):
    for key in dict_object:
        element = etree.SubElement(tree, key) # key에 해당하는 서브트리 객체 생성
        value = dict_object[key] # key에 대응하는 값의 타입 검사
        if value:
            if type(value) is str:
                element.text = value
            elif type(value) is dict: # 현재 트리를 최상위 트리로 지정하고
                to_xml(element, value) # 새로운 트리를 만들도록(재귀)
            elif type(value) is list:
                for v in value:
                    assert type(v) is str
                    etree.SubElement(element, 'element').text = v
            else:
                assert False

message2 = {
    u'number': u'12345',
    u'pi': u'3.14',
    u'str': u'문자열 값',
    u'null_tag': None,
    u'object': {
        u'str2': u'문자열 값 2',
        u'object2': {
            u'number2': u'12345'
        }
    },
    u'num_array': [u'1', u'2', u'3', u'4', u'5'],
    u'str_array': [u'one', u'two', u'three', u'four', u'five']
}

xml_tree = etree.Element('message')
to_xml(xml_tree, message2)

# xml_declaration = True : 헤더 삽입으로 유지보수를 수월하게
with open('test_by_sunn.xml', 'wb') as file:
    file.write(etree.tostring(
        xml_tree, xml_declaration=True, encoding='UTF-8', pretty_print=True))