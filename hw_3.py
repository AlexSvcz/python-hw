import pandas as pd

df = pd.read_csv('train.csv')

print('ПЕРВЫЕ СТРОКИ ТАБЛИЦЫ:')
print(df.head())
print()

print('1. ОБЩАЯ ИНФОРМАЦИЯ О ДАТАСЕТЕ')
print('-----------------------------')
print('Типы данных по колонкам:')
print(df.dtypes)
print()
print('Число пропусков по колонкам:')
print(df.isna().sum())
print()
print('Средние значения числовых колонок:')
for column in df.columns:
    if df[column].dtype in ['int64', 'float64']:
        print(column, round(df[column].mean(), 2))
print()
print('Основные статистики:')
print(df.describe())
print()

print('2. ПРОЦЕНТ ВЫЖИВАЕМОСТИ ПО КЛАССАМ ПАССАЖИРОВ (Pclass)')
print('------------------------------------------------------')
for i in range(1, 4):
    pass_in_class = df[df['Pclass'] == i]
    surv_in_class = df[(df['Pclass'] == i) & (df['Survived'] == 1)]
    percent = len(surv_in_class) / len(pass_in_class) * 100
    percent = round(percent, 2)
    print('Класс', i, ': выжило', len(surv_in_class),
          'из', len(pass_in_class), '-', percent, '%')
print()

print('3. САМОЕ ПОПУЛЯРНОЕ МУЖСКОЕ И ЖЕНСКОЕ ИМЯ НА КОРАБЛЕ')
print('----------------------------------------------------')
male_names = {}
female_names = {}
for i in range(len(df)):
    name = df.loc[i, 'Name']
    sex = df.loc[i, 'Sex']
    if '(' in name:
        first = name.split('(')[1].split(')')[0].split()[0]
    else:
        first = name.split(',')[1].split('.')[1].strip().split()[0]
    if sex == 'male':
        if first in male_names:
            male_names[first] = male_names[first] + 1
        else:
            male_names[first] = 1
    else:
        if first in female_names:
            female_names[first] = female_names[first] + 1
        else:
            female_names[first] = 1

best_male = ''
best_male_count = 0
for name in male_names:
    if male_names[name] > best_male_count:
        best_male_count = male_names[name]
        best_male = name

best_female = ''
best_female_count = 0
for name in female_names:
    if female_names[name] > best_female_count:
        best_female_count = female_names[name]
        best_female = name

print('Самое популярное мужское имя:', best_male, '-', best_male_count, 'человек')
print('Самое популярное женское имя:', best_female, '-', best_female_count, 'человек')
print()

print('4. САМОЕ ПОПУЛЯРНОЕ ИМЯ В КАЖДОМ КЛАССЕ')
print('---------------------------------------')
for i in range(1, 4):
    class_df = df[df['Pclass'] == i]
    class_df = class_df.reset_index(drop=True)
    male_names = {}
    female_names = {}
    for j in range(len(class_df)):
        name = class_df.loc[j, 'Name']
        sex = class_df.loc[j, 'Sex']
        if '(' in name:
            first = name.split('(')[1].split(')')[0].split()[0]
        else:
            first = name.split(',')[1].split('.')[1].strip().split()[0]
        if sex == 'male':
            if first in male_names:
                male_names[first] = male_names[first] + 1
            else:
                male_names[first] = 1
        else:
            if first in female_names:
                female_names[first] = female_names[first] + 1
            else:
                female_names[first] = 1

    best_male = ''
    best_male_count = 0
    for name in male_names:
        if male_names[name] > best_male_count:
            best_male_count = male_names[name]
            best_male = name

    best_female = ''
    best_female_count = 0
    for name in female_names:
        if female_names[name] > best_female_count:
            best_female_count = female_names[name]
            best_female = name

    print('Класс', i, ': мужское имя -', best_male,
          '(', best_male_count, '), женское имя -', best_female, '(', best_female_count, ')')
print()

print('5. ПАССАЖИРЫ, КОТОРЫМ БОЛЬШЕ 44 ЛЕТ')
print('------------------------------------')
print(df[df['Age'] > 44])
print()

print('6. ПАССАЖИРЫ, КОТОРЫМ МЕНЬШЕ 44 ЛЕТ И КОТОРЫЕ МУЖСКОГО ПОЛА')
print('------------------------------------------------------------')
print(df[(df['Age'] < 44) & (df['Sex'] == 'male')])
print()

print('7. КОЛИЧЕСТВО n-МЕСТНЫХ КАБИН')
print('-------------------------------')
cabins = {}
for i in range(len(df)):
    cabin = df.loc[i, 'Cabin']
    if pd.isna(cabin):
        continue
    if cabin in cabins:
        cabins[cabin] = cabins[cabin] + 1
    else:
        cabins[cabin] = 1

people_count = {}
for cabin in cabins:
    n = cabins[cabin]
    if n in people_count:
        people_count[n] = people_count[n] + 1
    else:
        people_count[n] = 1

for n in people_count:
    print('Кабин на', n, 'человек:', people_count[n])