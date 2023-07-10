from odoo import models, fields, api
from odoo.exceptions import ValidationError
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        order = super(SaleOrder, self).create(vals)
        
        for line in order.order_line:
            product = line.product_id
            quantity_requested = line.product_uom_qty
            
            if product and quantity_requested:
                if quantity_requested > product.qty_available:
                    raise ValidationError('Not enough quantity available for product: %s' % product.name)
        
        return order