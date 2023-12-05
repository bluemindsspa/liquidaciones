from odoo import api, fields, models, tools, _


class hr_ccaf(models.Model):
    _name = 'hr.ccaf'
    _description = 'CCAF'
    
    codigo = fields.Char('Codigo', required=True)
    codigo_rem = fields.Char('Codigo Remuneraciones', required=True)
    name = fields.Char('Nombre', required=True)
