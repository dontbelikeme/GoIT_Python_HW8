from datetime import date, datetime, timedelta
from os import name

users = [ { 'name': 'Rimma_Obukhova',
        'birthday': '12.01.1970'},
        {'name': 'Vika_Litvinenko',
        'birthday': '20.01.1970'},
        {'name':'Tasmina_Plevako',
        'birthday': '22.01.1970'},
        {'name':'Vitaliy_Kienko',
        'birthday': '31.01.1970'},
        {'name':'Elena_Shkodich',
        'birthday':'25.01.1970'},
        {'name': 'Alina_Moiseenko',
        'birthday':'20.01.1970'},
        {'name':'Alexandra_Rekshnya',
        'birthday':'10.01.1970'},
        {'name':'Evheniy_Kuzminov',
        'birthday':'01.02.1970'},
        {'name':'Elena_Babich',
        'birthday':'09.02.1970'},
        
        {'name':'Irina_14',
        'birthday':'14.02.1970'},
        {'name':'Irinaaaaa_13',
        'birthday':'13.02.1970'},
        {'name':'Irina_15',
        'birthday':'15.02.1970'},
        
        
        {'name':'Irina_Kudryashova',
        'birthday':'14.02.1970'},
        {'name':'Viktoriya_Minka',
        'birthday':'28.02.1970'},
        {'name':'Vera_Boyko',
        'birthday':'07.03.1970'},
        {'name':'Nastya_Grabichenko',
        'birthday':'01.03.1970'},
        {'name':'Nastya_Yurieva',
        'birthday':'09.03.1970'},
        {'name':'Vitaliy_Misevra',
        'birthday':'17.03.1970'},
        {'name':'Janna_Tukalova',
        'birthday':'29.03.1970'},
        {'name':'Oksana_Yanova',
        'birthday':'27.03.1970'},
        {'name':'Natasha_Karkunova',
        'birthday':'13.04.1970'},
        {'name':'Irina_Pravda',
        'birthday':'22.04.1970'},
        {'name':'Inna_Panchenko',
        'birthday':'28.04.1970'},
        {'name':'Yana_Markova',
        'birthday':'27.04.1970'},
        {'name':'Artem_Nijnik',
        'birthday':'17.04.1970'},
        {'name':'Alexey_Kucheryavenko',
        'birthday':'04.05.1970'},
        {'name':'Irina_Morozova',
        'birthday':'18.05.1970'},
        {'name':'Oksana_Babko',
        'birthday':'08.05.1970'},
        {'name':'Elzara_Boar',
        'birthday':'25.05.1970'},
        {'name':'Viktoriya_Veremeenko',
        'birthday':'09.05.1970'},
        {'name':'Alexey_Pavlov',
        'birthday':'22.05.1970'},
        {'name':'ZAKHAR',
        'birthday':'15.05.1970'},
        {'name':'Nastya_Efimtsova',
        'birthday':'31.05.1970'},
        {'name':'Nataliya_Diachenko',
        'birthday':'17.05.1970'},
        {'name':'Elena_Semenova',
        'birthday':'24.05.1970'},
        {'name':'Tanya_Koliy',
        'birthday':'01.06.1970'},
        {'name':'Katya_Laz',
        'birthday':'07.06.1970'},
        {'name':'Polina_Demochko',
        'birthday':'24.06.1970'},
        {'name':'Kostya_Titar',
        'birthday':'23.06.1970'},
        {'name':'Masha_Chertkova',
        'birthday':'14.06.1970'},
        {'name':'Angelika_Belitskaya',
        'birthday':'4.06.1970'},
        {'name':'Alenz_Belova',
        'birthday':'17.07.1970'},
        {'name':'Alevtina_Shevchenko',
        'birthday':'10.07.1970'},
        {'name':'Maria_Kuhareva',
        'birthday':'14.07.1970'},
        {'name':'Irina_Babich',
        'birthday':'16.07.1970'},
        {'name':'Dmitriy_Eskribano',
        'birthday':'16.07.1970'},
        {'name':'Elizaveta_Mishchenko',
        'birthday':'18.07.1970'},
        {'name':'Natasha_Politanskaya',
        'birthday':'30.07.1970'},
        {'name':'Rita',
        'birthday':'09.08.1970'},
        {'name':'Konstantin_Alipov',
        'birthday':'13.08.1970'},
        {'name':'Alyona_Maslyanik',
        'birthday':'30.08.1970'},
        {'name':'Liliya_Gritsay',
        'birthday':'02.08.1970'},
        {'name':'Tatiana_Bondarenko',
        'birthday':'23.09.1970'},
        {'name':'Vladislav_Yukhimenko',
        'birthday':'25.09.1970'},
        {'name':'Katya_Sterina',
        'birthday':'09.10.1970'},
        {'name':'Ivan_Podolyak',
        'birthday':'12.10.1970'},
        {'name':'Irina_Rakitskaya',
        'birthday':'15.10.1970'},
        {'name':'Natasha_Ovdienko',
        'birthday':'13.10.1970'},
        {'name':'Ekaterina_Molodan',
        'birthday':'21.10.1970'},
        {'name':'Ekaterina_Kudinova',
        'birthday':'20.10.1970'},
        {'name':'Yana_Solo',
        'birthday':'01.11.1970'},
        {'name':'Anya_Akhmadeeva',
        'birthday':'15.11.1970'},
        {'name':'Vika_Krutash',
        'birthday':'22.11.1970'},
        {'name':'Anya_Susak',
        'birthday':'23.11.1970'},
        {'name':'Yuri_Yarovoy',
        'birthday':'25.11.1970'},
        {'name':'Sergey_P',
        'birthday':'28.11.1970'},
        {'name':'Igor_Ivanov',
        'birthday':'05.11.1970'},
        {'name':'Andrey_Tsvilev',
        'birthday':'23.11.1970'},
        {'name':'Milhail_Maslak',
        'birthday':'21.11.1970'},
        {'name':'Nataliya_Maslak',
        'birthday':'14.11.1970'},
        {'name':'Alyona_Kibalnik',
        'birthday':'14.11.1970'},
        {'name':'Natasha_Chalaya',
        'birthday':'11.11.1970'},
        {'name':'Anastasiya_Artamonova',
        'birthday':'24.12.1970'},
        {'name':'Viktoriya_Shestopalova',
        'birthday':'08.12.1970'},
        {'name':'Viktoriya_Perepelkina',
        'birthday':'09.12.1970'},
        {'name':'Aleksandriya_Zotova',
        'birthday':'27.12.1970'},
        {'name':'Masha_HR',
        'birthday':'11.12.1970'},
        {'name':'Liliya_Belogurova',
        'birthday':'29.12.1970'},
        {'name':'Dima_Demchenko',
        'birthday':'10.12.1970'},
        {'name':'Vladimir_Reshetnyak',
        'birthday':'15.12.1970'}
]


