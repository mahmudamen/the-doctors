# -*- coding: utf-8 -*-
# from odoo import http


# class Doctors(http.Controller):
#     @http.route('/doctors/doctors/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/doctors/doctors/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('doctors.listing', {
#             'root': '/doctors/doctors',
#             'objects': http.request.env['doctors.doctors'].search([]),
#         })

#     @http.route('/doctors/doctors/objects/<model("doctors.doctors"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('doctors.object', {
#             'object': obj
#         })
