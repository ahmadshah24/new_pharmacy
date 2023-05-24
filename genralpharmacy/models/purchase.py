from odoo import models, fields, api

class ProductInherit(models.Model):
    _inherit = "purchase.order"
    _description = 'pharmacy.purchase.info'
