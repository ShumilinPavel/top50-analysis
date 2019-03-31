import pandas as pd
import numpy as np


def regions_processing(df):
    regions = []

    for i in df.index:
        line = df.loc[i, 'Место']

        # Список всех различных мест по всем редакицям
        if line not in debug_affiliations:
            debug_affiliations.append(line)

        words_in_line = line.split()

        city = words_in_line[0]
        if city == 'Нижний' or city == 'Старый' or city == 'Нижегородская':
            city = city + ' ' + words_in_line[1]

        # if city not in russian_regions and city != 'не' and city != 'IT':      # Если город из СНГ, но не Россия, то регион = город
        #     regions.append(city)
        if city in city_to_region_dict.keys():
            regions.append(city_to_region_dict[city])
        else:
            regions.append('Неизвестно')

    df['Region'] = regions


def affiliations_processing(df):
    for i in df.index:
        f = True
        line = df.loc[i, 'Место'].upper()

        for affil in affiliations_to_id_dict.keys():
            if affil.upper() in line:

                affil = affiliation_unification(affil)

                df.loc[i, 'Место'] = affil
                f = False
                break
        if f:
            df.loc[i, 'Место'] = 'Не институт'

    # print(df['Место'])


def affiliation_unification(affil):
    affil_u = affil.upper()
    if affil_u == 'Ломоносов'.upper():
        return 'МГУ'
    if affil_u == 'Южно-Уральский государственный университет'.upper():
        return 'ЮУрГУ'
    if affil_u == 'Институт биоорганической химии РАН'.upper():
        return 'ИБХ РАН'
    if affil_u == 'Институт математики и механики УрО РАН'.upper():
        return 'ИММ УРО РАН'
    if affil_u == 'Институт вычислительной математики РАН'.upper():
        return 'ИВМ РАН'
    if affil_u == 'НИИ биомедицинской химии им. В.Н.Ореховича РАМН'.upper():
        return 'НИИ БМХ РАМН'
    if affil_u == 'Санкт-Петербургский политехнический университет'.upper():
        return 'СПбГПУ'
    if affil_u == 'Санкт-Перербургский государственный университет'.upper():
        return 'СПбГУ'
    if affil_u == 'ИВМиМГ'.upper() or \
        affil_u == 'ССКЦ ИВМиМГ'.upper():
        return 'ИВМиМГ СО РАН'
    if affil_u == 'НГУ'.upper():
        return 'ННГУ'
    if affil_u == 'НГУ им. Н.И.Лобачевского'.upper():
        return 'ННГУ'
    if affil_u == 'кафедра физической химии ТГУ'.upper():
        return 'ТвГУ'
    elif affil_u == 'Центр параллельных вычислений ФГУП ЦНИИ машиностроения'.upper() or \
         affil_u == 'ФГУП ЦНИИ машиностроения'.upper():
        return 'ФГУП ЦНИИмаш'
    elif affil_u == 'РНЦ «Курчатовский институт»'.upper():
        return 'РНЦ Курчатовский институт'
    elif affil_u == 'Томский государственный университет'.upper():
        return 'ТГУ'
    elif affil_u == 'Московский физико-технический институт'.upper():
        return 'МФТИ'
    elif affil_u == 'Лаборатория Информационных Технологий Объединенный Институт Ядерных Исследований'.upper():
        return 'ЛИТ ОИЯИ'
    elif affil_u == 'Томский политехнический университет'.upper():
        return 'ТПУ'
    elif affil_u == 'Ивановский государственный энергетический университет'.upper():
        return 'ИГЭУ'
    elif affil_u == 'Уфимский государственный авиационный технический университет'.upper():
        return 'УГАТУ'
    elif affil_u == 'Вятский государственный университет'.upper():
        return 'ВятГУ'
    elif affil_u == 'Новосибирский государственный университет'.upper():
        return 'НГУ'
    elif affil_u == 'Владимирский государственный университет'.upper():
        return 'ВлГУ'
    elif affil_u == 'Объединенный Институт Высоких Температур РАН'.upper():
        return 'ОИВТ РАН'
    elif affil_u == 'Институт Прикладной Механики Российской Академии Наук'.upper() or \
         affil_u == 'Институт прикладной механики УрО РАН'.upper():
        return 'ИПРИМ РАН'
    elif affil_u == 'Институт автоматики и процессов управления ДВО РАН'.upper():
        return 'ИАПУ ДВО РАН'
    elif affil_u == 'Научно-исследовательский институт эпидемиологии и ​микробиологии им. Н. Ф. Гамалеи РАМН'.upper():
        return 'НИЦЭМ им. Н.Ф. Гамалеи'
    elif affil_u == 'ФГУП "Крыловский государственный научный центр"'.upper():
        return 'ФГУП ЦНИИ Крылова'
    elif affil_u == 'Сколковский Институт Науки и Технологий'.upper():
        return 'Сколтех'
    elif affil_u == 'Нижегородский государственный университет им. Н.И. Лобачевского'.upper():
        return 'ННГУ'
    elif affil_u == 'Томский политехнический университет'.upper():
        return 'ТПУ'
    elif affil_u == 'Институт теоретической и прикладной механики им. С.А. Христиановича СО РАН'.upper():
        return 'ИТПМ СО РАН'
    elif affil_u == 'Казанский научный центр РАН'.upper():
        return 'КазНЦ РАН'
    elif affil_u == 'Вычислительный центр имени А. А. Дородницына РАН'.upper() or \
         affil_u == 'Вычислительный центр имени А.А. Дородницына РАН'.upper():
        return 'ВЦ РАН'
    elif affil_u == 'НИИ физической и органической химии РГУ'.upper() or \
         affil_u == 'ЮгИНФО РГУ'.upper() or \
         affil_u == 'Таганрогский Технологический Институт Южного Федерального Университета'.upper() or \
         affil_u == 'НИИ физической и органической химии ЮФУ'.upper():
        return 'ЮФУ'
    elif affil_u == 'Кыргизско Российский Славянский Университет'.upper():
        return 'КРСУ'
    elif affil_u == 'Пермский государственный национальный исследовательский университет'.upper():
        return 'ПГНИУ'
    elif affil_u == 'Пермский Государственный Технический Университет'.upper():
        return 'ПНИПУ'
    elif affil_u == 'Кабардино-Балкарский государственный университет им. Х.М. Бербекова'.upper():
        return 'КБГУ'
    elif affil_u == 'Московский государственный университет путей сообщения'.upper():
        return 'МГУПС'
    elif affil_u == 'Российский Государственный Университет им. Иммануила Канта'.upper():
        return 'БФУ имени И. Канта'
    elif affil_u == 'Самарский государственный аэрокосмический университет имени академика С.П.Королева'.upper():
        return 'СГАУ'
    elif affil_u == 'ФГУП ""ЦИАМ им П. И. Баранова""'.upper() or \
         'Баранов'.upper() in affil_u:
        return 'ЦИАМ им. П.И. Баранова'
    elif affil_u == 'Северо-Восточный федеральный университет имени М.К.Аммосова'.upper() or \
         affil_u == 'Якутский Государственный Университет'.upper():
        return 'СВФУ'
    elif affil_u == 'Тюменский государственный университет'.upper():
        return 'ТюмГУ'
    elif affil_u == 'Институт прикладной астрономии РАН'.upper():
        return 'ИПА РАН'
    elif affil_u == 'Волгоградский государственный технический университет'.upper():
        return 'ВолгГТУ'
    return affil


