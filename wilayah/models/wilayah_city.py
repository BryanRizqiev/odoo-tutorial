from odoo import models, fields

class City(models.Model):
    _name = "wilayah.city"
    _description = "City"

    name = fields.Char(string="City")
    province_code = fields.Char(string="Province Code")
    code = fields.Char(string="City Code")
    state = fields.Many2one("res.country.state", string="Province")