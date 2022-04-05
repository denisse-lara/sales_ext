# -*- coding: utf-8 -*-
{
    "name": "sales_ext",
    "summary": """
        Sales app extention""",
    "description": """
        Sales app extention
    """,
    "author": "Denisse Lara",
    "website": "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale_management", "hr"],
    # always loaded
    "data": [
        # "security/ir.model.access.csv",
        # "views/employee.xml",
        "views/order.xml",
        "views/menus.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