def cpu_and_cores_processing(df):
    cpu = []
    cores = []

    for i in df.index:
        line = df.loc[i, 'Кол-во CPU/ядер']
        values = line.split('/')
        cpu.append(values[0])
        cores.append(values[1])

    del df['Кол-во CPU/ядер']
    df['Cpu'] = cpu
    df['Cores'] = cores


def nodes_and_memory_processing(df):
    nodes = []
    memory = []

    for i in df.index:
        cur_line = df.loc[i, 'Архитектура(тип процессора / сеть)']
        words_in_line = cur_line.split()
        if words_in_line[0] != 'узлов:':
            nodes.append(np.nan)
            memory.append(np.nan)
            continue

        sum_of_nodes = 0
        amount_of_last_type_nodes = 0
        sum_of_memory = 0

        for j in range(len(words_in_line) - 1):
            if words_in_line[j] == 'узлов:':
                sum_of_nodes += int(words_in_line[j + 1])
                amount_of_last_type_nodes = int(words_in_line[j + 1])

            if words_in_line[j + 1] == 'GB':
                sum_of_memory += float(words_in_line[j]) * amount_of_last_type_nodes

            if words_in_line[j + 1] == 'MB':
                sum_of_memory += float(words_in_line[j]) / 1024 * amount_of_last_type_nodes

        nodes.append(sum_of_nodes)
        memory.append(sum_of_memory)

    df['Nodes'] = nodes
    df['Memory'] = memory


