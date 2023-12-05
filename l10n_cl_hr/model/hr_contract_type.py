from odoo import api, fields, models, tools, _


class hr_contract_type(models.Model):
    _name = 'hr.contract.type'
    _description = 'Tipo de Contrato'
    _order = 'sequence, id'

    name = fields.Char(string='Contract Type', required=True, translate=True)
    sequence = fields.Integer(help="Gives the sequence when displaying a list of Contract.", default=10)
    codigo = fields.Char('Codigo')


class hr_causal_termino(models.Model):
    _name = 'hr.causal.termino'
    _description = 'Causal termino de contrato'
    
    codigo = fields.Char('Codigo', required=True)
    name = fields.Char('Nombre', required=True)
