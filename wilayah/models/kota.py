from odoo import models, fields

class Kota(models.Model):
    _name = "wilayah.kota"
    _description = "Kota model"

    name = fields.Char(string="Kota")
    province_code = fields.Char(string="Kode Provinsi")
    code = fields.Char(string="Kode Kota")
    state = fields.Many2one("res.country.state", string="State")