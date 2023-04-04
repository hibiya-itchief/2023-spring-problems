import itertools
from math import sqrt

dinner_time=240 # 分後までに夕食を食べないとお腹が空いてしまう
speed=12 # 分/km

#座標(km),滞在時間(分)
yobikou=[
    {"name":"restaurant","x":5,"y":5,"time":20},
    {"name":"kawai","x":3,"y":4,"time":30},
    {"name":"testu","x":4,"y":2,"time":100},
    {"name":"sundai","x":3,"y":1,"time":60},
    {"name":"zkai","x":1,"y":2,"time":120},
    {"name":"tousnin","x":0,"y":5,"time":50}]


all_routes=itertools.permutations(yobikou)

min_time=float("inf")
min_route=[]

for route in all_routes:
    time=0
    for i in range(len(route)):
        if i==0: # スタートは(0,0)から
            dist=sqrt((route[i]["x"])**2+(route[i]["y"])**2)
        else:
            dist=sqrt((route[i]["x"]-route[i-1]["x"])**2+(route[i]["y"]-route[i-1]["y"])**2)
        time+=dist*speed
        if(route[i]["name"]=="restaurant" and time>dinner_time):
            time=float("inf")
            break
        time+=route[i]["time"]
    time+=sqrt((route[len(route)-1]["x"])**2+(route[len(route)-1]["y"])**2) # ゴールは(0,0)に戻る

    if time!=float("inf") and time<min_time:
        min_time=time
        min_route=[]
        min_route.append(route)
    elif time!=float("inf") and time==min_time:
        min_route.append(route)

print("min_cost: ",min_time,"分")
print("最短経路は",len(min_route),"個見つかりました")

for route in min_route:
    time=0
    for i in range(len(list(route))):
        if i==0:
            dist=sqrt((route[i]["x"])**2+(route[i]["y"])**2)
        else:
            dist=sqrt((route[i]["x"]-route[i-1]["x"])**2+(route[i]["y"]-route[i-1]["y"])**2)
        print("(",route[i]["x"],",",route[i]["y"],")に移動")
        print("移動時間:",dist*speed,"分")
        time+=dist*speed
        if(route[i]["name"]=="restaurant" and time>dinner_time):
            print("お腹が空いて力が出ない...")
            time=float("inf")
            break
        print(route[i]["name"]," 滞在時間:",route[i]["time"],"分")
        time+=route[i]["time"]
    time+=sqrt((route[len(route)-1]["x"])**2+(route[len(route)-1]["y"])**2)
    print("cost: ",time,"分")
