// Copyright (c) 2024, Saad and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Airline", {
 	refresh(frm) {
        if (frm.doc.website_link) {
            // Add a custom web link to the form that points to the airline's official website
            frm.add_custom_button(__('Visit Website'), function() {
                window.open(frm.doc.website_link, '_blank');
            }).addClass('btn-primary');
        }
    
 	},
 });
