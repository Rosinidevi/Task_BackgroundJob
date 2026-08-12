# Copyright (c) 2026, Roshini and contributors
# For license information, please see license.txt
 # Copyright (c) 2026, Roshini and contributors
# For license information, please see license.txt
import logging
import frappe
from frappe.model.document import Document

logger = frappe.logger("student",allow_site=True)     #create logger object
logger.setLevel(logging.WARNING)

class Student(Document):
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        age: DF.Int
        blood_group: DF.Literal[None]
        dept: DF.Data | None
        status: DF.Literal["Pending", "Completed"]
        student_name: DF.Data | None

    def validate(self):
        
        logger.warning("Student validation started")
        logger.info(f"Student Name : {self.student_name}")
        logger.info(f"Age          : {self.age}")
        logger.info(f"Department   : {self.dept}")
        logger.info(f"Status       : {self.status}")
   