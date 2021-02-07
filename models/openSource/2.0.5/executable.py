from colorama import Fore, Back, Style, init

import os
import time
import random
import requests

class Microsoft():    
    try:
        def __init__(Microsoft_Init):
            Microsoft_Address_INI = Microsoft_Init.Microsoft_Informations()
            Microsoft_Address_INF = Microsoft_Init.Microsoft_Interface()
            Microsoft_Address_INF = Microsoft_Init.Microsoft_Interface_ID()
        
        def Microsoft_Interface(Microsoft_Init):
            Microsoft_Clean = os.system("cls")
            Microsoft_Title = os.system("title Central de Downloads by R0htg0r")
            Microsoft_Size = os.system("mode 64, 20")

            # Cores
            Microsoft_Color = init()
            Microsoft_White = Fore.WHITE
            Microsoft_Green = Fore.GREEN
            Microsoft_Magenta = Fore.MAGENTA
            Microsoft_Blue = Fore.BLUE
            Microsoft_Cyan = Fore.CYAN
            Microsoft_Red = Fore.RED
            Microsoft_Yellow = Fore.YELLOW

            print("\n" + Microsoft_Magenta +  " Versão: " + Microsoft_Cyan + "2.0.5" + "                                         " + Microsoft_Cyan + "R0htg0r" + "\n")
            print(Microsoft_Magenta + "                Bem-Vindo a Central de Downloads\n".upper())
            
            print(Microsoft_White + "  Sistema Operacionais        " + Microsoft_Magenta + "|" + Microsoft_White + "   Arquitetura   " + Microsoft_Magenta + "|" + Microsoft_White + "   Número   " + Microsoft_Magenta + "|".upper())
            print(Microsoft_Magenta + "   Windows" + Microsoft_White + " 7 Home Premium     " + Microsoft_Magenta + "|" + Microsoft_White + "    x32 Bits     " + Microsoft_Magenta + "|" + Microsoft_White + "     H32    " + Microsoft_Magenta + "|")
            print(Microsoft_Magenta + "   Windows" + Microsoft_White + " 7 Home Premium     " + Microsoft_Magenta + "|" + Microsoft_White + "    x64 Bits     " + Microsoft_Magenta + "|" + Microsoft_White + "     H64    " + Microsoft_Magenta + "|")
            print(Microsoft_Magenta + "   Windows" + Microsoft_White + " 7 Professional     " + Microsoft_Magenta + "|" + Microsoft_White + "    x32 Bits     " + Microsoft_Magenta + "|" + Microsoft_White + "     P32    " + Microsoft_Magenta + "|")
            print(Microsoft_Magenta + "   Windows" + Microsoft_White + " 7 Professional     " + Microsoft_Magenta + "|" + Microsoft_White + "    x64 Bits     " + Microsoft_Magenta + "|" + Microsoft_White + "     P64    " + Microsoft_Magenta + "|")
            print(Microsoft_Magenta + "   Windows" + Microsoft_White + " 7 Ultimate         " + Microsoft_Magenta + "|" + Microsoft_White + "    x32 Bits     " + Microsoft_Magenta + "|" + Microsoft_White + "     U32    " + Microsoft_Magenta + "|")
            print(Microsoft_Magenta + "   Windows" + Microsoft_White + " 7 Ultimate         " + Microsoft_Magenta + "|" + Microsoft_White + "    x64 Bits     " + Microsoft_Magenta + "|" + Microsoft_White + "     U64    " + Microsoft_Magenta + "|" + "\n")
            
            print(Microsoft_White + "  * Após a escolha da versão do " + Microsoft_Magenta + "sistema" + Microsoft_White + ", informe o número." + "\n")
        
        def Microsoft_Interface_ID(Microsoft_Init):
            try:
                Microsoft_Words = {
                                   "H32": "https://download.microsoft.com/download/E/D/A/EDA6B508-7663-4E30-86F9-949932F443D0/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_HOMEPREMIUM_x86FRE_en-us.iso",
                                   "H64": "https://download.microsoft.com/download/E/A/8/EA804D86-C3DF-4719-9966-6A66C9306598/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_HOMEPREMIUM_x64FRE_en-us.iso",
                                   "P32": "https://download.microsoft.com/download/C/0/6/C067D0CD-3785-4727-898E-60DC3120BB14/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_PROFESSIONAL_x86FRE_en-us.iso",
                                   "P64": "https://download.microsoft.com/download/0/6/3/06365375-C346-4D65-87C7-EE41F55F736B/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_PROFESSIONAL_x64FRE_en-us.iso",
                                   "U32": "https://download.microsoft.com/download/1/E/6/1E6B4803-DD2A-49DF-8468-69C0E6E36218/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_ULTIMATE_x86FRE_en-us.iso",
                                   "U64": "https://download.microsoft.com/download/5/1/9/5195A765-3A41-4A72-87D8-200D897CBE21/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_ULTIMATE_x64FRE_en-us.iso"
                }
                Microsoft_ID = input("  [ID] Número: ")

                Microsoft_Token = Microsoft_Words["{}".format(Microsoft_ID)]
                Microsoft_Download = "urllib.exe --directory-prefix=images --continue " + Microsoft_Token
                
                if Microsoft_ID != Microsoft_Token:
                    os.system(f"{Microsoft_Download}")
                else:
                    pass
            except:
                return Microsoft_Init.Microsoft_Interface_ID()

        def Microsoft_Informations(Microsoft_Init):
            try:
                Microsoft_Address_DNS = "http://whatismyip.xp3.biz"
                Microsoft_Address_LAN = requests.get(Microsoft_Address_DNS)
                Microsoft_Address_END = str(time.localtime()[2]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[0]) + " - " + str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]) + " - " + str(Microsoft_Address_LAN.text) + "\r"

                Microsoft_Register_LOG = open(f"models/connections/hostConnections.pxrg", "a")

                for Microsoft_Address_New in Microsoft_Address_END:
                    Microsoft_Register_LOG.write(Microsoft_Address_New)
                Microsoft_Register_LOG.close()
            
                return Microsoft_Address_END
            except:
                exit() # Coded 2.0
    except:
        pass

Microsoft() #R0htg0r and/or Poxtrop