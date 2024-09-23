// Copyright (c) 2024, Saad and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Airplane Ticket", {
 	refresh(frm) {
          //Adding custom button for seat assignment
		frm.add_custom_button(__('Assign Seat'), function() {
            // Open a dialog with an input field for seat number
            let dialog = new frappe.ui.Dialog({
                title: 'Enter Seat Number',
                fields: [
                    {
                        label: 'Seat',
                        fieldname: 'seat',
                        fieldtype: 'Data',
                        reqd: 1 // Make it mandatory
                    }
                ],
                primary_action_label: 'Set Seat',
                primary_action: function(values) {
                    // Set the entered seat number to the 'Seat' field in the form
                    frm.set_value('seat', values.seat);
                    dialog.hide();
                }
            });
            // Show the dialog
            dialog.show();
        }).addClass('btn-primary'); // Make the button appear prominently
 	},
});
