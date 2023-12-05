from odoo import fields, models


class City(models.Model):
    _inherit = 'res.city'

    code = fields.Char(string='Codigo')