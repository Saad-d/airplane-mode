# Copyright (c) 2024, Saad and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestAirplane(FrappeTestCase):
	def setup(self):
		self.airplane = frappe.get_doc({
			'doctype': 'Airplane',
			'capacity':2,
			'name':'Test Airplane'
		}).insert()
	    
		self.flight = frappe.get_doc({
			'doctype':'Airplane Flight',
			'airplane':self.airplane.name,
			'name':'Test Flight'
		}).insert()
    
	def test_creation_below_capacity(self):
		ticket1 =  frappe.get_doc({
            'doctype':'Airplane Ticket',
			'flight':self.flight.name
		}).insert()

		ticket2 =  frappe.get_doc({
            'doctype':'Airplane Ticket',
			'flight':self.flight.name
		}).insert()

		self.assertEqual(frappe.db.count('Airplane Ticket',{'flight':self.flight.name}),2)

	def test_ticket_creation_exceeds_capacity(self):
        # Insert two tickets to reach the airplane's capacity
		ticket1 =  frappe.get_doc({
            'doctype':'Airplane Ticket',
			'flight':self.flight.name
		}).insert()

		ticket2 =  frappe.get_doc({
            'doctype':'Airplane Ticket',
			'flight':self.flight.name
		}).insert()

		with self.assertRaises(frappe.ValidationError):
			frappe.get_doc({
				'doctype':'Airplane Ticket',
				'flight' : self.flight.name
			}).insert()
		self.assertEqual(frappe.db.count('Airplane Ticket', {'flight': self.flight.name}), 2)