from odoo import models, fields, api

class ContractInherit(models.Model):
    _inherit = "hr.contract"
    _description = 'pharmacy.employee.info'
