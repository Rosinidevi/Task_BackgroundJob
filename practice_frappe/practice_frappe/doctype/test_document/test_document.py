# Copyright (c) 2026, Roshini and contributors
# For license information, please see license.txt

# import Frappe
from frappe.model.document import Document


class TestDocument(Document):

    def before_save(self):

        if not self.description:
            self.description = "Default Description"