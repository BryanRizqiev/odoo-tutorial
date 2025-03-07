from odoo import models, fields

class Provinsi(models.Model):
    _name = "wilayah.provinsi"
    _description = "Provinsi model"

    name = fields.Char(string="Provinsi")