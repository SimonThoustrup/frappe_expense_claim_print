frappe.ui.form.on("Expense Claim", {
    refresh(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button("Print with Attachments", () => {
                frappe.call({
                    method: "frappe_expense_claim_print.api.expense_claim_print.get_expense_claim_with_attachments_pdf",
                    args: { name: frm.doc.name },
                    callback(r) {
                        if (!r.message) {
                            frappe.msgprint("PDF generation failed");
                            return;
                        }

                        let pdf = "data:application/pdf;base64," + r.message;
                        let win = window.open();
                        win.document.write(`<iframe src="${pdf}" style="width:100%;height:100%;border:none;"></iframe>`);
                    }
                });
            }).addClass("btn-primary");
        }
    }
});
