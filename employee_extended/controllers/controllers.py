# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeExtended(http.Controller):
#     @http.route('/employee_extended/employee_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_extended/employee_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_extended.listing', {
#             'root': '/employee_extended/employee_extended',
#             'objects': http.request.env['employee_extended.employee_extended'].search([]),
#         })

#     @http.route('/employee_extended/employee_extended/objects/<model("employee_extended.employee_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_extended.object', {
#             'object': obj
#         })
