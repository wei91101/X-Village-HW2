import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

url = 'http://data.coa.gov.tw/Service/OpenData/DataFileService.aspx?UnitId=378'
response = requests.get(url)

f = open('fram_yeild.json', 'w', encoding = 'utf-8')
f.write(response.text)
j = json.loads(response.text)
# print(type(j))

l_year = []
l_permoney = []
l_money = []
l_weight = []
p_year = []
p_permoney = []
p_money = []
pi_year = []
pi_permoney = []
pi_money = []

for i in range (len(j)):
    if (j[i]['作物名稱'] == '檸檬'):
        l_year.append(j[i]['年度'])
        l_permoney.append(j[i]['單價'])
        l_money.append(j[i]['產值'])
        l_weight.append(j[i]['產量'])
        #print(j[i])

for i in range (len(j)):
    if (j[i]['作物名稱'] == '李'):
        p_year.append(j[i]['年度'])
        p_permoney.append(j[i]['單價'])
        p_money.append(j[i]['產值'])
        #print(j[i])

for i in range (len(j)):
    if (j[i]['作物名稱'] == '枇杷'):
        pi_year.append(j[i]['年度'])
        pi_permoney.append(j[i]['單價'])
        pi_money.append(j[i]['產值'])  
        #print(j[i])

# print(l_year)
# print(l_permoney)
# print(l_money)
# print(p_year)
# print(p_permoney)
# print(p_money)
# print(pi_year)
# print(pi_permoney)
# print(pi_money)
l_year.reverse()
l_permoney.reverse()
l_money.reverse()
l_weight.reverse()
p_year.reverse()
p_permoney.reverse()
p_money.reverse()
pi_year.reverse()
pi_permoney.reverse()
pi_money.reverse()
#print(type(l_permoney))
for i in range (len(l_permoney)):
    l_permoney[i] = float(l_permoney[i])
    l_money[i] = float(l_money[i])
    l_weight[i] = float(l_weight[i])
    p_permoney[i] = float(p_permoney[i])
    p_money[i] = float(p_money[i])
    pi_permoney[i] = float(pi_permoney[i])
    pi_money[i] = float(pi_money[i])
# for data in range l_permoney:
#     print(data)

f = open('all_weather.json', 'r', encoding='utf-8')
j = json.loads(f.read())

Taizhong_per_place_tem = []
# Hengchun_per_place_tem = []
Taizhong_per_place_drop = []
# Hengchun_per_place_drop = []
Taizhong_per_place_drop_day = []
Taizhong_per_place_sunnyhour = []
Taizhong_per_place_wet = []

# print(j)

for w in range (0,8):
    avg_tem = [0] * 28
    avg_drop = [0] * 28
    avg_drop_day = [0] * 28
    avg_sunnyhour = [0] * 28
    avg_wet = [0] * 28
    for i in range (0 + 12 * w, 12 + 12 * w):
        #print(j[0]["cwbopendata"]["dataset"]["time"][i]["dataTime"])
        for k in range (28):
            if(j[0]["cwbopendata"]["dataset"]["time"][i]["dataTime"] == '2013-05'):
                continue
            if(j[0]["cwbopendata"]["dataset"]["time"][i]["dataTime"] == '2014-11'):
                continue
            #print(j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["locationName"])
            #print(j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][0]["elementValue"]["value"])
            j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][0]["elementValue"]["value"] = float(j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][0]["elementValue"]["value"])
            avg_tem[k] += j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][0]["elementValue"]["value"]
            if(j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][5]["elementValue"]["value"] == 'T'):
                continue
            else:
                j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][5]["elementValue"]["value"] = float(j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][5]["elementValue"]["value"])
                avg_drop[k] += j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][5]["elementValue"]["value"]       
            # print(j[0]["cwbopendata"]["dataset"]["time"][i]["location"][0]["weatherElement"][k]["elementValue"]["value"])
            j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][17]["elementValue"]["value"] = float(j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][17]["elementValue"]["value"])
            avg_sunnyhour[k] += j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][17]["elementValue"]["value"]
        # print(avg_sunnyhour)
            j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][16]["elementValue"]["value"] = float(j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][16]["elementValue"]["value"])
            avg_drop_day[k] += j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][16]["elementValue"]["value"]
            # print(avg_drop_day)
            j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][12]["elementValue"]["value"] = float(j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][12]["elementValue"]["value"])
            avg_wet[k] += j[0]["cwbopendata"]["dataset"]["time"][i]["location"][k]["weatherElement"][12]["elementValue"]["value"]
    for z in range (len(avg_tem)):
        avg_tem[z] = avg_tem[z] / 12
        avg_drop[z] = avg_drop[z] / 12
        avg_sunnyhour[z] = avg_sunnyhour[z] / 12
        avg_drop_day[z] = avg_drop_day[z] / 12
        avg_wet[z] = avg_wet[z] / 12
        if (z == 21):           # 台中
            Taizhong_per_place_tem.append(avg_tem[z])
            Taizhong_per_place_drop.append(avg_drop[z])
            Taizhong_per_place_sunnyhour.append(avg_sunnyhour[z])
            Taizhong_per_place_drop_day.append(avg_drop_day[z])
            Taizhong_per_place_wet.append(avg_wet[z])
        # if (z == 24):           # 恆春
        #     Hengchun_per_place_tem.append(avg_tem[z])
        #     Hengchun_per_place_drop.append(avg_drop[z])
