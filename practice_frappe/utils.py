
"""   
def before_job():
    print("===== BEFORE JOB =====")


def after_job():
    print("===== AFTER JOB =====")
"""



""" 
import frappe
from frappe.utils import now_datetime


def before_request():
    print("\n====================================")
    print("NEW REQUEST RECEIVED")
    print(f"Time   : {now_datetime()}")
    print(f"URL    : {frappe.request.path}")
    print(f"Method : {frappe.request.method}")
    print("====================================\n")


def after_request(response):
    print("\n====================================")
    print("REQUEST COMPLETED")
    print(f"Time : {now_datetime()}")
    print("====================================\n")

    return response  #after_request receives the response object. You should return it so Frappe can continue sending it to the browser.
    """