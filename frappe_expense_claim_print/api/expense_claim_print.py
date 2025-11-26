import frappe
from frappe.utils.pdf import get_pdf
from PyPDF2 import PdfMerger
import base64
import io

@frappe.whitelist()
def get_expense_claim_with_attachments_pdf(name):
    # Base PDF
    html = frappe.get_print("Expense Claim", name)
    base_pdf = get_pdf(html)

    merger = PdfMerger()
    merger.append(io.BytesIO(base_pdf))

    # Attachments
    attachments = frappe.get_all(
        "File",
        filters={"attached_to_doctype": "Expense Claim", "attached_to_name": name},
        fields=["name", "file_name"]
    )

    for att in attachments:
        file_doc = frappe.get_doc("File", att.name)
        content = file_doc.get_content()

        fn = att.file_name.lower()

        if not fn.endswith(".pdf"):
            encoded = base64.b64encode(content).decode()
            html = f"""
                <html><body style="margin:0;padding:0">
                <img src="data:image/*;base64,{encoded}" style="width:100%;height:auto;">
                </body></html>
            """
            content = get_pdf(html)

        merger.append(io.BytesIO(content))

    # Output PDF
    out = io.BytesIO()
    merger.write(out)
    merger.close()

    return base64.b64encode(out.getvalue()).decode()
