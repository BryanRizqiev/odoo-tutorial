from odoo import fields, models, api
import logging

logger = logging.getLogger(__name__)

class InheritedUser(models.Model):
    _inherit = "res.partner"

    desa_id = fields.Many2one("wilayah.desa", string="Desa")
    kota_id = fields.Many2one("wilayah.kota", string="Kota")
    kecamatan_id = fields.Many2one("wilayah.kecamatan", string="Kecamatan")

    @api.onchange("state_id")
    def _ochange_state_id(self):
        self.kota_id = None
        self.kecamatan_id = None
        self.desa_id = None

    @api.onchange("kota_id")
    def _ochange_kota_id(self):
        self.kecamatan_id = None
        self.desa_id = None

    @api.onchange("kecamatan_id")
    def _ochange_kecamatan_id(self):
        self.desa_id = None
