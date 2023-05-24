from odoo import models, fields, api

class EmployeeInherit(models.Model):
    _inherit = "hr.employee"
    _description = 'pharmacy.employee.info'



    salary =fields.Integer("Salary")

