#!/usr/bin/env python
# coding: utf-8

# In[21]:


from cashier import transaction
import sys
def program(obj):
    '''
    Fungsi menampilkan menu pada kasir
    
    '''
    #Perintah yang muncul pada program
    actions = [
        "Insert your Article",
        "Update Article Name",
        "Update Article Quantity",
        "Update Article Price",
        "Remove Article",
        "Restart Transaction",
        "Check your Order",
        "Pay Now!",
    ]
    
    text = "Welcome to Pacmann-Market Frankfurt! Please choose those number to insert, update, or delete your article \n    , reset your transaction, or to process your payment"
    print(' ')
    print(text)
    print(' ')
    
    for index in range(len(actions)):
        action = actions[index]
        print(f"{index+1} : {action}");
        
    #Input requested feature
    feature = int(input('Choose your wished feature: '));
    
    try:
        if feature == 1:
            #Masukan nama Barang
            item_name = input('Please insert article name: ')
            
            #Masukan jumlah barang dan harus bilangan positif 0
            while True:
                try:
                    qty_item = float(input('Please insert quantity of goods: '))
                    if qty_item <= 0:
                        raise ValueError
                except ValueError:
                    print('Quantity of Item {item_name} must be positive number.\ Please input a quantity number with positive numbers only!')
                else:
                    break
                
            #Masukan harga barang dan harus bilangan positiv
            while True:
                try:
                    price_item = float(input('Please insert price of goods: '))
                    if price_item <= 0:
                        raise ValueError
                except ValueError:
                     print('Quantity of Item {item_name} must be positive number.\ Please input a quantity number with positive numbers only!')
                else:
                    break
                    
            #Memanggil fungsi menambahkan artikel 
            obj.add_item(item_name.capitalize(), qty_item, price_item)
            print(' ')
            #Kembali ke Program
            program(obj) 
        
        elif feature == 2:
            #Masukan nama Barang
            item_name = input('Please insert article name: ')
            
            #Masukan nama barang ingin di-update
            article_update_name = input('Please insert new article name: ')
            
            #Memanggil fungsi menambahkan artikel 
            obj.update_item_name(item_name.capitalize(), article_update_name.capitalize())
            print(' ')
            #Kembali ke Program
            program(obj)
        
        
        elif feature == 3:
            #Masukan nama Barang
            item_name = input('Please insert article name: ')
            
            #Masukan jumlah barang berupa bilangan asli
            while True:
                try:
                    qty_item_update = float(input('Please insert quantity of goods: '))
                    if qty_item_update <= 0:
                        raise ValueError
                except ValueError:
                    print(f'Amount of Item {item_name} must be positive number.             Please input a quantity number with positive numbers only!')
                else:
                    break
               
            #Memanggil fungsi menambahkan artikel 
            obj.update_item_quantity(item_name.capitalize(), qty_item_update)
            print(' ')
            #Kembali ke Program
            program(obj)
            
        elif feature == 4:
            #Masukan nama Barang
            item_name = input('Please insert article name: ')
            
            #Masukan hraga barang berupa bilangan asli
            while True:
                try: 
                    price_item_update = float(input('Please insert price of goods: '))
                    if price_item_update <= 0:
                        raise ValueError
                except ValueError:
                    print(f'Price of Item {item_name} must be positive number.                 Please input a quantity number with positive numbers only!')
                else:
                    break
                
             #Memanggil fungsi memperbaharui harga 
            obj.update_item_price(item_name.capitalize(), price_item_update)
            print(' ')
            #Kembali ke Program
            program(obj)
        
        elif feature == 5:
            #Masukan nama Barang
            item_name = input('Please insert article name: ')
            
            #Memanggil fungsi menghilangkan artikel 
            obj.delete_item(item_name.capitalize())
            print(' ')
            #Kembali ke Program
            program(obj)
            
        elif feature == 6:
            #Memanggil fungsi mengulang transaksi
            obj.reset_transaction()
            
            #Kembali ke Program
            program(obj)
            
        elif feature == 7:
            #Memanggil fungsi mengecek transaksi
            obj.check_order()
            print(' ')
            #Kembali ke Program
            program(obj)
            
        elif feature == 8:
            #Memanggil fungsi membayar barang belanjaan
            obj.total_price()
            obj.exit()
            pass
        
        else:
            print("Sorry, you give a wrong number. Please Follow the instruction!")
            #Kembali ke Program
            program(obj)  
    except:
        print("Sorry, your request can not be fulfilled. Please Follow the instruction!")
        #Kembali ke Program
        program(obj)     

tr1 = transaction()
program(tr1)


# In[20]:





# In[ ]:




