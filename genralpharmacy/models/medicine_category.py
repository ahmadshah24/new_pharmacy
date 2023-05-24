# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MedicineCategor(models.Model):
    _name = 'odoo.medicine.category'
    _description = 'medicine.company.category'

    name = fields.Selection(
    selection=[
        ('all', "All"),
        ('consumable', "Consumable"),
        ('expaneses', "Expaneses"),
        ('internal', "Internal"),
    ],
    string="Type"
)

    product_id=fields.Many2one("product.template")
