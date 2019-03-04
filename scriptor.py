#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import smtplib
from tqdm import tqdm
from time import sleep
import banner

os.system('clear' or 'cls')

banner.choice_banner()

def main():
	try:
		escolha = int(str(input("scp: ")))
		if escolha == 1:
			sleep(1)
			os.system('clear' or 'cls')
			Request_Main()
		elif escolha == 2:
			sleep(1)
			os.system('clear' or 'cls')
			Login_Smtp()
		elif escolha == 0:
			exit()
		else:
			print("Opção inválida!")
	except:
		print("Aconteceu algum erro inesperado!")

def Smtp_Server(endereço,porta, usuario, senha):
	smtp = smtplib.SMTP(endereço, porta)
	smtp.starttls()
	smtp.ehlo()

	try:
		smtp.login(usuario,senha)
		print("Logado com sucesso! ")
		os.system('clear' or 'cls')
		sujeito = input("Sujeito: ").lower().strip()
		msg = input("Mensagem: ").lower().strip()
		n_msg = int(input("Número de mensagens a enviar: "))
		os.system('clear' or 'cls')
		for i in tqdm(range(0, n_msg)):
			sleep(0.1)
			print("Quantidade a enviar {} enviados: \033[1;32m{}\033[0;0m".format(n_msg, i))
			print('Enviando...',i)
			print('( {} ) de ( {} ) '.format(i, n_msg))
			smtp.sendmail(usuario,sujeito,msg)

		voltar = input('Deseja retornar ao menu principal? (Y/n): ').lower().strip()
		if voltar == "y":
			main()
		else:
			exit()
			
	except:
		print("ERRO!")
		Login_Smtp()

def Login_Smtp():
	print("""
1) Yahoo
2) Gmail
3) Outlook
4) Hotmail
	"""	)
	provedor = int(input("scp: "))

	if provedor == 1:
		user = input('Seu endereço de email: ').lower().strip()
		Verifica_Email(provedor, user)
		password = input("Digite a sua senha: ").strip()
		Smtp_Server('smtp.mail.yahoo.com', 465, user, password)

	elif provedor == 2:
		user = input('Seu endereço de email: ').lower().strip()
		Verifica_Email(provedor,user)
		
		password = input("Digite a sua senha: ").strip()
		Smtp_Server('smtp.gmail.com', 587, user, password)

	elif provedor == 3:
		user = input('Seu endereço de email: ').lower().strip()
		Verifica_Email(provedor,user)
		password = input("Digite a sua senha: ").strip()
		Smtp_Server('imap-mail.outlook.com', 587, user, password)

	elif provedor == 4:
		user = input('Seu endereço de email: ').lower().strip()
		Verifica_Email(provedor,user)
		password = input("Digite a sua senha: ")
		Smtp_Server('smtp.live.com', 465, user, password)
	else:
		print("Opção inválida!")

def Verifica_Email(escolha,usuario):

	if escolha == 1:
		s = usuario.find('@yahoo.com')
		if s == -1:
			print("O e-mail informado não é válido! Tente novamente")
			Login_Smtp()
		else:
			print("O email informado está correto!")

	elif escolha == 2:
		s = usuario.find('@gmail.com')
		if s == -1:
			print("O e-mail informado não é válido! Tente novamente")
			Login_Smtp()
		else:
			print("O email informado está correto!")

	elif escolha == 3:
		s = usuario.find('@outlook.com')
		if s == -1:
			print("O e-mail informado não é válido! Tente novamente")
			Login_Smtp()
		else:
			print("O email informado está correto!")
	elif escolha == 4:
		s = usuario.find('@hotmail.com')
		if s == -1:
			print("O e-mail informado não é válido! Tente novamente")
			Login_Smtp()
		else:
			print("O email informado está correto!")
	else:
		print("estamos desenvolvendo")

def Request_Main():
	endereço = input('Digite o endereço: ').lower().strip()
	if endereço == " ":
		print("Digite um endereço! ")
		Request_Main()
	try:
		prosseguir = int(input('Você deseja prosseguir com a ação? (1/Sim) (0/Sair) (2/Corrigir): '))
	except:
		print("Aconteceu algum erro! Verifique se você marcou uma opção")
		Request_Main()
	if prosseguir == 1:
		Request(endereço)
	elif prosseguir == 2:
		Request_Main()
	elif prosseguir == 0:
		exit()
	else:
		print("Opção inválida! ")
		exit()

def Request(parameter):
	os.system('clear')
	print("PROCESSANDO...")
	print("Tentando conectar-se a: ", parameter)
	sleep(3)
	try:
		requisição = requests.get(parameter)
		print("Conectado com sucesso ao endereço ", parameter)
		print("Estamos baixando a informação para o seu computador!")
		sleep(4)

		extrai_html = requisição.text
		print(extrai_html)

		with open('scriptor_req.html', 'w') as f:
			f.write(extrai_html)

		voltar_menu = input("Deseja voltar ao menu principal? (S/n): ").strip().lower()
		if voltar_menu == "s":
			sleep(2)
			os.system('clear' or 'cls')
			banner.choice()
			main()
		else:
			exit()
	except:
		print("Aconteceu algum erro!")

main()
