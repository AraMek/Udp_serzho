#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pickle as pl

IP = '127.0.0.1' #айпи сервера
PORT = 8000 #порт сервера
TIMEOUT = 60 #время ожидания ответа сервера [сек]

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #создаем udp сервер
server.bind((IP, PORT)) #запускаем udp сервер
print("Listening %s on port %d..." % (IP, PORT)) #выводим сообщение о запуске сервера
server.settimeout(TIMEOUT) #указываем серверу время ожидания

while True: #создаем бесконечный цикл    
    try:
        data = server.recvfrom(1024) #попытка получить 1024 байта
    except socket.timeout:
        print("Time is out...")
        break
    cmd, param = pl.loads(data[0]) #разбиваем ответ на сообщение
    adrs = data[1] #и адресс с портом откуда пришло сообщение

    print(cmd, param, adrs)


    if(cmd == 'speed'):
        leftSpeed, rightSpeed = param
        print('leftSpeed: %d, rightSpeed: %d' % (leftSpeed, rightSpeed))
    elif(cmd == 'beep'):
        print('Beep!!!')
    else:
        print('Unknown command: %s' % cmd)
    #msg = 'Ok'
    #server.sendto(msg.encode('utf-8'), adrs)
server.close()