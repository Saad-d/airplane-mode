# Copyright (c) 2024, Saad and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [{
		"fieldname":"airplane",
		"label":"Airplane",
		"fieldtype":"link"
	},{
		"fieldname":"total_revenue",
		"label":"Revenue",
		"fieldtype":"currency",
		"options":"INR"
	},
	]

	data = frappe.get_all("Airplane Ticket", 
		fields=["SUM(total_amt) AS total_revenue",
		"flight.airplane"],group_by="airplane")
	
	chart = {
		"data":{
			"labels":[x.airplane for x in data],
			"datasets":[{"values":[x.total_revenue for x in data]}],
		},
		"type":"donut",
	}
	total_revenue = sum([x['total_revenue'] for x in data])
	summery = [{
		"label": "Total Revenue",
        "value": total_revenue,
        "indicator": "green"
	}]
	return columns, data, 'Here is the report', chart, summery
