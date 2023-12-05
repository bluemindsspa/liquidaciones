{
    'name': "Libro de Remuneraciones Electrónico",

    'summary': """
        Libro de Remuneraciones Electrónico
    """,

    'description': """
        Libro de Remuneraciones Electrónico
    """,

    'author': "Blueminds",
    'website': "http://blueminds.cl",
    'contribuitors': "Frank Quatromani <fquatromani@blueminds.cl>",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'l10n_cl_hr',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/report_hrsalarybymonth.xml',
        'views/hr_salary_books.xml'
    ],

    'installable': True,
    'auto_install': False,
    'demo': [],
    'test': [],
}
# -*- coding: utf-8 -*-
