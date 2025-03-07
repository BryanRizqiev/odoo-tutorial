from odoo import models, fields

class Kota(models.Model):
    _name = "wilayah.kota"
    _description = "Kota model"

    name = fields.Char(string="Kota")
    kode = fields.Char(string="Kode")
    provinsi_id = fields.Many2one("wilayah.provinsi", string="Provinsi")