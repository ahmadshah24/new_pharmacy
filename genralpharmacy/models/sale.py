from odoo import models, fields, api

class SaleInherit(models.Model):
    _inherit = "sale.order"
    _description = 'pharmacy.purchase.info'
