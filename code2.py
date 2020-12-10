import os
import json
import time
import threading
dic = {}
time_stamp = {} 
class CRD:
    
    def create(self,TIME = 0):
        key=input('Enter the key : ')
        if len(key) > 32:
            raise Exception('Key exceeds 32 characters')
        if (os.path.isfile(key)):
            raise Exception('Entered key is already present')
        value=input('Enter the value : ')
        file = json.dumps(value) 
        if file.__sizeof__() > (1024**3):
            raise Exception("Size exceeded")
        if(key.isalpha()):
            with open(key,'w') as f:
                dic[key]=value
                f.write(json.dumps(dic))
                if TIME == 0:
                    time_stamp[key] = TIME
                else:
                    time_stamp[key] = int(time.time()) + TIME 
        else:
            print("Enter a vaild key that contain only string\n")
            
                    
    def read(self):
        key=input('Enter the key to search : ')
        read_data = time_stamp[key]
        if (os.path.isfile(key)):
            with open(key,'r') as f:
                if(read_data!=0):
                    if int(time.time()) < int(read_data):
                        set_value = 0
                        for i in dic:
                            if key==i:
                                print('{',i,':',dic[i],'}')
                                set_value = 1
                        if(set_value==0):
                            print("Key not found\n")
                        print("Key found")
                        print(json.loads(f.readline()))
                    else:
                        print("Time-To-Live property of--" , key , "--has expired \n")
                else:
                    set_value = 0
                    for i in dic:
                        if key==i:
                            print("-----------------------")
                            print("|Key    |Value")
                            print("-----------------------")
                            user_dic = {}
                            user_dic[i] = int(dic[i])
                            print(user_dic)
                            user_dic.clear()
                            set_value = 1
                    if(set_value==0):
                        print("key not found")
                    print("Key found")
                    print(json.loads(f.readline()))
        else:
            print("File not found")
                    
       

    def delete(self):
        key=input('Enter the key to delete : ')
        if not(os.path.isfile(key)):
            raise Exception("!!!File not found")    
        else:
            read_data = time_stamp[key]
            if read_data!=0:
                if int(time.time()) < int(read_data):
                    os.remove(key)
                    print("User Detail is successfully deleted!\n")
                else:
                    print("Time-To-Live property of" , key , "has expired ")
            else:
                os.remove(key)
if __name__ == '__main__':
    d = CRD()
    try:
            path = input('Enter the path to store the data : \n')
            os.mkdir(os.path.join(path,'data1'))
            path = path+'\data1'
            os.chdir(path)
    except:
        path = r"C:\Users\srinivasan\Desktop\a"
        os.mkdir(os.path.join(path,'data1'))
        path=path+'\data1'
        os.chdir(path)
    n = 1
    while(True):
        print("\n1.Create new key-value pair.\n2.To read a value. \n3. Delete a key-value. \nPress 0 to exit")
        val = int(input())
        if(val==1):
            ttl= int(input("enter the TIME-TO-LIVE : "))
            t1=threading.Thread(target=(d.create),args = (ttl,))
            t1.start()
            t1.join()
        elif(val==2):
            t2=threading.Thread(target=( d.read))
            t2.start()
            t2.join()
        elif(val==3):
            t3=threading.Thread(target=(d.delete))
            t3.start()
            t3.join()
        else:
            print("Exit.")
            break
