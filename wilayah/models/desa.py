from odoo import models, fields

class Desa(models.Model):
    _name = "wilayah.desa"
    _description = "Desa model"

    name = fields.Char(string="Desa")
    kode = fields.Char(string="Kode")
    kecamatan_id = fields.Many2one("wilayah.kecamatan", 'id', string="Kecamatan")