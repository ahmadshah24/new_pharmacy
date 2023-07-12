from odoo import models, fields, api
from odoo.exceptions import ValidationError
class SaleOrder(models.Model):
    _inherit = 'sale.order'

   

    discount = fields.Integer("dicount(%)")

    total_with_discount = fields.Integer("Total",compute="_compute_total_with_discout")


    @api.onchange('discount')
    def _compute_total_with_discout(self):
        for order in self:
            discount_percentage = order.discount / 100.0
            order.total_with_discount = order.amount_total * (1 - discount_percentage)
        