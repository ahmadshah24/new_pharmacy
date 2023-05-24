from odoo import models, fields, api

class CustomerInherit(models.Model):
    _inherit = "res.partner"
    _description = 'pharmacy.customer.info'
