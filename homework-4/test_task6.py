import csv
import pytest

def f(name_input,name_output,filter):
    n = 0
    try:
        s1=[]
        with open(name_input,'r',encoding='utf-8') as f1:
            reader = csv.DictReader(f1)
            for row in reader:
                s1.append(row)

    except FileNotFoundError:
        print(name_input,'not found')
    else:
        s2=[row for row in s1 if filter(row)]
        n = len(s2)

        with open(name_output,'w',newline='', encoding='utf-8') as f2:
            writer = csv.DictWriter(f2,fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in s2:
                writer.writerow(row)

    return n

print(f('data/employees.csv','data/employees_with_filter.csv',lambda row: int(row['age'])>30))
print(f('data/employees.csv','data/employees_with_filter.csv',lambda row: row['city'] == 'Москва'))

@pytest.mark.parametrize("name_input,name_output,filter,expected",[
    ('data/employees.csv','data/employees_with_filter.csv',lambda row: int(row['age']) > 30,3),
    ('data/employees.csv','data/employees_with_filter2.csv',lambda row: int(row['age']) > 40,1),
    ('data/employees.csv','data/employees_with_filter2.csv',lambda row: row['city'] == 'Москва',3),
])

def test_f(name_input,name_output,filter,expected):
    assert f(name_input,name_output,filter) == expected
        