def nets_processing(df):
    nets = []

    for i in df.index:
        line = df.loc[i, 'Архитектура(тип процессора / сеть)']
        id_of_nets_beg = line.find('сеть: ')
        line = line[id_of_nets_beg + len('сеть: '):]
        nets_in_line = line.split('/')
        main_net = nets_in_line[0]                 # upper() но тогда все if большими буквами

        if main_net == 'Трехмерный тор 60 Gbits, макс. задержка 1 мкс, InfiniBand QDR 40 Gbits' or \
                main_net == 'ряд 4 Xeon X5680 3.33 GHz Трехмерный тор 60 Gbits, макс. задержка 1 мкс, InfiniBand QDR 40 Gbits' or \
                main_net == 'ряд 4 Intel Xeon X5570 2.93 GHz Трехмерный тор 60 Gbits, макс. задержка 1 мкс InfiniBand QDR 40 Gbits':
            main_net = 'Трехмерный тор 60 Gbits'

        if main_net == 'perDome PA-RISC 750 MHz' or \
                main_net == 'perDome PA-8600 550 MHz' or \
                main_net == 'es 690 POWER4 1.1 GHz' or \
                main_net == 'es 690 POWER4+ 1.9 GHz' or \
                main_net == 'es 670 POWER4+ 1.5 GHz' or \
                main_net == 'es 690 POWER4 1.3 GHz' or \
                main_net == 'ire 15000 UltraSPARC III 900 MHz' or \
                main_net == 'МЕР ДЮММШУ':
            nets.append(np.nan)
        else:
            nets.append(nets_to_speed_dict[main_net])

    del df['Архитектура(тип процессора / сеть)']
    df['Nets'] = nets


def linpack_and_peak_processing(df):
    linpack = []
    peak = []

    for i in df.index:
        cur_line = df.loc[i, 'Производительность Linpack Пиковая']
        values = cur_line.split()
        linpack.append(float(values[0]))
        peak.append(float(values[1]))

    del df['Производительность Linpack Пиковая']
    df['Linpack'] = linpack
    df['Peak'] = peak


def developers_processing(df):
    developer = []

    for i in df['Разработчик']:
        if developers_to_code_dict[i] == 1:
            developer.append('Foreign dev')
        if developers_to_code_dict[i] == 2:
            developer.append('Domestic dev')
        if developers_to_code_dict[i] == 3:
            developer.append('Joint dev')

    del df['Разработчик']
    df.insert(2, 'Developer', developer)
    # df['developer'] = developer


def add_statistics(df, year):
    statistics_files = ['GRPperCapita.csv']  # statistics_files = ['Average incomes per capita.csv', 'GRPperCapita.csv', 'Internal spendigns on science.csv', 'Number of scientists.csv']

    if year == '2018' or year == '2017':
        year = '2016'

    for file in statistics_files:
        df_tmp = pd.read_csv(file)
        attribute = file[:-4]       # Имя файла без расширения = имя атрибута

        if str(year) in df_tmp.columns:
            for i in df.index:
                val = df_tmp.loc[df.loc[i, 'Region'] == df_tmp['Регион'], str(year)].tolist()
                if len(val) != 0:
                    df.loc[i, attribute] = val[0]
                else:
                    df.loc[i, attribute] = np.nan
        else:
            df[attribute] = np.nan


def aggregate_by_affiliation(df):
    df_aggreg = df.groupby(['Affiliation', 'Year'], as_index=False).aggregate(sum)
    df_aggreg = df_aggreg.drop(df_aggreg[df_aggreg['Affiliation'] == 'Не институт'].index)

    num_of_systems = []
    for affil in df_aggreg['Affiliation']:
        num_of_systems.append(len(df[df['Affiliation'] == affil]))
    df_aggreg['Num of Systems'] = num_of_systems
    df_aggreg['GRPperCapita'] = df_aggreg['GRPperCapita'] / df_aggreg['Num of Systems']

    df_aggreg = df_aggreg.reset_index(drop=True)

    df_aggreg.to_csv('TEST.csv')

    return df_aggreg


