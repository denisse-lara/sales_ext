# -*- coding: utf-8 -*-
# from odoo import http


# class SalesExt(http.Controller):
#     @http.route('/sales_ext/sales_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_ext/sales_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_ext.listing', {
#             'root': '/sales_ext/sales_ext',
#             'objects': http.request.env['sales_ext.sales_ext'].search([]),
#         })

#     @http.route('/sales_ext/sales_ext/objects/<model("sales_ext.sales_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_ext.object', {
#             'object': obj
#         })
