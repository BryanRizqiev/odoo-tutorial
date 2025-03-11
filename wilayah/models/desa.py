from odoo import models, fields

class Desa(models.Model):
    _name = "wilayah.desa"
    _description = "Desa model"

    name = fields.Char(string="Desa")
    code = fields.Char(string="Kode Desa")
    kecamatan_id = fields.Many2one("wilayah.kecamatan", string="Kecamatan")