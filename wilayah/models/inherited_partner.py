from odoo import fields, models, api
import logging

logger = logging.getLogger(__name__)

class InheritedUser(models.Model):
    _inherit = "res.partner"

    desa_id = fields.Many2one("wilayah.desa", string="Desa")
    kota_id = fields.Many2one("wilayah.kota", string="Kota")
    kecamatan_id = fields.Many2one("wilayah.kecamatan", string="Kecamatan")
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
        self.kota_id = None
        self.kecamatan_id = None
        self.desa_id = None
        self.city = ""

    @api.onchange("state_id")
    def _ochange_state_id(self):
        self.kota_id = None
        self.kecamatan_id = None
        self.desa_id = None
        self.city = ""

    @api.onchange("kota_id")
    def _ochange_kota_id(self):
        for record in self:
            record.kecamatan_id = None
            record.desa_id = None
            try:
                record.city = record.kota_id.name.title()
            except:
                record.city = ""

    @api.onchange("kecamatan_id")
    def _ochange_kecamatan_id(self):
        self.desa_id = None
