# -*- coding: utf-8 -*-
{
    'name': "Purchase Default Storable Product",
    'summary': """ 
        This module allows to add (product category, product quantity on hand, product sales price and 
        coefficient of margin) column in the purchase order line and also to set product type to 
        storable Product and check in product available in pos while creating and editing product 
        in the Purchase.
    """,
    'description': """
        This module allows to add (product category, product quantity on hand, product sales price and 
        coefficient of margin) column in the purchase order line and also to set product type to 
        storable Product and check in product available in pos while creating and editing product 
        in the Purchase.    
    """,
    'author': "Cabrel Tchomte",
    'website': "http://www.innovations-groups.com",
    'category': 'Purchase',
    'version': '13.0.1.0',
    'price': 10,
    'currency': "USD",
    "license": "OPL-1",
    'depends': ['purchase'],
    'data': ['views/purchase_orderline_stock.xml'],
    'images': ['static/description/df_mainscree.png',
               'static/description/df_producttype.png',
               'static/description/df_available_pos.png'],
    "installable": True,
    "application": True,
    "auto_install": False,
}
