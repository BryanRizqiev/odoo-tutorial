from random import randint
from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag model"

    name = fields.Char("Name", required=True)
    property_id = fields.Many2one("estate.property", string="Property", ondelete="cascade")
    color = fields.Integer(
        string="Color Index", default=lambda self: self._default_color(),
        help="Tag color.")

    _sql_constraints = [
        ("unique_name", "unique(name)", "The tag name already created"),
    ]

    def _default_color(self):
        return randint(1, 11)
