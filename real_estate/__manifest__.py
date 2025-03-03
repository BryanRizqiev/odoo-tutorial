# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': """
        Starting module for "Discover the JS framework, chapter 1: Owl components"
    """,

    'description': """
        Starting module for "Discover the JS framework, chapter 1: Owl components"
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",

    'category': 'Tutorials/Real Estate',
    'version': '0.1',

    'depends': ['base', 'auth_totp', 'base_import', 'base_import_module', 'base_setup', 'bus', 'html_editor', 'iap', 'web', 'web_editor', 'web_tour', 'web_unsplash'],
    'application': True,
    'installable': True,
    'license': 'AGPL-3',
    'data': [
      'security/ir.model.access.csv',
      'views/estate_property_views.xml',
      'views/property_offer_views.xml',
    ]
}
