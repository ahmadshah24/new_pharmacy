# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MedicineType(models.Model):
    _name = 'pharmacy.medicine.type'
    _description = 'pharmacy.medicine.type.info'



    name = fields.Char(string="type")
    # name =fields.Many2one('pharmacy.medicine.type.parnet',string="Type")
    description = fields.Text("Description")


    # name2 = fields.Char(string="Type")
#     name = fields.Selection(
#     selection=[
#         ('fever', "Fever"),
#         ('infection', "Infection"),
#         ('pain', "Pain Killer"),
#         ('vitamin', "Vitamin"),
#     ],
#     string="Type"
# )


    # product_id=fields.Many2one("product.template")


# class MedicineTypeParnet(models.Model):
#     _name = 'pharmacy.medicine.type.parnet'
#     _description = 'pharmacy.medicine.type.parent.info'



#     name = fields.Char(string="Name")