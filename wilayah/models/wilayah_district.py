from odoo import models, fields

class District(models.Model):
    _name = "wilayah.district"
    _description = "District"

    name = fields.Char(string="District")
    code = fields.Char(string="District Code")
    city_id = fields.Many2one("wilayah.city", string="City")