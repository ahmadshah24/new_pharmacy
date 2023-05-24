# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MedicineType(models.Model):
    _name = 'pharmacy.medicine.type'
    _description = 'pharmacy.medicine.type.info'

    name = fields.Selection(
    selection=[
        ('fever', "Fever"),
        ('infection', "Infection"),
        ('pain', "Pain Killer"),
        ('vitamin', "Vitamin"),
    ],
    string="Type"
)


    description = fields.Text("Description")
    product_id=fields.Many2one("product.template")