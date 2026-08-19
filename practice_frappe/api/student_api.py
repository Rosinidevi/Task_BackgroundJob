import frappe


@frappe.whitelist()
def process_students():

    Student = frappe.qb.DocType("Student")
    Department = frappe.qb.DocType("Department")

    results = (
        frappe.qb.from_(Student)
        .join(Department)
        .on(Student.dept == Department.name)
        .select(
            Student.name,
            Student.student_name,
            Student.age,
            Student.dept,
            Student.status,
            Student.mark
        )
        .where(Student.status == "Pending")
        .run(as_dict=True)
    )

    if not results:
        return []

    doc = frappe.get_doc("Student", results[0]["name"])
    doc.mark = doc.mark + 5
    doc.save()

    for student in results:
        frappe.db.set_value(
            "Student",
            student["name"],
            "status",
            "Completed"
        )

    return results