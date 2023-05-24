from odoo import models, fields, api

class ProductInherit(models.Model):
    _inherit = "res.partner"
    _description = 'pharmacy.vender.info'
