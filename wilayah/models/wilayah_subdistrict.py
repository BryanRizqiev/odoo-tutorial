from odoo import models, fields

class Subdistrict(models.Model):
    _name = "wilayah.subdistrict"
    _description = "Subdistrict"

    name = fields.Char(string="Subdistrict")
    code = fields.Char(string="Subdistrict Code")
    district_id = fields.Many2one("wilayah.district", string="District")