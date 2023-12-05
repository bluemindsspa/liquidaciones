# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
from datetime import datetime

class hr_payslip_employees(models.TransientModel):
    _inherit = 'hr.payslip.employees'

    #@api.multi
    def compute_sheet(self):
        HrIndicadores = self.env['hr.indicadores']
        indicadores = False
        if 'default_date_start' in self.env.context:
            from_date = fields.Date.to_date(self.env.context.get('default_date_start'))
            indicadores_id = HrIndicadores.search([('month', '=', from_date.month), ('year', '=', from_date.year)])
        if self.env.context.get('active_id'):
            indicadores_id = self.env['hr.payslip.run'].browse(self.env.context.get('active_id')).indicadores_id.id
        if not indicadores_id:
            raise UserError("No ha generado registro de indicadores para el periodo %s %s" % (datetime.strftime(from_date, '%B'), from_date.year))
        return super(hr_payslip_employees, self.with_context(default_indicadores_id=indicadores_id)).compute_sheet()

