from odoo import fields, models, api
import logging

logger = logging.getLogger(__name__)

class InheritedPartner(models.Model):
    _inherit = "res.partner"

    subdistrict_id = fields.Many2one("wilayah.subdistrict", string="Subdistrict")
    city_id = fields.Many2one("wilayah.city", string="City")
    district_id = fields.Many2one("wilayah.district", string="District")
    is_indonesia = fields.Boolean(compute="_is_indonesia", store=True)

    @api.depends('country_id')
    def _is_indonesia(self):
        for record in self:
            if record.country_id.name == "Indonesia":
                record.is_indonesia = True
            else:
                record.is_indonesia = False

    @api.onchange("country_id")
    def _ochange_state_id(self):
        self.state_id = None
        self.city_id = None
        self.district_id = None
        self.subdistrict_id = None
        self.city = ""

    @api.onchange("state_id")
    def _ochange_state_id(self):
        self.city_id = None
        self.district_id = None
        self.subdistrict_id = None
        self.city = ""

    @api.onchange("city_id")
    def _ochange_city_id(self):
        for record in self:
            record.district_id = None
            record.subdistrict_id = None
            try:
                record.city = record.city_id.name.title()
            except:
                record.city = ""

    @api.onchange("district_id")
    def _ochange_district_id(self):
        self.subdistrict_id = None
