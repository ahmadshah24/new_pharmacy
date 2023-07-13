from datetime import date, timedelta
from odoo import models, fields, api
from odoo import models, fields, api
import barcode
from barcode.writer import ImageWriter
import base64
import io
from PIL import Image
import os
from odoo.exceptions import ValidationError


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
 


    expiration_date = fields.Date("expariation_date")
    remaining_months = fields.Integer("Remaining Months", compute="_compute_remaining_months")

    @api.depends('expiration_date')
    def _compute_remaining_months(self):
        for record in self:
            if record.expiration_date:
                today = fields.Date.today()
                remaining_days = (record.expiration_date - today).days
                remaining_months = remaining_days // 30
                record.remaining_months = remaining_months
            else:
                record.remaining_months = 0


    

    barcode_number = fields.Char(string='Barcode Number')

    barcode_image = fields.Binary(string='Barcode Image')
    barcode_image_path = fields.Char(string='Barcode Image Path')
     
    def generate_barcode(self):
        barcode_data = str(self.barcode_number)  # Convert barcode number to a string
        barcode_image_name = '{}.png'.format(self.name)  # Use the product name as the barcode image name
        barcode_image_dir = os.path.expanduser('~/Desktop/barcodes/')
        os.makedirs(barcode_image_dir, exist_ok=True)  # Create the directory if it doesn't exist
        barcode_image_path = os.path.join(barcode_image_dir, barcode_image_name)

        # Save the barcode image as a PNG file
        barcode_image = barcode.get('code128', barcode_data, writer=ImageWriter())
        barcode_image.save(barcode_image_path)
  

    
            
    @api.constrains('barcode_number')
    def _check_unique_barcode_number(self):
        for record in self:
            if self.search_count([('barcode_number', '=', record.barcode_number)]) > 1:
                raise ValidationError('Barcode number must be unique.')




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



