# -*- coding:utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from dateutil.relativedelta import relativedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_no = fields.Char(string='Employee No.')
    function = fields.Char(string='Function')
    bank_details = fields.Char(string='Bank Details')
    ifsc = fields.Char(string='IFSC Code')
    tax_regime = fields.Char(string='Tax Regime')
    income_tax_no = fields.Char(string='Income Tax Number (PAN)')
    universal_account_no = fields.Char(string='Universal Account Number (UAN)')
    pf_account_number = fields.Char(string='PF Account Number')
    esi_number = fields.Char(string='ESI Number')
    pr_account_number = fields.Char(string='PR Account Number (PRAN)')

class HrPayslipInherit(models.Model):
    _inherit = 'hr.payslip'

    def get_amount_in_words(self,amount):
        return self.env.user.company_id.currency_id.amount_to_text(amount)