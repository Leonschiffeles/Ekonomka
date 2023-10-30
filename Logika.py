import sqlite3

def get_dannue():
    all_data = []
    with sqlite3.connect('bd/baza.db') as bd:
        bd.row_factory = sqlite3.Row
        cursor = bd.cursor()
        zapros = """ SELECT * FROM Оплата JOIN Расходы ON Расходы.id = Оплата.Расходы_id  """
        cursor.execute(zapros)
        all_data = zapros
    return all_data

def get_nachtochashe():
    dannue = get_dannue()
    kolichestvo = {}
    for Оплата in dannue:
        if Оплата['Расходы_id'] in kolichestvo:
            kolichestvo[Оплата['Расходы_id']]['straskh'] += 1
        else:
            kolichestvo[Оплата['Расходы_id']] = {'straskh' : 1, 'name' : Оплата['name']}
    return max(kolichestvo.values(), key= lambda x: x['straskh'])['name']

def get_kakoyden():
    dannue = get_dannue()
    kolichestvo = {}
    for Оплата in dannue:
        if Оплата['Расходы_id'] in kolichestvo:
            kolichestvo[Оплата['Расходы_id']]['straskh'] += 1
        else:
            kolichestvo[Оплата['Расходы_id']] = {'straskh' : 1, 'name' : Оплата['name']}
    return max(kolichestvo.values(), key= lambda x: x['straskh'])['name']


def get_kakoyden():
    dannue = get_dannue()
    kolichestvo = {}
    for Оплата in dannue:
        if Оплата['Расходы_id'] in kolichestvo:
            kolichestvo[Оплата['Расходы_id']]['straskh'] += 1
        else:
            kolichestvo[Оплата['Расходы_id']] = {'straskh' : 1, 'name' : Оплата['name']}
    return max(kolichestvo.values(), key= lambda x: x['straskh'])['name']

def get_kakoymesyac():
    dannue = get_dannue()
    kolichestvo = {}
    for Оплата in dannue:
        if Оплата['Расходы_id'] in kolichestvo:
            kolichestvo[Оплата['Расходы_id']]['straskh'] += 1
        else:
            kolichestvo[Оплата['Расходы_id']] = {'straskh' : 1, 'name' : Оплата['name']}
    return max(kolichestvo.values(), key= lambda x: x['straskh'])['name']
