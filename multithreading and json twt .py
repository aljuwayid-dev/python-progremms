#name: Abdulkarim Aljuwayid


#Program 1:
import json
import threading
import time
start = time.time()
mm = dict()
f = open('TweetsDataPart1.txt', 'r')
e = open('output.txt','w')
for k in f:
    w2 = f.readline()
    m5 = json.loads(w2)
    r = m5['created_at']
    mm['created_at']=r
    r = m5["user"]['screen_name']
    mm['screen_name'] = r
    r = m5['text']
    mm['text'] = r

    json_object2 = json.dumps(mm, indent= 1)
    e.write(json_object2)


mm2 = dict()
f2 = open('TweetsDataPart2.txt', 'r')
for k in f2:
    w2 = f2.readline()
    m5 = json.loads(w2)
    r1 = m5['created_at']
    mm2['created_at'] = r1
    r1 = m5["user"]['screen_name']
    mm2['screen_name'] = r1
    r1 = m5['text']
    mm2['text'] = r1

    json_object2 = json.dumps(mm2, indent= 1)
    e.write(json_object2)

f2.close()

mm3 = dict()
f3 = open('TweetsDataPart3.txt', 'r')
for k in f3:
    w3 = f3.readline()
    m66 = json.loads(w3)
    r3 = m66['created_at']
    mm3['created_at'] = r3
    r3 = m66["user"]['screen_name']
    mm3['screen_name'] = r3
    r3 = m66['text']
    mm3['text'] = r3

    json_object = json.dumps(mm3, indent= 1)
    e.write(json_object)
f2.close()
f.close()
e.close()
end = time.time()
e1 = end-start
print("E1: Total time is {} sec ".format(e1))

##Program 2:

def reading():
    f11 = open('TweetsDataPart1.txt', 'r')
    for k11 in f11:
        w2 = f11.readline()
        m5 = json.loads(w2)
        r1 = m5['created_at']
        mm11['created_at'] = r1
        r1 = m5["user"]['screen_name']
        mm11['screen_name'] = r1
        r1 = m5['text']
        mm11['text'] = r1
        json_object11 = json.dumps(mm11, indent=1)
        e.write(json_object11)
    f11.close()

def reading2():
   f22 = open('TweetsDataPart2.txt', 'r')
   for dfs in f22:
        w8 = f22.readline()
        m33 = json.loads(w8)
        r33 = m33['created_at']
        mm22['created_at'] = r33
        r33 = m33["user"]['screen_name']
        mm22['screen_name'] = r33
        r33 = m33['text']
        mm22['text'] = r33
        json_object22 = json.dumps(mm22, indent=1)
        e.write(json_object22)
   f22.close()




def reading3():
    f33 = open('TweetsDataPart3.txt', 'r')
    for u55 in f33:
        w77 = f33.readline()
        m222 = json.loads(w77)
        r333 = m222['created_at']
        mm33['created_at'] = r333
        r333 = m222["user"]['screen_name']
        mm33['screen_name'] = r333
        r333 = m222['text']
        mm33['text'] = r333
        json_object33 = json.dumps(mm33, indent=1)
        e.write(json_object33)
    f33.close()

start2 = time.time()
e=open('output2.txt','w')
mm11= dict()
mm22= dict()
mm33= dict()

t1 = threading.Thread(target=reading, name="T1")
t2 = threading.Thread(target=reading2, name="T2")
t3 = threading.Thread(target=reading3, name="T3")

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
end2= time.time()
e2 = end2-start2
print("=======================================")
print("E2:")
print("Total time is {} sec ".format(e2))
print("multithreading is faster by {}".format(e1-e2))
print("=======================================")