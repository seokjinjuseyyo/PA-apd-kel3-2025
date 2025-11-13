# # Berisi program utama 
# from func import *
# from data import *
# from admin import *
# from user import *

# import os
# import time
# from prettytable import PrettyTable

# while True :

#     loading()
#     tampilkan_header_utama()
#     menu_awal()

#     pilihan_utama = input("Pilih menu (1-3): ")

#     if pilihan_utama == "1":
#                 layar_bersih()
#                 login()
#                 pilihan_login = input("Pilih menu (1-2): ")

#                 if pilihan_login == "1" : # Login Admin
#                     layar_bersih()
#                     tampilkan_header_utama()
                
#                     while percobaan < max_percobaan:
#                             Login_Username = input("Masukkan username Admin : ")
#                             Login_Password = input("Masukan password Admin : ")


#                             if Login_Username == Username and Login_Password == Password  :
                
#                                 Admin = True
#                                 status_login = True
#                                 break
                                    

#                             else:
#                                 percobaan += 1
#                                 print("Username atau Password salah !!!")
#                                 layar_bersih()

#                                 if percobaan == max_percobaan :
#                                     layar_bersih()
#                                     print("Username atau Password salah !!!")
#                                     input("Tekan Enter untuk memulai dari awal......")
#                                     break
                    
#                 if pilihan_login == "2" : # Login User
#                     layar_bersih()
#                     tampilkan_header_utama()

#                     while percobaan < max_percobaan:
#                         Login_Username = input("Masukkan username : ")
#                         Login_Password = input("Masukan password : ")


#                         if Login_Username == pengguna and Login_Password == Password  :
            
#                             User = True
#                             status_login = True
#                             break
                                

#                         else:
#                             percobaan += 1
#                             print("Username atau Password salah !!!")
#                             layar_bersih()

#                             if percobaan == max_percobaan :
#                                 layar_bersih()
#                                 print("Username atau Password salah !!!")
#                                 input("Tekan Enter untuk memulai dari awal......")
#                                 break
# rerereererer