def get_deciles(df, columns):
    for col in columns:
        df_tmp = df.dropna(subset=[col])
        if len(df_tmp) == 0:
            continue

        # thresholds = df_tmp[col].quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]).tolist()
        # for i in df_tmp.index:
        #     if df_tmp.loc[i, col] >= thresholds[8]:
        #         df.loc[i, col] = col + ': 1'
        #     elif df_tmp.loc[i, col] >= thresholds[7]:
        #         df.loc[i, col] = col + ': 2'
        #     elif df_tmp.loc[i, col] >= thresholds[6]:
        #         df.loc[i, col] = col + ': 3'
        #     elif df_tmp.loc[i, col] >= thresholds[5]:
        #         df.loc[i, col] = col + ': 4'
        #     elif df_tmp.loc[i, col] >= thresholds[4]:
        #         df.loc[i, col] = col + ': 5'
        #     elif df_tmp.loc[i, col] >= thresholds[3]:
        #         df.loc[i, col] = col + ': 6'
        #     elif df_tmp.loc[i, col] >= thresholds[2]:
        #         df.loc[i, col] = col + ': 7'
        #     elif df_tmp.loc[i, col] >= thresholds[1]:
        #         df.loc[i, col] = col + ': 8'
        #     elif df_tmp.loc[i, col] >= thresholds[0]:
        #         df.loc[i, col] = col + ': 9'
        #     else:
        #         df.loc[i, col] = col + ': 10'

        # th1, th2, th3 = df_tmp[col].quantile([0.49, 0.69, 0.89])
        th1, th2, th3 = df_tmp[col].quantile([0.25, 0.5, 0.75])
        for i in df_tmp.index:
            if df_tmp.loc[i, col] >= th3:
                df.loc[i, col] = col + ': 1'
            elif df_tmp.loc[i, col] >= th2:
                df.loc[i, col] = col + ': 2'
            elif df_tmp.loc[i, col] >= th1:
                df.loc[i, col] = col + ': 3'
            else:
                df.loc[i, col] = col + ': 4'


        # df[col] = pd.qcut(df_tmp[col].rank(method='first'), 10,
        #                   labels=[col + ': 10', col + ': 9', col + ': 8', col + ': 7', col + ': 6',
        #                           col + ': 5', col + ': 4', col + ': 3', col + ': 2', col + ': 1'])


top50_files = ['Top50_2004.csv', 'Top50_2005.csv', 'Top50_2006.csv',
                    'Top50_2007.csv', 'Top50_2008.csv', 'Top50_2009.csv',
                    'Top50_2010.csv', 'Top50_2011.csv', 'Top50_2012.csv',
                    'Top50_2013.csv', 'Top50_2014.csv', 'Top50_2015.csv',
                    'Top50_2016.csv', 'Top50_2017.csv', 'Top50_2018.csv']

scopus_files = ['Top50_2004_Scopus.csv', 'Top50_2005_Scopus.csv', 'Top50_2006_Scopus.csv', 'Top50_2007_Scopus.csv',
                'Top50_2008_Scopus.csv', 'Top50_2009_Scopus.csv', 'Top50_2010_Scopus.csv', 'Top50_2011_Scopus.csv',
                'Top50_2012_Scopus.csv', 'Top50_2013_Scopus.csv', 'Top50_2014_Scopus.csv', 'Top50_2015_Scopus.csv',
                'Top50_2016_Scopus.csv', 'Top50_2017_Scopus.csv', 'Top50_2018_Scopus.csv']

