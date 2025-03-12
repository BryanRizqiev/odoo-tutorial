# -*- coding: utf-8 -*-
{
    'name': "Wilayah",
    'summary': """
        Modul untuk integrasi wilayah Indonesia
    """,

    'description': """
        Modul untuk integrasi wilayah Indonesia"
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
      'data/wilayah.city.csv',
      'data/wilayah.district.csv',
      'data/wilayah.subdistrict.csv',
      'views/city_view.xml',
      'views/district_view.xml',
      'views/subdistrict_view.xml',
      'views/res_partner_form.xml'
    ]
}
