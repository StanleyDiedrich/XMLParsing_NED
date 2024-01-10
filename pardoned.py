
from bs4 import BeautifulSoup
import lxml
import pandas as pd
dlist=[]
file1 = '/Users/stanislavdidenko/PycharmProjects/pythonProject2/.venv/p1.xml'
file2 ='/Users/stanislavdidenko/PycharmProjects/pythonProject2/.venv/v1.xml'

itemdatas=[]

with open (file1, 'r') as file:
    soup=BeautifulSoup(file,'lxml').find_all('item')

    for i in soup:
        try:
            name = i.find('name').text
            flowwork = i.find('flowwork').text
            pressurework = i.find('pressurework').text
            revnominalmotor = i.find('revnominalmotor').text
            ifrequency = i.find('ifrequency').text
            nominalpower = i.find('nominalpower').text
            tglycolinflow = i.find('tglycolinflow').text
            tglycoloutflow = i.find('tglycoloutflow').text
            qneed= i.find('qneed').text
            if 'Гликолевый' in name:
                 glneed= i.find('qneed').text
            else:
                glneed=i.find('qneed').find_next('qneed').text
            glycoldp = i.find('glycoldp').text
            tinairinflow = i.find('tinairinflow').text
            toutairoutflow = i.find('toutairoutflow').text
            droppressurewater = i.find('droppressurewater').text
            # toutoutinflow= i.find('toutoutinflow').text
            # toutinflow=i.find('toutinflow').text
            # flowinflow=i.find('flowinflow').text


            data = [ flowwork, pressurework, nominalpower, revnominalmotor, tglycolinflow, tglycoloutflow,qneed,
                     glycoldp, tinairinflow,\
                    toutairoutflow,glneed, droppressurewater]
            # data2 = [flowinflow,pressurework,nominalpower,\
            #          revnominalmotor,toutairoutflow,toutinflow,\
            #         toutoutinflow,qneed,glycoldp]

        except:
            continue
        itemdatas.append(data)



        # columns=['flowwork', 'pressurework', 'nominalpower', 'revnominalmotor', 'tglycolinflow', 'tglycoloutflow','qneed',
        #                  'glycoldp', 'tinairinflow',\
        #                 'toutairoutflow','glneed', 'droppressurewater']
    df =pd.DataFrame(data = itemdatas)


    df.to_csv('dfres.csv', index=False,sep=";")



#     consolidatename = soup.find('consolidateddata').text.split('\n')[0]
#     for item in items:
#         try:
#             name = item.find('name').text
#             if 'Нагревание' in name:
#                 data = tinairinflow, toutairoutflow, droppressurewater, qneed
#                 waterheater.append(data)
#
#             elif 'Гликолевый' in name:
#                 data = tglycolinflow, tglycoloutflow, gneed, glycoldp
#                 watercooler.append(data)
#
#             elif 'Вентилятор' in name:
#                 data = flowwork, pressurework, revnominalmotor, ifrequency, nominalpower
#                 ventilator.append(data)
#             tinairinflow=item.find('tinairinflow').text
#             toutairoutflow=item.find('toutairoutflow').text
#             droppressurewater=item.find('droppressurewater').text
#             qneed=item.findall('qneed').text
#             for qn in qneed:
#                 print(qn)
#
#             qneedglyc=item.find('qneed').text
#             toutinflow=item.find('toutinflow').text
#             glycoldp=item.find('glycoldp').text
#             tglycolinflow=item.find('tglycolinflow').text
#             tglycoloutflow=item.find('tglycoloutflow').text
#             kpd=item.find('kpd').text
#             pressurework=item.find('pressurework').text
#             flowwork=item.find('flowwork').text
#             revnominalmotor=item.find('revnominalmotor').text
#             ifrequency=item.find('ifrequency').text
#             nominalpower=item.find('nominalpower').text
#             amperage=item.find('amperage').text
#
#
#         except:
#             continue
#
# print(waterheater)
# print(watercooler)
# print(ventilator)









    # names = [ x.text for x in soup.findAll('name')]
    # tinairinflows=[x.text for x in soup.findAll('tinairinflow')] #Гликолевый рекуператор
    # toutairoutflows=[x.text for x in soup.findAll('toutairoutflow')]#Гликолевый рекуператор
    # droppressurewaters=[x.text for x in soup.findAll('droppressurewater')]#Перепад давления в калорифере
    # qneeds=[x.text for x in soup.findAll('qneed')] #Нагреватель или охладитель
    #
    # toutinflows=[x.text for x in soup.findAll('toutinflow')]#Температура входящая входного воздуха
    # toutoutflows=[x.text for x in soup.findAll('toutoutflow')]#Температура выходящая входного воздуха
    # glycoldps = [x.text for x in soup.findAll('glycoldp')]  # Перепад давления в рекуператоре
    # tglycolinflows=[x.text for x in soup.findAll('tglycolinflow')]#Температура гликоля на входе
    # tglycoloutflows=[x.text for x in soup.findAll('tglycoloutflow')]#Температура гликоля на выходе
    # kpds=[x.text for x in soup.findAll('kpd')]#КПД рекуператора
    #
    # pressureworks=[x.text for x in soup.findAll('pressurework')] #Давление вентилятора
    # flowworks=[x.text for x in soup.findAll('flowwork')]#расход воздуха в вентиляторе
    # revnominalmotors=[x.text for x in soup.findAll('revnominalmotor')] #номинальные обороты двигателя
    # ifrequencys=[x.text for x in soup.findAll('ifrequency')] #частота электричества
    # nominalpowers=[x.text for x in soup.findAll('nominalpower')]#Номинальная мощность двигателя
    # #amperages =[x.text for x in soup.findAll('amperage')]#Сила тока
    #
    # print (names)
    # print(flowworks)
    # print(pressureworks)
    # print(nominalpowers)
    # print(revnominalmotors)
    # print (tinairinflows)
    # print (toutairoutflows)
    # print(qneeds)
    # print (droppressurewaters)
    # print (glycoldps)

    # for item in soup.find_all('item'):
    #     for name, tinairinflow,toutairoutflow,toutairoutflow,qneed,glycoldp,pressurework,flowwork,revnominalmotor,\
    #         ifrequency,nominalpower in zip(names, tinairinflows,toutairoutflows,toutairoutflows,qneeds,glycoldps,pressureworks,flowworks,revnominalmotors,\
    #         ifrequencys,nominalpowers):
    #         data = [name, tinairinflow,toutairoutflow,toutairoutflow,qneed,glycoldp,pressurework,flowwork,revnominalmotor,\
    #         ifrequency,nominalpower]
    #         print(data)