city_to_region_dict = {
    'Москва': 'Город Москва столица Российской Федерации город федерального значения',
    'Санкт-Петербург': 'Город Санкт-Петербург город федерального значения',
    'Нижний Новгород': 'Нижегородская область',
    'Челябинск': 'Челябинская область',
    'Гатчина': 'Ленинградская область',
    'Дубна': 'Московская область',
    'Екатеринбург': 'Свердловская область',
    'Томск': 'Томская область',
    'Иркутск': 'Иркутская область',
    'Новосибирск': 'Новосибирская область',
    'Хабаровск': 'Хабаровский край',
    'Долгопрудный': 'Московская область',
    'Минск': 'Минская область',
    'Пермь': 'Пермский край',
    'Зеленоград': 'Московская область',
    'Тюмень': 'Тюменская область',
    'Владивосток': 'Приморский край',
    'Волгоград': 'Волгоградская область',
    'Казань': 'Республика Татарстан (Татарстан)',
    'Нижегородская обл.,': 'Нижегородская область',
    'Алматы': 'Алматы',
    'Якутск': 'Республика Саха (Якутия)',
    'Белгород': 'Белгородская область',
    'Уфа': 'Республика Башкортостан',
    'Таганрог': 'Ростовская область',
    'Киров': 'Кировская область',
    'Красноярск': 'Красноярский край',
    'Рыбинск': 'Ярославская область',
    'Самара': 'Самарская область',
    'Киев': 'Киев',
    'Владимир': 'Владимирская область',
    'Калининград': 'Калининградская область',
    'Ростов-на-Дону': 'Ростовская область',
    'Черноголовка': 'Московская область',
    'Королев': 'Московская область',
    'Нальчик': 'Кабардино-Балкарская Республика',
    'Тольятти': 'Самарская область',
    'Жуковский,': 'Московская область',
    'Краснодар': 'Краснодарский край',
    'Саров': 'Нижегородская область',
    'Ереван': 'Ереван',
    'Ухта': 'Республика Коми',
    'Харьков': 'Харьковская область',
    'Львов': 'Львовская область',
    'Бугульма': 'Республика Татарстан (Татарстан)',
    'Бишкек': 'Бишкек',
    'Иваново': 'Ивановская область',
    'Снежинск': 'Челябинская область',
    'Тула': 'Тульская область',
    'Ростов': 'Ярославская область',
    'Ставрополь': 'Ставропольский край',
    'Королев,': 'Московская область',
    'Череповец': 'Волгоградская область',
    'Барнаул': 'Алтайский край',
    'Ижевск': 'Удмуртская Республика',
    'Переславль-Залесский': 'Ярославская область',
    'Старый Оскол': 'Белгородская область',
    'Троицк': 'Московская область',
    'Ханты-Мансийск': 'Ханты-Мансийский автономный округ - Югра (Тюменская область)',
    'Тверь': 'Тверская область'
}

nets_to_speed_dict = {
    '10 Gigabit Ethernet': 10,
    'Gigabit Ethernet': 1,
    'InfiniBand': 2.5,
    'Infiniband 4x DDR': 20,
    'Infiniband EDR': 103.125,
    'InfiniBand EDR': 103.125,
    'Infiniband FDR': 56.25,
    'Infiniband QDR': 10,
    'OmniPath': 100,
    'Трехмерный тор 60 Gbits': 60,
    'Aries': 20,
    'Aries + Infiniband': 20,
    'Aries + Gigabit Ethernet': 10,
    'Fast Ethernet': 0.1,
    0: 0,
    '2xGigabit Ethernet': 2,
    '10 Gigabit Ethernet Copper': 10,
    'I2C-IPMI': 0.0034,
    '"МВС-экспресс"': 32,
    "Gene": 10,
    'Infiniband FDR-10': 40,
    'NUMALink': 6.4,
    'Myrinet': 2,
    'QLogic InfiniPath': 10,
    'HyperPlex': 10,
    'Myrinet 2000': 2,
    'SCI': 0.667,
    'QsNet, InfiniBand, BULL FAME NUMA intercnection': 0.9,
    'Infiniband (PCI-Express)': 2.5,
    'NUMAlink4': 6.4,
    'Ангара': 10
}

