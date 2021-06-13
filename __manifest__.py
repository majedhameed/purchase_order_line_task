# -*- coding: utf-8 -*-
{
    'name': "purchase_order_line_task",

    'summary': """
       This Mudule Perform the folloing tasks Show sale price, cost, and last purchase price in purchase order line:""",

    'description': """
        In purchase order lines show product cost and sale price.
        In purchase order line show the last purchase price for the given vendor product and unit of measure from previous purchase orders.
    """,

    'author': "MajedShogaa",
    'website': "majedshogaa@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/purchase_order_line.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
