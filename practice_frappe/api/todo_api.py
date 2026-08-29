import frappe


@frappe.whitelist()
def get_recent_todos():

    todos = frappe.get_list(
        "ToDo",
        fields=["name", "description", "owner"],
        order_by="creation desc",
        limit=5
    )
    for todo in todos:
        todo["email"] = frappe.db.get_value(
            "User",
            todo["owner"],
            "email"
        )
    return {
        "timestamp": frappe.utils.now(),
        "records": todos
    }