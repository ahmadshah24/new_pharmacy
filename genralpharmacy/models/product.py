from datetime import date, timedelta
from odoo import models, fields, api


class ProductInherit(models.Model):
    _inherit = "product.template"
    _description = "sharq_investment.sharq_employee"

    manufacture_date = fields.Date(string="Manufacture Date")
    expiration_date = fields.Date(string="Expiration Date")
    cat_id = fields.Many2one("odoo.medicine.category", replace="categ_id")
    com_id = fields.Many2one("odoo.medicine.company")
    type_id = fields.Many2one("pharmacy.medicine.type")
    doze = fields.Char(string="Doze")
    unite_id = fields.Many2one("medicine.unite")


    expiration_alert = fields.Boolean(
        compute="_compute_expiration_alert", string="Expiration Alert"
    )

    @api.depends("expiration_date")
    def _compute_expiration_alert(self):
        today = date.today()
        two_months = timedelta(days=60)
        for product in self:
            if product.expiration_date:
                remaining_days = (product.expiration_date - today).days
                if remaining_days <= two_months.days:
                    product.expiration_alert = True
                else:
                    product.expiration_alert = False
            else:
                product.expiration_alert = False
