/*
frappe.ready(function () {

    let password_section = $(`
        <div class="form-group">
            <label>Password</label>
            <input
                type="password"
                class="form-control"
                id="registration_password"
            >
        </div>
    `);

    frappe.web_form.fields_dict.age.$wrapper.after(password_section);


    frappe.web_form.after_save = () => {

        let password = $("#registration_password").val();

        frappe.call({
            method: "practice_frappe.api.create_customer_user",

            args: {
                email: frappe.web_form.get_value("email"),
                student_name: frappe.web_form.get_value("student_name"),
                password: password
            },

            callback: function (r) {

                if (!r.exc) {
                    frappe.msgprint(
                        "Customer User created successfully"
                    );
                }

            }
        });
    };

}); */