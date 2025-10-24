import csv
import json
import pytest

def g1(value):
    if value == '':
        return None
    elif value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    
    try:
        return int(value)
    except ValueError:
        pass
    
    try:
        return float(value)
    except ValueError:
        pass
    
    return value



def g2(input,output):
    data=[]
    with open(input,'r',encoding='utf-8') as f1:
        reader = csv.DictReader(f1)
    
        for row in reader:
            s={}
            for key,value in row.items():
                s[key] = g1(value)
            data.append(s)

    with open(output,'w',encoding='utf-8') as f2:
        json.dump(data,f2,indent=2,ensure_ascii=False)
    return data

print(g2('data/mixed_data.csv','data/mixed_data2.json'))

print(g1('321'))
print(g1('3.1'))
print(g1('true'))
print(g1('false'))
print(g1('Книга'))


@pytest.mark.parametrize("value, expected",[
    ('321',321),
    ('3.1',3.1),
    ('true',True),
    ('false',False),
    ('Книга','Книга'),
])

def test_g1(value,expected):
    assert g1(value) == expected


@pytest.mark.parametrize("input,output, expected",[
    ('data/mixed_data.csv','data/mixed_data2.json',[{'product': 'Ноутбук', 'price': 50000, 'in_stock': True, 'rating': 4.5}, {'product': 'Мышь', 'price': 500, 'in_stock': True, 'rating': 4.2}, {'product': 'Книга', 'price': 1200, 'in_stock': False, 'rating': 4.8}, {'product': 'Клавиатура', 'price': 1500, 'in_stock': True, 'rating': 4.0}]),
])

def test_g2(input,output,expected):
    assert g2(input,output) == expected