developers_to_code_dict = {
    'Т-Платформы': 2,
    'Группа компаний РСК': 2,
    'T-Платформы, CRAY': 3,
    'НИЦ "Курчатовский Институт", Supermicro, Борлас, Т-Платформы': 3,
    'Ниагара Компьютерс': 2,
    'NP-IT, Ниагара компьютерс': 3,
    'Hewlett-Packard': 1,
    'NVIDIA, IBS Platformix': 1,
    'Intel': 1,
    'Hewlett Packard, Открытые технологии': 3,
    'группа компаний РСК': 2,
    'Т-Платформы, Ай-Теко': 2,
    'Hewlett Packard': 1,
    'NVIDIA': 1,
    'Т-Платформы, Ниагара Компьютерс': 2,
    'Hewlett Packard Enterprise': 1,
    'IBM/Lenovo': 1,
    'Hewlett-Packard, Dell, Sky Technics Group': 1,
    'IBM': 1,
    'Нэтберг': 2,
    'iRU': 2,
    'SuperMicro, Борлас': 3,
    'СКИФ': 2,
    'ИПМ им. М.В.Келдыша РАН, ООО НПО "Роста", ФГУП "НИИ "КВАНТ"': 2,
    'Ситоника': 2,
    'ВолгГТУ, Ниагара компьютерс, Группа компаний РСК': 2,
    'Hewlett-Packard, Нонолет': 3,
    'ООО Градиент технолоджи, НИИСИ РАН, НТФ Байко': 2,
    'ООО "ЦКО"': 2,
    'Fujitsu': 1,
    'Группа компаний РСК, Аквариус, Сканер': 2,
    'Ниагара Компьютерс, Supermicro': 3,
    'Hewlett-Packard, INLINE Group': 3,
    'IBM, ООО Технический центр ГАРМОНИЯ': 3,
    'Hewlett Packard, Нонолет': 3,
    'Hewlett Packard / КРОК': 3,
    'SGI': 1,
    'IBM, ООО "Технический центр "ГАРМОНИЯ"': 3,
    'Hewlett Packard / Открытые технологии': 3,
    'Hewlett-Packard, Открытые технологии': 3,
    'ОАО Т-Платформы': 2,
    'АйТи/IBM': 3,
    'РСК': 2,
    'IBM/Крок': 3,
    'РСК СКИФ': 2,
    'Hewlett-Packard Нонолет': 3,
    'ОИПИ НАН Беларуси, УП "НИИЭВМ"': 2,
    'ПНВП "ЮСТАР"': 2,
    'ИК НАН Украины, Энтри, Фолгат ФТС, Медиа Меджик': 2,
    'Hewlett-Packard,'
    'Институт системного программирования РАН (ИСП РАН)': 3,
    'СКИФ-ГРИД (ОИПИ НАН Беларуси, УП "НИИЭВМ", Т-Платформы)': 2,
    'Fujitsu Siemens/ДВ.ком': 3,
    'ЕТегро Текнолоджис': 2,
    'ДАТА Технологии, Троник, ССТ': 3,
    'ОАО "Т-Платформы" / ОАО "Депо Компьютерс"': 2,
    'Т-Платформы, SuperMicro': 3,
    'Supermicro/Ниагара': 3,
    'Sun Microsystems Jet Infosystems': 1,
    'HP/ЗАО "Открытые Технологии 98" "Открытые Технологии -Пермь"': 2,
    'IBM/Техносерв': 3,
    'SGI/Ай-Теко, Арбайт': 3,
    'ОАО "Т-Платформы"': 2,
    'ООО Модуль-Проекты': 2,
    'ФГУП "Квант", ИПМ РАН, МСЦ': 2,
    'FujitsuSiemens/T-Платформы': 3,
    'ИДСТУ СО РАН': 2,
    'Kraftway/АйТи': 2,
    'IBM/КРОК': 3,
    'Институт системного программирования (ИСП РАН)': 2,
    'ИПИА НАН РА, ИСП РАН, C.I.Technology': 3,
    'Kraftway Corporation Pls.': 2,
    'ИММ УрО РАН': 2,
    'IBM/Verysel-проекты': 3,
    'Институт кибернетики НАН Украины, Энтри, Фолгат FTC': 2,
    'ЗАО Крафтвэй корпорэйшн ПЛС, собственная сборка на платформе Bull': 2,
    'IBM/X-COM': 3,
    'ПНВП "ЮСТАР"/Медия-Мэджик': 2,
    'IBM/ROY Int': 1,
    'IBM/Inline': 3,
    'ИК НАН Украины / ПНВП "ЮСТАР" г. Киев': 2,
    'Собственная сборка': 2,
    'СКИФ, ОАО ”НИЦЭВТ”': 2,
    'Т-Платформы, Sun Microsystems': 3,
    'Институт Кибернетики НАН Украины, ЮСТАР (г. Киев), Т-Платформы (г. Москва)': 2,
    'ДАТА Технологии': 2,
    'IBM/BCC': 3,
    'ООО "ДАТА Технологии" (поставщик)': 2,
    'Кафедра "Компьютерные технологии в машиностроении" СПбГПУ': 2,
    'Институт Кибернетики НАН Украины': 2,
    'ООО "Крафтвей компьютерс", собственная сборка(на базе платформы SGI)': 2,
    'IBM/KPBS': 3,
    'Hewlett-Packard / Ай-Теко': 3,
    'Aquarius/OLLY': 2,
    'ФГУП "Квант"': 2,
    'ИСП РАН, C.I.Technology': 3,
    'Hewlett-Packard, Ай-Теко': 3,
    'ИК НАНУ, ПНВП "ЮСТАР"': 2,
    'НИИМех МГУ, СКИФ': 2,
    'SUN Microsystems': 1,
    'DELL': 1,
    'ОИПИ НАН Беларуси': 2,
    'АО "НИЦЭВТ", Ниагара компьютерс': 2,
    'Hewlett-Packard, Институт системного программирования РАН (ИСП РАН)': 3
}
# Возможны одинаковые id надо сделать одно имя им
affiliations_to_id_dict = {
    'МГУ': '60007457',
    'Ломоносов': '60007457',
    # 'Московский государственный университет имени М.В. Ломоносова': '60007457',
    'Южно-Уральский государственный университет': '60008009',
    'ЮУрГУ': '60008009',
    'Институт биоорганической химии РАН': '60085212',
    'ИБХ РАН': '60085212',
    'Институт математики и механики УрО РАН': '60020267',
    'ИММ УРО РАН': '60020267',
    'Институт вычислительной математики РАН': '60109781',
    'ИВМ РАН': '60109781',
    'Вычислительный центр имени А.А. Дородницына РАН': '60003168',
    'ИПС РАН': '60099167',
    'НИИ биомедицинской химии им. В.Н.Ореховича РАМН': '60069638',
    'НИИ БМХ РАМН': '60069638',
    'НИИ физической и органической химии РГУ': '60025383',
    'ЮгИНФО РГУ': '60025383',
    'ЮФУ': '60025383',
    'Таганрогский Технологический Институт Южного Федерального Университета': '60025383',
    'СПбГПУ': '60017103',
    'Санкт-Петербургский политехнический университет': '60017103',
    'Санкт-Перербургский государственный университет': '60031888',
    'СПбГУ': '60031888',
    'КГУ': '60020189',
    'ИВМиМГ СО РАН': '60025485',
    'ИВМиМГ': '60025485',
    'КГПУ': '60110152',
    'НГУ им. Н.И.Лобачевского': '60008673',
    'Нижегородский государственный университет им. Н.И. Лобачевского': '60008673',
    'ННГУ': '60008673',
    'кафедра физической химии ТГУ': '60016896',
    'Томский государственный университет': '60016896',
    'ТГУ': '60016896',
    'ИПХФ РАН': '60007728',
    'ИММ РАН': '60101966',
    'Казанский научный центр РАН': '60096198',
    'Кыргизско Российский Славянский Университет': '60072554',
    'Якутский Государственный Университет': '60013628',
    'Северо-Восточный федеральный университет имени М.К.Аммосова': '60013628',
    'Центр параллельных вычислений ФГУП ЦНИИ машиностроения': '60032468',
    'ФГУП ЦНИИ машиностроения': '60032468',
    # 'РНЦ «Курчатовский институт»': '60020943',
    # 'РНЦ Курчатовский институт': '60020943',
    # 'НИЦ "Курчатовский институт"': '60020943',
    'Курчатовский институт': '60020943',
    #'МСЦ РАН': '',
    #'Межведомственный суперкомьютерный центр Российская академия наук': '',
    'МФТИ': '60000308',
    'Московский физико-технический институт': '60000308',
    'Лаборатория Информационных Технологий Объединенный Институт Ядерных Исследований': '60004764',
    'ЛИТ ОИЯИ': '60004764',
    'Томский политехнический университет': '60024069',
    'ТПУ': '60024069',
    'ИСП РАН': '60028621',
    'Ивановский государственный энергетический университет': '60008036',
    'ИГЭУ': '60008036',
    'Уфимский государственный авиационный технический университет': '60001458',
    'УГАТУ': '60001458',
    'СФУ': '60075346',
    'Вятский государственный университет': '60104421',
    'Новосибирский государственный университет': '60002049',
    'Владимирский государственный университет': '60020886',
    'Пермский Государственный Технический Университет': '60023325',
    'Объединенный Институт Высоких Температур РАН': '60017889',
    'ОИВТ РАН': '60017889',
    'Институт Прикладной Механики Российской Академии Наук': '60109783',
    'Институт прикладной механики УрО РАН': '60109783',
    'ИПРИМ РАН': '60109783',
    'Институт теоретической и прикладной механики им. С.А. Христиановича СО РАН': '60103861',
    'ИТПМ СО РАН': '60103861',
    'ИДСТУ СО РАН': '60010545',
    'Институт автоматики и процессов управления ДВО РАН': '60011843',
    'ИАПУ ДВО РАН': '60011843',
    'МИЭТ': '60001037',
    'Научно-исследовательский институт эпидемиологии и ​микробиологии им. Н. Ф. Гамалеи РАМН': '60069621',
    'НИЦЭМ им. Н. Ф. Гамалеи': '60069621',
    'Московский государственный университет путей сообщения': '60018918',
    'Российский Государственный Университет им. Иммануила Канта': '60031254',
    'МГТУ им. Н. Э.Баумана': '60033469',
    'Кабардино-Балкарский государственный университет им. Х.М. Бербекова': '60015519',
    'РГУ им. Губкина': '60010055',
    'Самарский государственный аэрокосмический университет имени академика С.П.Королева': '60011415',
    'ФГУП "ЦИАМ им П. И. Баранова"': '60070982',
    'МАИ': '60069256',
    'ФГУП НИИР': '60027587',
    'ИПМ им. М.В.Келдыша РАН': '60010862',
    'ИЦиГ СО РАН': '60068684',
    'Тюменский государственный университет': '60009789',
    'ФГУП ЦНИИ Крылова': '60029012',
    'ФГУП "Крыловский государственный научный центр"': '60029012',
    'Пермский государственный национальный исследовательский университет': '60023914',
    'Институт прикладной астрономии РАН': '60109931',
    'МИСиС': '60068681',
    'Сколковский Институт Науки и Технологий': '60107405',
    'Сколтех': '60107405',
    'Волгоградский государственный технический университет': '60029073',
    #'Западно-Сибирское управление по гидрометеорологии и мониторингу окружающей среды': '',
    #'Дальневосточное управление по гидрометеорологии и мониторингу окружающей среды': '',
}

