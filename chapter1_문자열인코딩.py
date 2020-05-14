print('10진수(01000001)={0}'.format(0b01000001))
print('16진수(01000001)={0}'.format(hex(0b01000001)))
print('문자(01000001)={0}'.format(chr(0b01000001)))

# 0b - 2진수를 명시하기 위한 것
# 유니코드 문자열 인코딩 방식 : UTF-8, UTF-16, UTF-32
# 문자 집합(charset) : 유니코드, ISO-8859, ASCII 등

# 1. 아스키 코드(ASCII) : 0 - 127까지, 총 8비트(=1바이트)
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{0}".format(int(c)) for c in byte_data)

    print('\'' + text + '\' 전체 문자 길이: {0}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는데 사용한 바이트 수: {0} 바이트'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))

print_text('Hello', 'ascii')

# 2. EUC-KR(CP949) : 문자 하나에 2바이트, 아스키와 호환
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{0}".format(int(c)) for c in byte_data)

    print('\'' + text + '\' 전체 문자 길이: {0}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는데 사용한 바이트 수: {0} 바이트'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))

print_text('Hello', 'euc-kr')
print_text('안녕하세요', 'euc-kr')

# 실제 문자열 길이 : 사람 눈에 보이는 문자 길이
# 버퍼 길이 : 컴퓨터가 문자를 표현하는 데 사용한 바이트 수
# 버퍼 : 메모리에 할당된 공간

# 3. 유니코드
## 3-1) UTF-8 : 8비트 = 1바이트, 최소 1바이트 ~ 6바이트까지, 아스키 코드와 호환
## 윈도우, 자바, 임베디드를 제외한 거의 모든 환경에서의 문자열 처리 표준
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{0}".format(int(c)) for c in byte_data)

    print('\'' + text + '\' 전체 문자 길이: {0}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는데 사용한 바이트 수: {0} 바이트'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))

print_text('Hello', 'utf-8')
print_text('안녕하세요', 'utf-8')

## 3-2) UTF-16 : 16비트 = 2바이트, 2바이트(일반 글자) 또는 4바이트(특별한 글자) 사용으로 아스키 코드와 호환x
## 자바와 윈도우에서의 표준으로 멀티 바이트라고도 한다.
def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{0}".format(int(c)) for c in byte_data)

    print('\'' + text + '\' 전체 문자 길이: {0}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는데 사용한 바이트 수: {0} 바이트'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))

print_text('Hello', 'utf-16')
print_text('안녕하세요', 'utf-16') # 0xff 0xfe 추가되어, 10바이트가 아닌 12바이트 사용

# BOM(Byte Order Mark) : 바이트 순서 표시 in UTF-16, UTF-32 > CPU 설계에 따라 바이트 값을 처리하는 순서가 달라서 필요
# (1) 0xFF 먼저 : 리틀 엔디언(LE) - 작은 것부터 읽기
# (2) 0xFE 먼저: 빅 엔디언(BE) - 큰 것부터 읽기