bd_res1 = []
bd_res2 = []
bd_res3 = []
bd_res4 = []
bd_res5 = []

bd_dict = {}
result = []
string = []
dn = date.today()
for val in users:
    b_day =val.get('birthday') 
    b_d = datetime.strptime(b_day, '%d.%m.%Y')
    b_d = b_d.replace(year=dn.year)
    dt = datetime.now()
    time_to_birthday = (b_d - dt)
    if time_to_birthday.days >= 0 and time_to_birthday.days < 8:
        result.append(val)


            
for res in result:
    #bd_name.append(res.get('name'))
    bday = res.get('birthday')
    birth_day = datetime.strptime(bday, '%d.%m.%Y')
    birth_day = birth_day.replace(year=dn.year)
    day_output = datetime.strftime(birth_day, '%A')
    if day_output == 'Sunday':
        bd_res1.append(res.get('name'))
    elif day_output == 'Saturday':
        bd_res1.append(res.get('name'))
    elif day_output == 'Monday':           
        bd_res1.append(res.get('name'))
    elif day_output == 'Tuesday':
        bd_res2.append(res.get('name'))    
    elif day_output == 'Wednesday':
        bd_res3.append(res.get('name'))
    elif day_output == 'Thursday':
        bd_res4.append(res.get('name'))      
    elif day_output == 'Friday':
        bd_res5.append(res.get('name'))
    #print(f'{day_output}:{str(bd_name)}')

if len(bd_res1) > 0:
    bd_dict['Moday'] = (', '.join(bd_res1))
if len(bd_res2) > 0:
    bd_dict['Tuesday'] = (', '.join(bd_res2))
if len(bd_res3) > 0:
    bd_dict['Wednesday'] = (', '.join(bd_res3))
if len(bd_res4) > 0:
    bd_dict['Thursday'] = (', '.join(bd_res4))
if len(bd_res5) > 0:
    bd_dict['Friday'] = (', '.join(bd_res5))
    
    
print('\n'.join("{}: {}".format(k, v) for k, v in bd_dict.items()))    