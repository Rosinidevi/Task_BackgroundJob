import frappe
from frappe.model.document import Document


class Student(Document):
    pass
"""
import frappe
from frappe.model.document import Document


class Student(Document):

    def validate(self):

        if frappe.session.user == "Guest":
            frappe.throw("You must be logged in")
        student = frappe.db.get_value(
            "Student",
            {"email": frappe.session.user},
            "name"
        )

        if not student:
            frappe.throw("Student record not found")
        self.student = student
        """