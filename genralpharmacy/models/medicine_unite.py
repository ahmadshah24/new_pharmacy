# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MedicineUnite(models.Model):
    _name = 'medicine.unite'
    _description = 'medicine.company.unite'

    name = fields.Char("Name")
