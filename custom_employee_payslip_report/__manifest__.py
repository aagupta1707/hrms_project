# -*- coding: utf-8 -*-

{
    'name': 'Employee Payslip',
    'version': '13.0.1.0.0',
    'category': 'Human Resources',
    'sequence': 75,
    'author': '',
    'summary': """Centralize employee information""",
    'description': """Employee Master""",
    'website': '',
    
    'depends': [
        'base',
        'hr',
        'hr_attendance',
        'om_hr_payroll',
        'report_xlsx',
    ],
    'data': [
        'views/employee_view.xml',
        'report/report_employee_payslip_template.xml',
        'report/report_employee_payslip.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
