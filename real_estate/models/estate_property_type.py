from odoo import fields, models, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type model"

    name = fields.Char('Name', required=True)
    estate_ids = fields.One2many("estate.property", "property_type_id", string="Estate")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    property_ids = fields.One2many(
        'estate.property', 'property_type_id', string="Properties"
    )
    offer_ids = fields.One2many(related="property_ids.offer_ids")
    offer_count = fields.Integer("Offer Count", compute="_compute_offer_count", readonly=True)

    _sql_constraints = [
        ("unique_name", "unique(name)", "The type name already created"),
    ]

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.property_ids.mapped('offer_ids'))


