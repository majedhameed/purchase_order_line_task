# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderLine(http.Controller):
#     @http.route('/purchase_order_line/purchase_order_line/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_line/purchase_order_line/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_line.listing', {
#             'root': '/purchase_order_line/purchase_order_line',
#             'objects': http.request.env['purchase_order_line.purchase_order_line'].search([]),
#         })

#     @http.route('/purchase_order_line/purchase_order_line/objects/<model("purchase_order_line.purchase_order_line"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_line.object', {
#             'object': obj
#         })
