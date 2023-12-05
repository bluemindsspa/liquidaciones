{
    'name': ' Chilean Payroll Account Menu in Human Resources',
    'author': 'Blueminds',
    'website': 'https://www.blueminds.cl',
    'license': 'AGPL-3',
    'depends': ['base', 'l10n_cl_hr', 'hr_payroll_account'],
    'license': 'AGPL-3',
    'version': '14.0.0.0.0',
    'description': "Permite unir las liquidaciones de sueldo a Contabilidad",
    'category': 'Localization/Chile',
    'data': [
            'views/menu_root.xml',
            'views/report_payslip.xml',
            # 'data/hr_centros_costos.xml', # error: plan_id es obligatorio
            'data/account_journal.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
