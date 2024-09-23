# Copyright (c) 2024, Saad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airplane(Document):
	def validate(self):
		flight = frappe.get_doc("Flight",self.flight)
		airplane = frappe.get_doc("Airplane",flight.airpalne)

		airplane_capacity = airplane.capacity
		ticket_count = frappe.db.count('Airplane ticket',{'flight':self.flight})

		if ticket_count >= airplane_capacity:
			frappe.throw(f"Cannot create more tickets for this flight. The airplane has onl {airplane_capacity}")

