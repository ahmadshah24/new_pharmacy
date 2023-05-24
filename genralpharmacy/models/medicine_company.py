# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MedicineCompany(models.Model):
    _name = 'odoo.medicine.company'
    _description = 'medicine.company.info'

    name = fields.Char("Name")
    phone = fields.Integer("Phone")
    email = fields.Char("Email")
    address = fields.Char("Address")

    product_id=fields.Many2one("product.template")