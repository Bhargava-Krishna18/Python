

class Fruits:
	
	def __init__(self,fid,name,rate,imp_frm,imp_date,buy_price):
		self.fid = fid
		self.name = name
		self.rate = rate
		self.imp_frm = imp_frm
		self.imp_date = imp_date
		self.buy_price = buy_price
		
	def display(self):
		print(f"Fr_id : {self.fid} | Name : {self.name} | Rate : {self.rate} | imp_from : {self.imp_frm} | imp_date : {self.imp_date} | buy_price : {self.buy_price}")
		
