# -- coding:utf-8 --
import socket,requests,re,os
from multiprocessing import Process

def handle_client(client_socket):
    html = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>DingDingBot</h1><spen></spen><h2>Surr</h2>'
    html = bytes(html,encoding='utf8') 
    try:
        client_socket.sendall(html)
    except Exception as e:
        print(e)
    finally:
        client_socket.close()

def DingDingSet():
    lujin = os.path.dirname(os.path.abspath(__file__))
    with open(f"{lujin}/data/DingDingSet.json","r",encoding="utf-8") as set:
        DingSet = set.read()
    global Post_set,ip
    DingSet_text = eval(DingSet)
    Post_set = (DingSet_text['set'][0]['Post'])
    url = requests.get("http://txt.go.sohu.com/ip/soip")
    text = url.text
    ip = re.findall(r'\d+.\d+.\d+.\d+',text)

def xiaoxi():
    try:
        os.system('clear')
    except:
        os.system('cls')
    print(" \033[0;37;40m\t\t\t验证程序\033[0m") 
    print("访问以下地址,访问失败则检查\033[1;77m[\033[0m\033[1;31m防火墙是否打开、公网是否能访问\033[0m\033[1;77m]") 
    print(f"\033[1;77m[\033[0m\033[1;33mIP\033[0m\033[1;77m]\033[0m\033[93m {ip[0]}:{Post_set} \033[0m")
    print("\n\n\033[1;77m[\033[0m\033[1;33m注\033[0m\033[1;77m]\033[0m\033[0;37;77m 只有在官网编辑钉钉机器人信息才需要启动此程序,机器人启动不需要运行此程序\033[0m") 

if __name__ == "__main__":
    DingDingSet()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", Post_set))
    server_socket.listen(120)
    xiaoxi()
    while True:
        client_socket, client_address = server_socket.accept()
        
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()