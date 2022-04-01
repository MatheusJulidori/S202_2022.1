import pymongo
import threading
import time
import random


#Conexao com mongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['bancoiot']
sensores = db.sensores




def thread1():
    temp = random.randint(30,40)
    

    result = sensores.find_one({"nomeSensor":"Temp1"})
    if(result is not None):
        if(result["sensorAlarmado"] == False):
            print("Temperatura sensor 1:"+str(temp))
            sensores.update_one({"nomeSensor":"Temp1"},{"$set":{"valorSensor":temp}})
            if(temp>=38):
                sensores.update_one({"nomeSensor":"Temp1"},{"$set":{"sensorAlarmado":True}})
        else:
            print("Atenção! Temperatura muito alta! Verificar Sensor Temp1!")
    else:
        data = {
            "nomeSensor":"Temp1",
            "valorSensor":temp,
            "unidadeMedida":"°C",
            "sensorAlarmado":False
        }
        sensores.insert_one(data)
    time.sleep(3)

    
def thread2():
    temp = random.randint(30,40)
    

    result = sensores.find_one({"nomeSensor":"Temp2"})
    if(result is not None):
        if(result["sensorAlarmado"] == False):
            print("Temperatura sensor 2:"+str(temp))
            sensores.update_one({"nomeSensor":"Temp2"},{"$set":{"valorSensor":temp}})
            if(temp>=38):
                sensores.update_one({"nomeSensor":"Temp2"},{"$set":{"sensorAlarmado":True}})
        else:
            print("Atenção! Temperatura muito alta! Verificar Sensor Temp2!")
    else:
        data = {
            "nomeSensor":"Temp2",
            "valorSensor":temp,
            "unidadeMedida":"°C",
            "sensorAlarmado":False
        }
        sensores.insert_one(data)
    time.sleep(3)


def thread3():
    temp = random.randint(30,40)
    

    result = sensores.find_one({"nomeSensor":"Temp3"})
    if(result is not None):
        if(result["sensorAlarmado"] == False):
            print("Temperatura sensor 3:"+str(temp))
            sensores.update_one({"nomeSensor":"Temp3"},{"$set":{"valorSensor":temp}})
            if(temp>=38):
                sensores.update_one({"nomeSensor":"Temp3"},{"$set":{"sensorAlarmado":True}})
        else:
            print("Atenção! Temperatura muito alta! Verificar Sensor Temp3!")
    else:
        data = {
            "nomeSensor":"Temp3",
            "valorSensor":temp,
            "unidadeMedida":"°C",
            "sensorAlarmado":False
        }
        sensores.insert_one(data)
    time.sleep(3)

x = threading.Thread(target=thread1)
y = threading.Thread(target=thread2)
z = threading.Thread(target=thread3)


x.start()
y.start()
z.start()
