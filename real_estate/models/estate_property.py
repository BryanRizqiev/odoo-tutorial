# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo import exceptions
import logging
from odoo.tools.float_utils import float_compare, float_is_zero

_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property model"
    _order = "id desc"

    name = fields.Char("Name", default="Unknown", required=True)
    description = fields.Text("Description", required=True)
    postcode = fields.Char("Postcode", required=True)
    date_availability = fields.Datetime("Available From", default=fields.Date.today(), readonly=True)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True)
    bedrooms = fields.Integer("Bedrooms", required=True, default=2)
    living_area = fields.Integer("Living Area (sqm)", required=True)
    facades = fields.Integer("Facades", required=True)
    garage = fields.Boolean("Garage", required=True)
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")],
        help="Garden orientation"
    )
    active = fields.Boolean(required=True, default=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type", required=True)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    state = fields.Selection(
        string='Status',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('canceled', 'Canceled'), ('sold', 'Sold')],
        default='new',
        readonly=True,
    )
    best_offer = fields.Float("Best Offer", compute="_compute_best_offer", store=True)
    salesman_id = fields.Many2one('res.users', string='Salesman', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    offer_ids = fields.One2many(
        'estate.property.offer',
        'property_id',
        string='Offers',
    )

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The tag name already created'),
    ]

    @api.constrains('expected_price', 'selling_price')
    def _check_selling_price(self):
        for property_record in self:
            if float_is_zero(property_record.expected_price, precision_digits=2):
                continue

            lower_limit = property_record.expected_price * 0.9
            if float_compare(property_record.selling_price, lower_limit, precision_digits=2) == -1:
                raise exceptions.ValidationError("Selling price cannot be lower than 90% of the expected price.")

    def button_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError("A sold property cannot be calceled.")
            record.write({'state': 'canceled'})

    def button_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise exceptions.UserError("A canceled property cannot be sold.")
            record.write({'state': 'sold'})

    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for property_record in self:
            property_record.best_offer = max(property_record.offer_ids.mapped('price'))