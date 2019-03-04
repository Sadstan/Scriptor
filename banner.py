#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choice

def choice_banner():
	banner1 = """
\033[31m

 ██████  ▄████▄   ██▀███   ██▓ ██▓███  ▄▄▄█████▓ ▒█████   ██▀███  
▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░ ▒ ░░▒ ░         ░      ░ ▒ ▒░   ░▒ ░ ▒░
░  ░  ░  ░          ░░   ░  ▒ ░░░         ░      ░ ░ ░ ▒    ░░   ░ 
      ░  ░ ░         ░      ░                        ░ ░     ░     
         ░                                                         
\033[0;0m v_1.0 Desenvolvido com amor por Pedro Hoffmann

\033[1;36m<OPTIONS>\033[0;0m					\033[1;36m<STATUS>\033[0;0m
Digite (2) para SMTP				\033[42;1;32mOnline\033[0;0m
Digite (0) para busca de painel administrativo	\033[41;1;31mOff-line\033[0;0m
Digite (0) para scanear redes e servidores	\033[41;1;31mOff-line\033[0;0m
Digite (0) para criptografias	                \033[41;1;31mOff-line\033[0;0m
Digite (1) para requisições web	                \033[42;1;32mOn-line\033[0;0m

Digite \033[36m0\033[0;0m para sair

	"""

	banner2 = """
\033[1;36m
         _nnnn_                      
        dGGGGMMb     .----------------.
       @p~qp~~qMb    | Open Source <3!|
       M|@||@) M|   _.----------------.
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' 
\033[0;0m
\033[1;36m<OPTIONS>\033[0;0m					\033[1;36m<STATUS>\033[0;0m
Digite (2) para SMTP				\033[42;1;32mOnline\033[0;0m
Digite (0) para busca de painel administrativo	\033[41;1;31mOff-line\033[0;0m
Digite (0) para scanear redes e servidores	\033[41;1;31mOff-line\033[0;0m
Digite (0) para criptografias	                \033[41;1;31mOff-line\033[0;0m
Digite (1) para requisições web	                \033[42;1;32mOn-line\033[0;0m

Digite \033[36m0\033[0;0m para sair
	"""

	banner3 = """
\033[1;33m
       _________
      (=========) 
      |=========| 
      |====_====| 
      |== / \ ==| 
      |= / _ \ =| 
   _  |=| ( ) |=| 
  /=\ |=|     |=| /=\ 
  |=| |=| USA |=| |=|
  |=| |=|  _  |=| |=|
  |=| |=| | | |=| |=|
  |=| |=| | | |=| |=|
  |=| |=| | | |=| |=|
  |=| |/  | |  \| |=|
  |=|/    | |    \|=|
  |=/NASA |_| NASA\=|
  |(_______________)|
  |=| |_|__|__|_| |=|
  |=|   ( ) ( )   |=|
 /===\           /===\ 
|||||||         ||||||| 
-------         ------- 
 (~~~)           (~~~) 
\033[0;0m
\033[1;36m<OPTIONS>\033[0;0m					\033[1;36m<STATUS>\033[0;0m
Digite (2) para SMTP				\033[42;1;32mOnline\033[0;0m
Digite (0) para busca de painel administrativo	\033[41;1;31mOff-line\033[0;0m
Digite (0) para scanear redes e servidores	\033[41;1;31mOff-line\033[0;0m
Digite (0) para criptografias	                \033[41;1;31mOff-line\033[0;0m
Digite (1) para requisições web	                \033[42;1;32mOn-line\033[0;0m

Digite \033[36m0\033[0;0m para sair	
	"""
	lista = [banner1,banner2, banner3]
	choice1 = choice(lista)
	print(choice1)

choice_banner()