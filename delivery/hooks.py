from __future__ import unicode_literals
import frappe
from . import __version__ as app_version


app_name = "delivery"
app_title = "Delivery"
app_publisher = "Nigel Jena"
app_description = "Shows delivery trips to clients and drivers"
app_email = "nigel@stokdirect.africa"
app_license = "MIT"


#Update driver's location
@frappe.whitelist()
def update_driver_location(driver, latitude, longitude):
    """Update the driver's location"""

    # Get the driver record
    driver_record = frappe.get_doc("Driver", driver)

    # Update the driver's location
    driver_record.set('driver_location', {'latitude': latitude, 'longitude': longitude})
    driver_record.save()

    # Return a success message


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/delivery/css/delivery.css"
# app_include_js = "/assets/delivery/js/delivery.js"

# include js, css files in header of web template
# web_include_css = "/assets/delivery/css/delivery.css"
# web_include_js = "/assets/delivery/js/delivery.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "delivery/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "delivery.utils.jinja_methods",
#	"filters": "delivery.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "delivery.install.before_install"
# after_install = "delivery.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "delivery.uninstall.before_uninstall"
# after_uninstall = "delivery.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "delivery.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"delivery.tasks.all"
#	],
#	"daily": [
#		"delivery.tasks.daily"
#	],
#	"hourly": [
#		"delivery.tasks.hourly"
#	],
#	"weekly": [
#		"delivery.tasks.weekly"
#	],
#	"monthly": [
#		"delivery.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "delivery.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "delivery.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "delivery.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"delivery.auth.validate"
# ]
