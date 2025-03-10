# -*- coding: utf-8 -*-
{
    'name': "Wilayah",
    'summary': """
        Starting module for "Discover the JS framework, chapter 1: Owl components"
    """,

    'description': """
        Starting module for "Discover the JS framework, chapter 1: Owl components"
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",

    'category': 'Tutorials/Wilayah',
    'version': '0.1',

    'depends': ['base'],
    'application': True,
    'installable': True,
    'license': 'AGPL-3',
    'data': [
      'security/ir.model.access.csv',
    #   'data/wilayah.provinsi.csv',
    #   'data/wilayah.kota.csv',
    #   'data/wilayah.kecamatan.csv',
    #   'data/wilayah.desa.csv',
      'views/provinsi_view.xml',
      'views/kota_view.xml',
      'views/kecamatan_view.xml',
      'views/desa_view.xml',
      'views/res_partner_form.xml'
    ]
}
