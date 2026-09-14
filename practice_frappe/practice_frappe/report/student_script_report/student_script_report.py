import frappe


def execute(filters=None):
    columns = [
        {
            "label": "Student Name",
            "fieldname": "student_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Department",
            "fieldname": "dept",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Mark",
            "fieldname": "mark",
            "fieldtype": "Currency",
            "width": 120
        }
    ]

    data = [
        {
            "student_name": "Arun",
            "dept": "Computer Science",
            "mark": 8500
        },
        {
            "student_name": "Kumar",
            "dept": "Information Technology",
            "mark": 9200
        },
        {
            "student_name": "Ravi",
            "dept": "Computer Science",
            "mark": 7800
        }
    ]

    return columns, data