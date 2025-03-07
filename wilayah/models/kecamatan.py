from odoo import models, fields

class Kecamatan(models.Model):
    _name = "wilayah.kecamatan"
    _description = "Kecamatan model"

    name = fields.Char(string="Kecamatan")
    kota_id = fields.Many2one("wilayah.kota", string="Kota")