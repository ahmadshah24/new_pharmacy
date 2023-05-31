from odoo import models, fields, api

class ProductInherit(models.Model):
    _inherit = "product.template"
    _description = 'sharq_investment.sharq_employee'


    cat_id=fields.Many2one("odoo.medicine.category",replace='categ_id')
    com_id=fields.Many2one("odoo.medicine.company")
    type_id=fields.Many2one("pharmacy.medicine.type")
