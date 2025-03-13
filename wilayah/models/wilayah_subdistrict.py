import base64
from odoo import models, fields, api
import logging
import os

cwd = os.getcwd()

logger = logging.getLogger(__name__)

class Subdistrict(models.Model):
    _name = "wilayah.subdistrict"
    _description = "Subdistrict"

    name = fields.Char(string="Subdistrict")
    code = fields.Char(string="Subdistrict Code")
    district_id = fields.Many2one("wilayah.district", string="District")

    @api.model
    def import_data_subdistrict(self):
        with open("../tutorial_odoo/wilayah/data/wilayah.subdistrict.csv", "rb") as file:
            import_cls = self.env['base_import.import'].create({
                'res_model': 'wilayah.subdistrict',
                'file': file.read(),
                'file_name': 'wilayah.subdistrict.csv',
                'file_type': 'text/csv',
            })

            return import_cls.execute_import(
                fields=['id', 'name', 'district_id/id', 'code'],
                columns=['id', 'name', 'district_id/id', 'code'],
                options={'import_skip_records': [], 
                         'import_set_empty_fields': [],
                         'fallback_values': {},
                         'name_create_enabled_fields': {},
                         'encoding': 'ascii',
                         'separator':',',
                         'quoting': '"',
                         'date_format': '',
                         'datetime_format': '',
                         'float_thousand_separator': ',',
                         'float_decimal_separator': '.',
                         'advanced': True,
                         'has_headers': True,
                         'keep_matches': False,
                         'sheets': [],
                         'sheet': '', 
                         'skip': 0,
                         'tracking_disable': True
                        }
            )