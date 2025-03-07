# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "eskill_custom"
app_title = "Eskill Customisations"
app_publisher = "Eskill Trading"
app_description = "App for any and all Eskill Trading customisations to ERPNext."
app_icon = "octicon octicon-file-directory"
app_color = "#ffbd20"
app_email = "andrew@eskilltrading.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = [
    "/assets/eskill_custom/css/form.css"
]
# app_include_js = "/assets/eskill_custom/js/eskill_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/eskill_custom/css/eskill_custom.css"
# web_include_js = "/assets/eskill_custom/js/eskill_custom.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    'Accounts Settings' : 'public/js/doctype/accounts_settings.js',
    'Customer' : 'public/js/doctype/customer.js',
    'Delivery Note' : 'public/js/doctype/delivery_note.js',
    'Item' : 'public/js/doctype/item.js',
    'Item Group' : 'public/js/doctype/item_group.js',
    'Journal Entry' : 'public/js/doctype/journal_entry.js',
    'Landed Cost Voucher' : 'public/js/doctype/landed_cost_voucher.js',
    'Material Request': 'public/js/doctype/material_request.js',
    'Payment Entry' : 'public/js/doctype/payment_entry.js',
    'Purchase Invoice' : 'public/js/doctype/purchase_invoice.js',
    'Purchase Order' : 'public/js/doctype/purchase_order.js',
    'Purchase Receipt' : 'public/js/doctype/purchase_receipt.js',
    'Quotation' : 'public/js/doctype/quotation.js',
    'Sales Invoice' : 'public/js/doctype/sales_invoice.js',
    'Sales Order' : 'public/js/doctype/sales_order.js',
    'Serial No': 'public/js/doctype/serial_no.js',
    'Stock Entry' : 'public/js/doctype/stock_entry.js',
    'Stock Reconciliation' : 'public/js/doctype/stock_reconciliation.js',
    'Supplier' : 'public/js/doctype/supplier.js',
    'Task' : 'public/js/doctype/task.js',
    'Timesheet' : 'public/js/doctype/timesheet.js',
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "eskill_custom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "eskill_custom.install.before_install"
# after_install = "eskill_custom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "eskill_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
#               "on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
# 	"all": [
# 		"eskill_custom.tasks.all"
# 	],
    'daily' : [
        "eskill_custom.eskill_customisations.doctype.device_sla.device_sla.update_state"
    ],
# 	"hourly": [
# 		"eskill_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"eskill_custom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"eskill_custom.tasks.monthly"
# 	]
}

# Testing
# -------

# before_tests = "eskill_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "eskill_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "eskill_custom.task.get_dashboard_data"
# }

fixtures = [
    'Custom Field',
    'Property Setter',
    {
        'dt': "Role",
        'filters': [
            ["role_name", "in", [
                "Cashier",
                "Stocktake User",
            ]]
        ]
    },
    {
        'dt': "DocType Link",
        'filters': [
            ["custom", "=", 1]
        ]
    }
]

website_context = {
    "favicon": "/assets/eskill_custom/images/EskillFavicon.png",
    "splash_image": "/assets/eskill_custom/images/EskillSplash.png"
}