# russian_regions = [
    #     'Москва',
    #     'Санкт-Петербург',
    #     'Нижний Новгород',
    #     'Челябинск',
    #     'Гатчина',
    #     'Дубна',
    #     'Екатеринбург',
    #     'Томск',
    #     'Иркутск',
    #     'Новосибирск',
    #     'Хабаровск',
    #     'Долгопрудный',
    #     'Пермь',
    #     'Зеленоград',
    #     'Тюмень',
    #     'Владивосток',
    #     'Волгоград',
    #     'Казань',
    #     'Нижегородская обл.,',
    #     'Якутск',
    #     'Белгород',
    #     'Уфа',
    #     'Таганрог',
    #     'Киров',
    #     'Красноярск',
    #     'Рыбинск',
    #     'Самара',
    #     'Владимир',
    #     'Калининград',
    #     'Ростов-на-Дону',
    #     'Черноголовка',
    #     'Королев',
    #     'Нальчик',
    #     'Тольятти',
    #     'Жуковский,',
    #     'Краснодар',
    #     'Саров',
    #     'Ухта',
    #     'Бугульма',
    #     'Иваново',
    #     'Снежинск',
    #     'Тула',
    #     'Ростов',
    #     'Ставрополь',
    #     'Королев',
    #     'Череповец',
    #     'Барнаул',
    #     'Ижевск',
    #     'Переславль-Залесский',
    #     'Старый Оскол',
    #     'Троицк',
    #     'Ханты-Мансийск',
    #     'Тверь'
    # ]


