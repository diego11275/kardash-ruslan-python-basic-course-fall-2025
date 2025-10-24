import re
import pytest

def g1(name_input):
    s={
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(name_input,'r',encoding='utf-8') as f:
        for line in f:
            match = re.search(r'\]\s+(\w+):', line)
            if match:
                level = match.group(1)
                s[level]+=1
    
    return s

def g2(name_input):
    s=[]

    with open(name_input,'r',encoding='utf-8') as f:
        for line in f:
            match = re.search(r'ERROR:\s*(.*)', line)
            if match:
                s.append(match.group(1))
    
    return s

print(g1('data/application.log'))
print(g1('data/file1.txt'))
print(g2('data/application.log'))
print(g2('data/file1.txt'))

# запускать тесты через терминал из нового файла с расширением .py
# pytest .\test_task9.py -v

@pytest.mark.parametrize("name_input, expected",[
    ('data/application.log',{'INFO': 12, 'WARNING': 4, 'ERROR': 4}),
    ('data/file1.txt',{'INFO': 0, 'WARNING': 0, 'ERROR': 0}),
])

def test_g1(name_input,expected):
    assert g1(name_input) == expected


@pytest.mark.parametrize("name_input, expected",[
    ('data/application.log',['Connection to database failed', 'File not found: config.json', 'Invalid user input', 'Failed to send notification']),
    ('data/file1.txt',[]),
])

def test_g2(name_input,expected):
    assert g2(name_input) == expected