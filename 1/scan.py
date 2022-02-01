import os , ctypes , threading ,  subprocess
from time import sleep
from sys import argv
from mem_edit import Process

def zapkonc(initial_value,nober_serva,miner_nomb): 
    while initial_value == int(cons(nober_serva,miner_nomb)):
        sleep(2)
        with open(f'/root/{nober_serva}/{miner_nomb}/log/1.log', "w") as f_out:
           f_out.write(str(cons(nober_serva,miner_nomb)))

def cons(nober_serva,miner_nomb):
    with open(f'/root/{nober_serva}/{miner_nomb}/log/miner.log.log') as f:
       data_log = f.read()
    cons_p=data_log[data_log.rfind("scan consume="):data_log.rfind("scan consume=")+17]
    cons=cons_p[13:]
    return cons

def read_hex(nober_serva,miner_nomb):
    initial_value = int(cons(nober_serva,miner_nomb))
    print(initial_value)
    pid = Process.get_pid_by_name('miner' + str(miner_nomb))
    print(pid)
    if pid == None:
        input('Я не нашел процесса , проверь майнер и нажми любую клавишу')
        initial_value = int(cons(nober_serva,miner_nomb))
        pid = Process.get_pid_by_name('miner' + str(miner_nomb))

    with open(f'/root/{nober_serva}/{miner_nomb}/log/1.log', "w") as f_out:
       f_out.write(f"{initial_value}")

    x = threading.Thread(target=zapkonc, args=(initial_value,nober_serva,miner_nomb ,))
    x.start()

    print('ЩАС СТАРТУЮ ')
    process = subprocess.Popen(['./22.sh', f'{pid}' , f'{initial_value}', f'{miner_nomb}'], stdout=subprocess.PIPE)
    rez22=str(str(process.stdout.read()))
    print(rez22)

    if int(rez22.rfind('we currently have 1 matches.')) > 1 :
        hex_rez=rez22[rez22.rfind('0]')+5:rez22.rfind('0]')+15]
        print('НАЙДЕНО '+hex_rez)
    else:
        print('НЕнайдеno')
        hex_rez=False

    return pid,hex_rez


sleep(5)
nober_serva = argv[1] 
miner_nomb = argv[2]


while '0 sc' == str(cons(nober_serva,miner_nomb)):
    print('ОЖИДАЮ НОНСУМЕ ОТЛИЧНОГО ОТ 0 ')
    sleep(2)
while 1501 > int(cons(nober_serva,miner_nomb)):
    print('ОЖИДАЮ НОНСУМЕ ОТЛИЧНОГО ОТ 1500 ')
    sleep(2)


data_scanmem = [False,False]
while data_scanmem[1]==False :
    data_scanmem=read_hex(nober_serva,miner_nomb)
    print(data_scanmem)
    sleep(2)






DIR = os.getcwd()
print(DIR)
print('СТАРТУЮ ЗАМОРОЗКУ СКАНТАЙМ')
sleep(2)

t=0
while True:
    t+=1
    if os.listdir(DIR):
       os.system(f"scanmem -p {data_scanmem[0]} -c 'write i32 {data_scanmem[1]} 3621;quit'")
       sleep(5)






       

#we currently have 1 matches.