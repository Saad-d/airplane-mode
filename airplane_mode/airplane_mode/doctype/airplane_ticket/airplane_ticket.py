# Copyright (c) 2024, Saad and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe import _
from frappe.model.document import Document

class AirplaneTicket(Document):
	def validate(self):
		total_amt =0
		for item in self.adds_on:
			total_amt += item.amount

		self.total_amt = total_amt + self.flight_price

	
	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw(_('Pls change the status to Boarded for submiting'))
     
      
	def before_insert(self):
		seat_num = random.randint(1,99)
		seat_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
		self.seat = f"{seat_num}{seat_letter}"


