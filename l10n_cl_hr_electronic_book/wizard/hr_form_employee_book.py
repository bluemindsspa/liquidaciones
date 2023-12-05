from odoo import api, fields, models
from datetime import datetime
import base64


class hr_salary_employee_bymonth(models.TransientModel):

    _name = 'hr.salary.employee.month'
    _description = 'Libro de Remuneraciones Haberes'

    def _get_default_end_date(self):
        date = fields.Date.from_string(fields.Date.today())
        return date.strftime('%Y') + '-' + date.strftime('%m') + '-' + date.strftime('%d')

    end_date = fields.Date(string='End Date', required=True, default=_get_default_end_date)

    def get_payslip_lines_value_2(self, obj, regla):
        valor = 0
        lineas = self.env['hr.payslip.line']
        detalle = lineas.search([('slip_id', '=', obj.id),('code', '=', regla)])
        valor = detalle.amount
        return int(round(valor))



    @api.model
    def get_tramo_asignacion_familiar(self, payslip, valor):
        if payslip.contract_id.carga_familiar != 0 and payslip.indicadores_id.asignacion_familiar_tercer >= payslip.contract_id.wage and payslip.contract_id.pension is False:
            if payslip.indicadores_id.asignacion_familiar_primer >= valor:
                return 'A'
            elif payslip.indicadores_id.asignacion_familiar_segundo >= valor:
                return 'B'
            elif payslip.indicadores_id.asignacion_familiar_tercer >= valor:
                return 'C'
        else:
            return ''

    def get_header_report(self):
        header = 'Rut trabajador(1101);Fecha inicio contrato(1102);Fecha término de contrato(1103);Causal término de contrato(1104);Región prestación de servicios(1105);Comuna prestación de servicios(1106);Tipo impuesto a la renta(1170);Técnico extranjero exención cot. previsionales(1146);Código tipo de jornada(1107);Persona con Discapacidad - Pensionado por Invalidez(1108);Pensionado por vejez(1109);AFP(1141);IPS (ExINP)(1142);FONASA - ISAPRE(1143);AFC(1151);CCAF(1110);Org. administrador ley 16.744(1152);Nro cargas familiares legales autorizadas(1111);Nro de cargas familiares maternales(1112);Nro de cargas familiares invalidez(1113);Tramo asignación familiar(1114);Rut org sindical 1(1171);Rut org sindical 2(1172);Rut org sindical 3(1173);Rut org sindical 4(1174);Rut org sindical 5(1175);Rut org sindical 6(1176);Rut org sindical 7(1177);Rut org sindical 8(1178);Rut org sindical 9(1179);Rut org sindical 10(1180);Nro días trabajados en el mes(1115);Nro días de licencia médica en el mes(1116);Nro días de vacaciones en el mes(1117);Subsidio trabajador joven(1118);Puesto Trabajo Pesado(1154);APVI(1155);APVC(1157);Indemnización a todo evento(1131);Tasa indemnización a todo evento(1132);Sueldo(2101);Sobresueldo(2102);Comisiones(2103);Semana corrida(2104);Participación(2105);Gratificación(2106);Recargo 30% día domingo(2107);Remun. variable pagada en vacaciones(2108);Remun. variable pagada en clausura(2109);Aguinaldo(2110);Bonos u otras remun. fijas mensuales(2111);Tratos(2112);Bonos u otras remun. variables mensuales o superiores a un mes(2113);Ejercicio opción no pactada en contrato(2114);Beneficios en especie constitutivos de remun(2115);Remuneraciones bimestrales(2116);Remuneraciones trimestrales(2117);Remuneraciones cuatrimestral(2118);Remuneraciones semestrales(2119);Remuneraciones anuales(2120);Participación anual(2121);Gratificación anual(2122);Otras remuneraciones superiores a un mes(2123);Pago por horas de trabajo sindical(2124);Sueldo empresarial (2161);Subsidio por incapacidad laboral por licencia médica(2201);Beca de estudio(2202);Gratificaciones de zona(2203);Otros ingresos no constitutivos de renta(2204);Colación(2301);Movilización(2302);Viáticos(2303);Asignación de pérdida de caja(2304);Asignación de desgaste herramienta(2305);Asignación familiar legal(2311);Gastos por causa del trabajo(2306);Gastos por cambio de residencia(2307);Sala cuna(2308);Asignación trabajo a distancia o teletrabajo(2309);Depósito convenido hasta UF 900(2347);Alojamiento por razones de trabajo(2310);Asignación de traslación(2312);Indemnización por feriado legal(2313);Indemnización años de servicio(2314);Indemnización sustitutiva del aviso previo(2315);Indemnización fuero maternal(2316);Pago indemnización a todo evento(2331);Indemnizaciones voluntarias tributables(2417);Indemnizaciones contractuales tributables(2418);Cotización obligatoria previsional (AFP o IPS)(3141);Cotización obligatoria salud 7%(3143);Cotización voluntaria para salud(3144);Cotización AFC - trabajador(3151);Cotizaciones técnico extranjero para seguridad social fuera de Chile(3146);Descuento depósito convenido hasta UF 900 anual(3147);Cotización APVi Mod A(3155);Cotización APVi Mod B hasta UF50(3156);Cotización APVc Mod A(3157);Cotización APVc Mod B hasta UF50(3158);Impuesto retenido por remuneraciones(3161);Impuesto retenido por indemnizaciones(3162);Mayor retención de impuestos solicitada por el trabajador(3163);Impuesto retenido por reliquidación remun. devengadas otros períodos(3164);Diferencia impuesto reliquidación remun. devengadas en este período(3165);Retención préstamo clase media 2020 (Ley 21.252) (3166);Rebaja zona extrema DL 889 (3167);Cuota sindical 1(3171);Cuota sindical 2(3172);Cuota sindical 3(3173);Cuota sindical 4(3174);Cuota sindical 5(3175);Cuota sindical 6(3176);Cuota sindical 7(3177);Cuota sindical 8(3178);Cuota sindical 9(3179);Cuota sindical 10(3180);Crédito social CCAF(3110);Cuota vivienda o educación(3181);Crédito cooperativas de ahorro(3182);Otros descuentos autorizados y solicitados por el trabajador(3183);Cotización adicional trabajo pesado - trabajador(3154);Donaciones culturales y de reconstrucción(3184);Otros descuentos(3185);Pensiones de alimentos(3186);Descuento mujer casada(3187);Descuentos por anticipos y préstamos(3188);AFC - Aporte empleador(4151);Aporte empleador seguro accidentes del trabajo y Ley SANNA(4152);Aporte empleador indemnización a todo evento(4131);Aporte adicional trabajo pesado - empleador(4154);Aporte empleador seguro invalidez y sobrevivencia(4155);APVC - Aporte Empleador(4157);Total haberes(5201);Total haberes imponibles y tributables(5210);Total haberes imponibles no tributables(5220);Total haberes no imponibles y no tributables(5230);Total haberes no imponibles y tributables(5240);Total descuentos(5301);Total descuentos impuestos a las remuneraciones(5361);Total descuentos impuestos por indemnizaciones(5362);Total descuentos por cotizaciones del trabajador(5341);Total otros descuentos(5302);Total aportes empleador(5410);Total líquido(5501);Total indemnizaciones(5502);Total indemnizaciones tributables(5564);Total indemnizaciones no tributables(5565)'
        return header

    def library(self):
        self.ensure_one()
        data = {'ids': self.env.context.get('active_ids', [])}
        res = self.read()
        res = res and res[0] or {}
        data.update({'form': res})
        date = data['form']['end_date'].strftime('%Y-%m-%d')
        data['form']['end_date'] = date
        get_employee2 = self.env['report.l10n_cl_hr_electronic_book.report_hrsalarybymonth'].get_employee2(data['form'])
        company = self.env.company
        file_name = 'libro de remuneraciones.csv'
        lines = []
        header = self.get_header_report()
        lines.append(header)
        for emp in get_employee2:
            contract_obj = self.env['hr.contract'].search([('id', '=', emp[16])])
            payslip_obj = self.env['hr.payslip'].search([('id', '=', emp[17])])
            tramo = self.get_tramo_asignacion_familiar(payslip_obj, self.get_payslip_lines_value_2(payslip_obj, 'TOTIM')),
            leave110 = payslip_obj.worked_days_line_ids.filtered(lambda f: f.code == 'LEAVE110')
            leave120 = payslip_obj.worked_days_line_ids.filtered(lambda f: f.code == 'LEAVE120')
            comi = payslip_obj.line_ids.filtered(lambda f: f.code == 'COMI')
            agui = payslip_obj.line_ids.filtered(lambda f: f.code == 'AGUI')
            col = payslip_obj.line_ids.filtered(lambda f: f.code == 'COL')
            mov = payslip_obj.line_ids.filtered(lambda f: f.code == 'MOV')
            viasan = payslip_obj.line_ids.filtered(lambda f: f.code == 'VIASAN')
            afp = payslip_obj.line_ids.filtered(lambda f: f.code == 'AFP')
            fonasa = payslip_obj.line_ids.filtered(lambda f: f.code == 'FONASA')
            isapre = payslip_obj.line_ids.filtered(lambda f: f.code == 'COLMENA')
            adisa = payslip_obj.line_ids.filtered(lambda f: f.code == 'ADISA')
            seceemp = payslip_obj.line_ids.filtered(lambda f: f.code == 'SECEEMP')
            sece = payslip_obj.line_ids.filtered(lambda f: f.code == 'SECE')
            impuni = payslip_obj.line_ids.filtered(lambda f: f.code == 'IMPUNI')
            cajacomp = payslip_obj.line_ids.filtered(lambda f: f.code == 'CAJACOMP')
            pccaf = payslip_obj.line_ids.filtered(lambda f: f.code == 'PCCAF')
            retjud = payslip_obj.line_ids.filtered(lambda f: f.code == 'RETJUD')
            sants = payslip_obj.line_ids.filtered(lambda f: f.code == 'SANTS')
            tod = payslip_obj.line_ids.filtered(lambda f: f.code == 'TOD')
            mut = payslip_obj.line_ids.filtered(lambda f: f.code == 'MUT')
            apv = payslip_obj.line_ids.filtered(lambda f: f.code == 'APV')
            hab = payslip_obj.line_ids.filtered(lambda f: f.code == 'HAB')
            totim = payslip_obj.line_ids.filtered(lambda f: f.code == 'TOTIM')
            totnoi = payslip_obj.line_ids.filtered(lambda f: f.code == 'TOTNOI')
            tde = payslip_obj.line_ids.filtered(lambda f: f.code == 'TDE')
            todele = payslip_obj.line_ids.filtered(lambda f: f.code == 'TODELE')
            aporte = payslip_obj.line_ids.filtered(lambda f: f.code == 'APORTE')
            liq = payslip_obj.line_ids.filtered(lambda f: f.code == 'LIQ')
            falp = payslip_obj.line_ids.filtered(lambda f: f.code == 'FALP')
            library = ''
            name = ''
            if emp[2]:
                name += emp[2]
            if emp[3]:
                name += ' ' + emp[3]
            if emp[4]:
                name += ' ' + emp[4]
            if emp[5]:
                name += ' ' + emp[5]
            if '.' in  str(emp[1]):
                rut = str(emp[1].replace('.',''))
            else:
                rut = str(emp[1])
            library += str(rut.lstrip("0")) + ';' # Rut trabajador(1101)
            ################# Fecha inicio contrato ##################
            date_start = datetime.strftime(contract_obj.date_start, '%d/%m/%Y')
            date_end = datetime.strftime(contract_obj.date_end, '%d/%m/%Y') if contract_obj.date_end else ''
            library += str(date_start)+ ';' # Fecha inicio contrato(1102)
            library += str(date_end) + ';' # Fecha termino Fecha término de contrato(1103)
            if date_end:
                codigo_causal = str(contract_obj.causal_id.codigo)
            else:
                codigo_causal = ''
            library += codigo_causal + ';' # Causal de termino Causal término de contrato(1104)
            library += str(company.state_id.code) + ';' # Codigo Region Región prestación de servicios(1105)
            library += str(company.city_id.code) + ';' # Codigo Comuna Comuna prestación de servicios(1106)
            library += '1' + ';' # Tipo de impuesto a la renta Tipo impuesto a la renta(1170)
            library += '0' + ';' # Tecnico extranjero Técnico extranjero exención cot. previsionales(1146)
            library += '101' + ';' # Codigo tipo de jornada Código tipo de jornada(1107)
            library += '0' + ';' # Discapacidad Persona con Discapacidad - Pensionado por Invalidez(1108)
            pensionado = '0'
            if contract_obj.pension:
                pensionado = '1'
            library += pensionado + ';' # Pensionado Pensionado por vejez(1109)
            library += str(contract_obj.afp_id.codigo_rem) + ';' # codigo rem AFP AFP(1141)
            library += '0' + ';' # Indice prevision social IPS IPS (ExINP)(1142)
            library += str(contract_obj.isapre_id.codigo_rem) + ';' # Prestacion de Salud (Isapre Id) FONASA - ISAPRE(1143)
            afc1151 = '0'
            if contract_obj.type_id.name == 'Plazo Indefinido':
                afc1151 = '1'
            library += afc1151 + ';' # AFC (Isapre Id) AFC(1151)
            library += str(payslip_obj.indicadores_id.ccaf_id.codigo_rem) + ';' # Caja de Compensacion codigo CCAF(1110)
            mutual = '0''1' if contract_obj.pension else '0'
            if payslip_obj.indicadores_id.mutual_seguridad_bool:
                mutual = str(int(payslip_obj.indicadores_id.mutualidad_id.codigo))
            library += mutual + ';' # Mutual Org. administrador ley 16.744(1152)
            library += str(contract_obj.carga_familiar) + ';' # Cargas familiares Nro cargas familiares legales autorizadas(1111)
            carga_maternal = ''
            if contract_obj.carga_familiar_maternal:
                carga_maternal = str(contract_obj.carga_familiar_maternal)
            library += carga_maternal + ';' # Cargas familiares Nro de cargas familiares maternales(1112)
            carga_invalida = ''
            if contract_obj.carga_familiar_invalida:
                carga_invalida = str(contract_obj.carga_familiar_invalida)
            library += carga_invalida + ';' # Cargas familiares Nro de cargas familiares invalidez(1113)
            library += str(tramo[0]) + ';' # Asignacion Familiar Tramo asignación familiar(1114)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1171)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1172)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1173)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1174)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1175)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1176)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1177)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1178)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1179)
            library += '' + ';' # Rut Sindical Rut org sindical 1(1180)
            library += str(int(emp[6])) + ';' # Dias trabajados Nro días trabajados en el mes(1115)
            nod_leave110 = ''
            if leave110:
                nod_leave110 = str(leave110.number_of_days)
            library += nod_leave110 + ';' # Licencia Medica Nro días de licencia médica en el mes(1116)
            nod_leave120 = ''
            if leave120:
                nod_leave120 = str(leave110.number_of_days)
            library += nod_leave120 + ';' # Vacaciones Nro días de vacaciones en el mes(1117)
            library += '0' + ';' # Subsidio trabajador joven(1118)
            library += '' + ';' # Puesto Trabajo Pesado(1154)
            val_apv = '0'
            if contract_obj.apv_id:
                val_apv = '1'
            library += val_apv + ';' # APV APVI(1155)
            library += '0' + ';' # APV Colectivo APVC(1157)
            library += '0' + ';' # Indemnizacion Indemnización a todo evento(1131)
            library += '' + ';' # Tasa indemnización a todo evento(1132)
            library += str(int(emp[7])) + ';' # Sueldo Sueldo(2101)
            library += '' + ';' # Sobresueldo Sobresueldo(2102)
            comi_val = ''
            if comi:
                comi_val = str(int(comi))
            library += comi_val + ';' # Comisiones(2103)
            library += '' + ';' # Semana corrida(2104)
            library += '0' + ';' # Participación(2105)
            library += str(int(emp[9])) + ';' # Gratificación(2106)
            library += str(int(emp[8])) + ';' # Recargo 30% día domingo(2107)
            library += '' + ';' # Remun. variable pagada en vacaciones(2108)
            library += '' + ';' # Remun. variable pagada en clausura(2109)
            agui_val = ''
            if agui:
                agui_val = str(int(agui))
            library += agui_val + ';' # Aguinaldo(2110)
            library += '' + ';' # Bonos u otras remun. fijas mensuales(2111)
            library += '0' + ';' # Tratos(2112)
            library += str(int(emp[10])) + ';' # Bonos u otras remun. variables mensuales o superiores a un mes(2113)
            library += '' + ';' # Ejercicio opción no pactada en contrato(2114)
            library += '' + ';' # Beneficios en especie constitutivos de remun(2115)
            library += '' + ';' # Remuneraciones bimestrales(2116)
            library += '' + ';' # Remuneraciones trimestrales(2117)
            library += '' + ';' # Remuneraciones cuatrimestral(2118)
            library += '' + ';' # Remuneraciones semestrales(2119)
            library += '' + ';' # Remuneraciones anuales(2120)
            library += '' + ';' # Participación anual(2121) Gratificación anual(2122)
            library += '' + ';' # Gratificación anual(2122)
            library += '' + ';' # Otras remuneraciones superiores a un mes(2123)
            library += '' + ';' # Pago por horas de trabajo sindical(2124)
            library += '' + ';' # Sueldo empresarial(2161)
            library += '' + ';' # Subsidio por incapacidad laboral por licencia médica(2201)
            library += '' + ';' # Beca de estudio(2202)
            library += '' + ';' # Gratificaciones de zona(2203)
            library += '' + ';' # Otros ingresos no constitutivos de renta(2204)
            col_val = ''
            if col:
                col_val = str(int(col.total))
            library += col_val + ';' # Colación(2301)
            mov_val = ''
            if mov:
                mov_val = str(int(mov.total))
            library += mov_val + ';' # Movilización(2302)
            viasan_val = ''
            if viasan and viasan.total:
                viasan_val = str(viasan.total)
            library += viasan_val + ';' # Viáticos(2303)
            library += '' + ';' # Asignación de pérdida de caja(2304)
            library += '0' + ';' # Asignación de desgaste herramienta(2305)
            library += str(int(emp[12])) + ';' # Asignación familiar legal(2311)
            library += '' + ';' # Gastos por causa del trabajo(2306)
            library += '' + ';' # Gastos por cambio de residencia(2307)
            library += '' + ';' # Sala cuna(2308)
            library += '' + ';' # Asignación trabajo a distancia o teletrabajo(2309)
            library += '' + ';' # Depósito convenido hasta UF 900(2347)
            library += '' + ';' # Alojamiento por razones de trabajo(2310)
            library += '' + ';' # Asignación de traslación(2312)
            library += '' + ';' # Indemnización por feriado legal(2313)
            library += '' + ';' # Indemnización años de servicio(2314)
            library += '' + ';' # Indemnización sustitutiva del aviso previo(2315)
            library += '' + ';' # Indemnización fuero maternal(2316)
            library += '' + ';' # Pago indemnización a todo evento(2331)
            library += '' + ';' # Indemnizaciones voluntarias tributables(2417)
            library += '' + ';' # Indemnizaciones contractuales tributables(2418)
            afp_val = ''
            if afp:
                afp_val = str(int(afp.total))
            library += afp_val + ';' # AFP Cotización obligatoria previsional (AFP o IPS)(3141)
            fonasa_isapre = ''
            if fonasa:
                fonasa_isapre = str(int(fonasa.total))
            else:
                fonasa_isapre = str(int(isapre.total))
            library += fonasa_isapre + ';' # ISAPRE o FONASA Cotización obligatoria salud 7%(3143)
            adisa_val = ''
            if adisa:
                adisa_val = str(int(adisa.total))
            library += adisa_val + ';' # Cotización voluntaria para salud(3144)
            sece_val = ''
            if sece:
                sece_val = str(int(sece.total))
            library += sece_val + ';' # Cotización AFC - trabajador(3151)
            library += '' + ';' # Cotizaciones técnico extranjero para seguridad social fuera de Chile(3146)
            library += '' + ';' # Descuento depósito convenido hasta UF 900 anual(3147)
            library += '' + ';' # Cotización APVi Mod A(3155)
            library += '' + ';' # Cotización APVi Mod B hasta UF50(3156)
            library += '' + ';' # Cotización APVc Mod A(3157)
            library += '' + ';' # Cotización APVc Mod B hasta UF50(3158)
            impuni_val = '0'
            if impuni:
                impuni_val = str(int(impuni.total))
            library += impuni_val + ';' # Impuesto retenido por remuneraciones(3161)
            library += '' + ';' # Impuesto retenido por indemnizaciones(3162)
            library += '' + ';' # Mayor retención de impuestos solicitada por el trabajador(3163)
            library += '' + ';' # Impuesto retenido por reliquidación remun. devengadas otros períodos(3164)
            library += '' + ';' # Diferencia impuesto reliquidación remun. devengadas en este período(3165)
            library += '' + ';' # Retención préstamo clase media 2020 (Ley 21.252) (3166)
            library += '' + ';' # Rebaja zona extrema DL 889 (3167)
            library += '' + ';' # Cuota sindical 1(3171)
            library += '' + ';' # Cuota sindical 1(3172)
            library += '' + ';' # Cuota sindical 1(3173)
            library += '' + ';' # Cuota sindical 1(3174)
            library += '' + ';' # Cuota sindical 1(3175)
            library += '' + ';' # Cuota sindical 1(3176)
            library += '' + ';' # Cuota sindical 1(3177)
            library += '' + ';' # Cuota sindical 1(3178)
            library += '' + ';' # Cuota sindical 1(3179)
            library += '' + ';' # Cuota sindical 1(3180)
            cajacomp_val = ''
            if cajacomp:
                cajacomp_val = str(int(cajacomp.total))
            library += cajacomp_val + ';' # Caja de Compensacion Crédito social CCAF(3110)
            library += '' + ';' # Cuota vivienda o educación(3181)
            pccaf_val = ''
            if pccaf:
                pccaf_val = str(int(pccaf.total))
            library += pccaf_val + ';'  # Pago Prestamos Caja de Compensacion Crédito cooperativas de ahorro(3182)
            library += '' + ';'  # Otros descuentos autorizados y solicitados por el trabajador(3183)
            library += '' + ';'  # Cotización adicional trabajo pesado - trabajador(3154)
            library += '' + ';'  # Donaciones culturales y de reconstrucción(3184)
            falp_val = ''
            if falp:
                falp_val = str(int(falp.total))
            library += falp_val + ';'  # Otros descuentos(3185)
            retjud_val = ''
            if retjud:
                retjud_val = str(int(retjud.total))
            library += retjud_val + ';'  # Pensiones de alimentos(3186)
            library += '' + ';'  # Descuento mujer casada(3187)
            sants_val = ''
            if sants:
                sants_val = str(int(sants.total))
            library += sants_val + ';'  # Descuentos por anticipos y préstamos(3188)
            seceemp_val = ''
            if seceemp:
                seceemp_val = str(int(seceemp.total))
            library += seceemp_val + ';' # AFC - Aporte empleador(4151)
            mut_val = '0'
            if mut:
                mut_val = str(int(mut.total))
            library += mut_val + ';' # Mutual Aporte empleador seguro accidentes del trabajo y Ley SANNA(4152)
            library += '' + ';' # Aporte empleador indemnización a todo evento(4131)
            library += '' + ';' # Aporte adicional trabajo pesado - empleador(4154)
            library += '0' + ';' # Aporte empleador seguro invalidez y sobrevivencia(4155)
            apv_val = ''
            if apv:
                apv_val = str(int(apv.total))
            library += apv_val + ';'  # APVC - Aporte Empleador(4157)
            hab_val = '0'
            if hab:
                hab_val = str(int(hab.total))
            library += hab_val + ';'  # Total haberes(5201)
            totim_val = '0'
            if totim:
                totim_val =  str(int(totim.total))
            library += totim_val + ';'  # Total haberes imponibles y tributables(5210)
            library += '0' + ';'  # Total haberes imponibles no tributables(5220)
            totnoi_val = '0'
            if totnoi:
                totnoi_val = str(int(totnoi.total))
            library += totnoi_val + ';'  # Total haberes no imponibles y no tributables(5230)
            library += '0' + ';'  # Total haberes no imponibles y tributables(5240)
            tde_val = '0'
            if tde:
                tde_val = str(int(tde.total))
            library += tde_val + ';'  # Total descuentos(5301)
            library += impuni_val + ';'  # Total descuentos impuestos a las remuneraciones(5361)
            library += '' + ';'  # Total descuentos impuestos por indemnizaciones(5362)
            todele_val = '0'
            if todele:
                todele_val = str(int(todele.total))
            library += todele_val + ';'  # Total descuentos por cotizaciones del trabajador(5341)
            tod_val = '0'
            if tod:
                tod_val = str(int(tod.total))
            library += tod_val + ';'  # Total otros descuentos(5302)
            aporte_val = '0'
            if aporte:
                aporte_val = str(int(aporte.total))
            library += aporte_val + ';'  # Total aportes empleador(5410)
            liq_val = '0'
            if liq:
                liq_val = str(int(liq.total))
            library += liq_val + ';'  # Total líquido(5501)
            library += '' + ';'  # Total indemnizaciones(5502)
            library += '0' + ';'  # Total indemnizaciones tributables(5564)
            library += ''  # Total indemnizaciones no tributables(5565)
            lines.append(library)
       
        output = ''
        for line in lines:
            output += line + '\n'

        data = base64.encodebytes(output.encode('windows-1252')),

        doc = self.env['ir.attachment'].create({
            'name': '%s' % (file_name),
            'datas': data[0],
            'store_fname': '%s' % (file_name),
            'type': 'binary'
        })
           
        return {
            'type': "ir.actions.act_url",
            'url': "web/content/?model=ir.attachment&id=" + str(
                doc.id) + "&filename_field=name&field=datas&download=true&filename=" + str(doc.name),
            'target': "self",
            'no_destroy': False,
        }
    
        


    def print_report(self):
        """
         To get the date and print the report
         @return: return report
        """
        self.ensure_one()
        data = {'ids': self.env.context.get('active_ids', [])}
        res = self.read()
        res = res and res[0] or {}
        data.update({'form': res})
        return self.env.ref('l10n_cl_hr_electronic_book.hr_salary_books').report_action(self, data=data)