def main():
    df_total = pd.DataFrame()
    scopus_file_id = 0

    for file in top50_files:
        df = pd.read_csv(file)

        df = df.dropna()
        del df['N']

        regions_processing(df)

        affiliations_processing(df)

        year = file[6:10]
        df['Year'] = year

        cpu_and_cores_processing(df)

        nodes_and_memory_processing(df)

        nets_processing(df)

        linpack_and_peak_processing(df)

        # developers_processing(df)

        df['Cpu'] = df['Cpu'].astype('float')
        df['Cores'] = df['Cores'].astype('float')
        df['Nodes'] = df['Nodes'].astype('float')
        df['Region'] = df['Region'].astype('str')
        # df['Developer'] = df['Developer'].astype('str')

        add_statistics(df, year)

        df.rename(columns={'Место': 'Affiliation'}, inplace=True)

        df = aggregate_by_affiliation(df)

        # df.to_csv('Top50_' + year + '_Result.csv')

        df_scopus = pd.read_csv(scopus_files[scopus_file_id], index_col=0)
        scopus_file_id += 1
        df['Year'] = df['Year'].astype('str')
        df_scopus['Year'] = df_scopus['Year'].astype('str')
        df = pd.merge(df, df_scopus)
        # df = df.merge(df_scopus)

        get_deciles(df, ['Cpu', 'Cores', 'Nodes', 'Memory', 'Nets',
                         'Linpack', 'Peak', 'GRPperCapita', 'Num of Systems',
                         'Q1', 'Q2', 'Q3', 'Q4', 'Top10'])

        df_total = pd.concat([df_total, df], ignore_index=True)

    df_total.to_csv('Top50_FINAL_4equalQuartiles.csv')

    # for e in debug_affiliations:
    #     print(e)

#===================
# Старт программы
#===================
if __name__ == '__main__':
    debug_affiliations = []
    main()