from odoo import models, fields

class Kota(models.Model):
    _name = "wilayah.kota"
    _description = "Kota model"

    name = fields.Char(string="Kota")
    kode_provinsi = fields.Char(string="Kode Provinsi")
    state = fields.Many2one("res.country.state", string="State")