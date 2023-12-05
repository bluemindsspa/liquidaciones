# -*- coding: utf-8 -*-
{
    'name': "Comunas Chile",

    'summary': """
        Comunas Chile
    """,

    'description': """
        Comunas Chile
    """,

    'author': "Blueminds",
    'website': "http://blueminds.cl",
    'contribuitors': "Frank Quatromani <fquatromani@blueminds.cl>",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_address_extended'],

    # always loaded
    'data': [
        'data/comunas.xml',
        'views/res_partner_views.xml',
    ],
}
