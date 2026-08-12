import frappe

@frappe.whitelist()
def say_hello():
    return "Hello from Original Function"