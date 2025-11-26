frappe.ui.form.on("Expense Claim", {
    refresh(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button("Print with Attachments", () => {
                frappe.call({
                    method: "frappe_expense_claim_print.api.expense_claim_print.get_expense_claim_with_attachments_pdf",
                    args: { name: frm.doc.name },
                    callback(r) {
                        if (!r.message) {
                            frappe.msgprint("Failed to generate PDF");
                            return;
                        }

                        const pdfData = "data:application/pdf;base64," + r.message;
                        const w = window.open();
                        w.document.write(
                            `<iframe src="${pdfData}" style="width:100%; height:100%; border:none;"></iframe>`
                        );
                    }
                });
            }).addClass("btn-primary");
        }
    }
});
