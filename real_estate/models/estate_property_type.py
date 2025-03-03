# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type model"

    name = fields.Char('Name', required=True)
    estate_ids = fields.One2many("estate.property", "property_type_id", string="Estate")

