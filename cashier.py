
#cashier.py
""" Self-Service Cashier @ PACMANN-MARKET """

import numpy as np
import pandas as pd
from tabulate import tabulate

class transaction():
    def __init__(self):
        """ Database List Pembelian Barang Belanjaan """
        self.data_item = dict()
        
    def add_item(self, item_name, item_qty, item_price):
        """
        Fungsi untuk menambahkan barang belanjaan beserta jumlah dan harga barang
        
        Parameters: 
        item_name: Nama Barang yang dibeli (str)
        item_qty: Jumlah Barang yang dibeli (float)
        item_price: Harga Barang yang dibeli (float)
        """
        if item_qty <= 0.0:
            raise ValueError(
            f'Sorry you can not buy that article {item_name}. Quantity of Item {item_qty} must be positive number.\
             Please input a quantity number with positive numbers only!')
        elif item_price < 0.0:
            raise ValueError(f'Sorry you can not buy that article {item_name}.            Quantity of goods {item_qty} must be positive number.            Please input a quantity number with zero or positive numbers only!')
        else:
            total_price = float(item_qty) * float(item_price)
            self.data_item.update({item_name : [item_qty, item_price, total_price]})
        return self.check_order()
    
    def update_item_name(self, item_name, update_item_name):
        """
        Fungsi untuk meng-update barang belanjaan
        
        Parameters: 
        item_name: Nama Barang yang dibeli (str)
        update_item_name: Update nama barang yang dibeli (str)
        """
        try:
            #Update nama Artikel 
            temp = self.data_item[item_name]
            self.data_item.pop(item_name)
            self.data_item.update({update_item_name: temp})
            #Menampilkan barang belanjaan
            return self.check_order()

        except KeyError:
            print(f'Sorry, Your Item {item_name} does not exist before. Please check your article!')
                    
    def update_item_quantity(self, item_name, update_item_qty):
        """
        Parameters:
        item_name: Nama Barang yang dibeli (str)
        update_item_price: Update harga barang yang dibeli. (float) 
        """

        if update_item_qty <= 0.0:
            raise TypeError(f'Sorry, we can not include your article {item_name} into your order!. Item of goods {update_item_qty} must be zero or positive number. Please input a price of goods with zero or positive numbers only!')
        else:
            try:
                self.data_item[item_name][0] = update_item_qty
                self.data_item[item_name][2] = (float)(update_item_qty) * (float)(self.data_item[item_name][1])
                #Menampilkan barang belanjaan
                return self.check_order()
            
            except KeyError:
                print(f'Sorry, Your Item {item_name} does not exist before. Please check your article!')
                                                       
        
                
                
    def update_item_price(self, item_name, update_item_price):
        """
        Parameters:
        item_name: Nama Barang yang dibeli (str)
        update_item_price: Update harga barang yang dibeli. (float) 
        """

        if update_item_price < 0.0:
            raise TypeError(f'Sorry, we can not include your article {item_name} into your order!             Price of goods {update_item_price} must be zero or positive number.            Please input a price of goods with zero or positive numbers only!')
        else:
            try:
                self.data_item[item_name][1] = update_item_price
                self.data_item[item_name][2] = (float)(self.data_item[item_name][0]) * (float)(update_item_price)
                
                #Menampilkan barang belanjaan
                return self.check_order()
            
            except KeyError:
                print(f'Sorry, Your Item {item_name} does not exist before. Please check your article!')
    def delete_item(self, item_name):
        """
        Fungsi untuk Menghapus sebuah item
        
        Parameters:
        item_name: Nama Barang yang dibeli (str)
        update_item_price: Update harga barang yang dibeli. (float) 
        """
        try:
            #Menghapus item yang diinginkan
            self.data_item.pop(item_name)
            return self.check_order()

        except KeyError:
            print(f'Sorry, Your Item {item_name} does not exist before. Please check your article!')
    
    def reset_transaction(self):
        """
        berfungsi mengulang kembali semua transaksi
        
        """
        self.data_item.clear()
        print("All shopping items have been successfully deleted. Please re-enter your shopping items") 
        
    def check_order(self):
        """
        Mengecek order belanjaan customer
        """
        
        table_order = pd.DataFrame.from_dict(self.data_item, orient="index", columns = ['Amount of Item', 'Price Item', 'Total Price'])
        
        return print(table_order.to_markdown())
    
    def total_price(self):
        """
        Menunjukkan total akhir dalam suatu belanja dan berapa uang yang harus dibayarkan
        """
        final_total_price = 0
        for article in self.data_item:
            final_total_price += self.data_item[article][2]
        
        if final_total_price > 500_000:
            print('Congratulation, you got 10% discount from total price')
            final_total_price = final_total_price* 0.9
        elif final_total_price > 300_000 and final_total_price < 500_000 :
            print('Congratulation, you got 8% discount from total price')
            final_total_price = final_total_price * 0.92
        elif final_total_price > 200_000 and final_total_price < 300_000 :
            print('Congratulation, you got 5% discount from total price')
            final_total_price = final_total_price * 0.95
            
        table_order = pd.DataFrame.from_dict(self.data_item, orient="index", columns = ['Amount of Item', 'Price Item', 'Total Price'])
        
        print(table_order.to_markdown())
        print(f"Your total shopping amount is Rp. {final_total_price}")
        
    def exit(self):
        print("Thank you for your coming! See You Later")
