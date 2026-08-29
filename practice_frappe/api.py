"""
import time

def sample_job():
    print("Job Started")

    time.sleep(10)

    print("Job Finished")

"""
    
'''
import frappe
import time
from frappe.utils import now_datetime

def sample_job():
    start_time = now_datetime()

    print("===== JOB STARTED =====")
    print(f"Start Time : {start_time}")

    print("Processing the job...")
    time.sleep(10)

    end_time = now_datetime()

    print("===== JOB FINISHED =====")
    print(f"End Time   : {end_time}")

    duration = end_time - start_time
    print(f"Duration   : {duration}")
    '''

import frappe


@frappe.whitelist()
def create_customer_user(email, student_name, password):

    if frappe.db.exists("User", {"email": email}):
        frappe.throw("User already exists for this email")

    user = frappe.new_doc("User")

    user.email = email
    user.first_name = student_name


    user.new_password = password

    user.append("roles", {
        "role": "Accounts User"
    })

    user.insert(ignore_permissions=True)

    return user.name