# -*- coding: utf-8 -*-
{
    'name': "POS Payment Analysis",

    'summary': """
    """,

    'description': """
POS Payment Analysis
====================
    """,

    'author': "Aasim Ahmed Ansari",
    'website': "http://aasimania.wordpress.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point Of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/point_of_sale_security.xml',
        'security/ir.model.access.csv',
        'report/pos_order_payment_report_view.xml'
    ],
}