Taizhong_per_place_tem[4] = Taizhong_per_place_tem[4] * 12 / 11         #修復資料缺失
#Hengchun_per_place_tem[4] = Hengchun_per_place_tem[4] * 12 / 11         #修復資料缺失
Taizhong_per_place_tem[5] = Taizhong_per_place_tem[5] * 12 / 11         #修復資料缺失
#Hengchun_per_place_tem[5] = Hengchun_per_place_tem[5] * 12 / 11         #修復資料缺失
Taizhong_per_place_drop[4] = Taizhong_per_place_drop[4] * 12 / 11         #修復資料缺失
#Hengchun_per_place_drop[4] = Hengchun_per_place_drop[4] * 12 / 11         #修復資料缺失
Taizhong_per_place_drop[5] = Taizhong_per_place_drop[5] * 12 / 11         #修復資料缺失
#Hengchun_per_place_drop[5] = Hengchun_per_place_drop[5] * 12 / 11         #修復資料缺失
Taizhong_per_place_sunnyhour[4] = Taizhong_per_place_sunnyhour[4] * 12 / 11
Taizhong_per_place_sunnyhour[5] = Taizhong_per_place_sunnyhour[5] * 12 / 11
Taizhong_per_place_drop[4] = Taizhong_per_place_drop[4] * 12 / 11
Taizhong_per_place_drop[5] = Taizhong_per_place_drop[5] * 12 / 11
Taizhong_per_place_wet[4] = Taizhong_per_place_wet[4] * 12 / 11
Taizhong_per_place_wet[5] = Taizhong_per_place_wet[5] * 12 / 11
# print(type(Hengchun_per_place_tem[4]))
# print(Taizhong_per_place_tem)
# #print(Hengchun_per_place_tem)
# print(Taizhong_per_place_drop)
# #print(Hengchun_per_place_drop)
# print(Taizhong_per_place_sunnyhour)
# print(Taizhong_per_place_drop_day)
# print(Taizhong_per_place_wet)
table = []
table.append(l_money[4:12])
table.append(l_permoney[4:12])
table.append(l_weight[4:12])
table.append(Taizhong_per_place_tem)
table.append(Taizhong_per_place_drop)
table.append(Taizhong_per_place_drop_day)
table.append(Taizhong_per_place_sunnyhour)
table.append(Taizhong_per_place_wet)
data = pd.DataFrame(table, index = ['Money', 'Per_money', 'yeild', 'Temperature', 'Drop', 'Drop_day', 'Sunnyhour', 'Wet'], columns = ['98' ,'99' , '100', '101', '102', '103', '104', '105'])
print(data)
print(data.T.corr())
# plt.figure(figsize=(10,2))
# plt.scatter(l_year[4:12],l_permoney[4:12], s=30, c='red', marker='<')
# plt.plot(l_year[4:12], l_permoney[4:12], color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('permoney')
# plt.title('Lemon Connection With Year & permoney')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(l_year[4:12],l_money[4:12], s=30, c='red', marker='<')
# plt.plot(l_year[4:12], l_money[4:12], color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('money')
# plt.title('Lemon Connection With Year & money')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(l_year[4:12],l_weight[4:12], s=30, c='red', marker='<')
# plt.plot(l_year[4:12], l_weight[4:12], color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('yeild')
# plt.title('Lemon Connection With Year & Yeild')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(l_year[4:12],Taizhong_per_place_tem, s=30, c='red', marker='<')
# plt.plot(l_year[4:12], Taizhong_per_place_tem, color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('Temperature')
# plt.title('Lemon Connection With Year & Taizhong_Temperature')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(l_year[4:12],Taizhong_per_place_drop, s=30, c='red', marker='<')
# plt.plot(l_year[4:12], Taizhong_per_place_drop, color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('Drop')
# plt.title('Lemon Connection With Year & Taizhong_Drop')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(l_year[4:12],Taizhong_per_place_drop_day, s=30, c='red', marker='<')
# plt.plot(l_year[4:12], Taizhong_per_place_drop_day, color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('Drop_day')
# plt.title('Lemon Connection With Year & Taizhong_Drop_day')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(l_year[4:12],Taizhong_per_place_sunnyhour, s=30, c='red', marker='<')
# plt.plot(l_year[4:12], Taizhong_per_place_sunnyhour, color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('Sunnyhour')
# plt.title('Lemon Connection With Year & Taizhong_Sunnyhour')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(l_year[4:12],Taizhong_per_place_wet, s=30, c='red', marker='<')
# plt.plot(l_year[4:12], Taizhong_per_place_wet, color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('Wet')
# plt.title('Lemon Connection With Year & Taizhong_Wet')
# plt.show()



# plt.figure(figsize=(10,2))
# plt.scatter(p_year,p_permoney, s=30, c='red', marker='<')
# plt.plot(p_year, p_permoney, color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('permoney')
# plt.title('Connection With Year & permoney')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(p_year,p_money, s=30, c='red', marker='<')
# plt.plot(p_year, p_money, color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('money')
# plt.title('Connection With Year & money')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(pi_year,pi_permoney, s=30, c='red', marker='<')
# plt.plot(pi_year, pi_permoney, color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('permoney')
# plt.title('Connection With Year & permoney')
# plt.show()
# plt.figure(figsize=(10,2))
# plt.scatter(pi_year,pi_money, s=30, c='red', marker='<')
# plt.plot(pi_year, pi_money, color='blue', linewidth=2.0, linestyle=':')
# plt.xlabel('year')
# plt.ylabel('money')
# plt.title('Connection With Year & money')
# plt.show()

