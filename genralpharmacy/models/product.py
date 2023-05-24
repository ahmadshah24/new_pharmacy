from odoo import models, fields, api

class ProductInherit(models.Model):
    _inherit = "product.template"
    _description = 'sharq_investment.sharq_employee'

    age = fields.Integer("Age")