# -*- coding: utf-8 -*-
{
    'name': "doctors",
    "version": "13.0.0.2",
    "currency": 'EGP',
    'summary': """
        the doctors
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        The Doctors
    """,

    'author': "Xamltech",
    'website': "http://www.xamltech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Industries",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'account', 'sale'],

    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'security/doctors_security.xml',
        'security/ir.model.access.csv',
        'views/main_menu_file.xml',
        'views/doc_reg.xml',
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "author": "Mahmudamen",
    "website": "https://mahmudamen.github.io/ten/",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": ["static/description/icon.png"],
}
