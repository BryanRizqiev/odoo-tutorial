from odoo import fields, models, api

class InheritedUser(models.Model):
    _inherit = "res.partner"

    desa_id = fields.Many2one("wilayah.desa", string="Desa")
    kota_id = fields.Many2one("wilayah.kota", string="Kota")
    kecamatan_id = fields.Many2one("wilayah.kecamatan", string="Kecamatan")
    provinsi_id = fields.Many2one("wilayah.provinsi", string="Provinsi")

    @api.onchange("provinsi_id")
    def _ochange_provinsi_id(self):
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
