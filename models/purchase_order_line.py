# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class purchase_order_line_addition(models.Model):
    _name = 'purchase.order.line'
    _inherit = 'purchase.order.line'
    sale_price = fields.Float(
        string='Sale Price', store=False, related='product_id.list_price')
    standard_price = fields.Float(
        string='Cost', store=False, related='product_id.standard_price')
    last_purchase_price = fields.Float(
        "Last Purchase Price", compute='_compute_last_purchase_price', store=False, readonly=True)

    @api.onchange('product_id')
    def _compute_last_purchase_price(self):
        for order_line in self:
            order_line_item = self.env['purchase.order.line'].search([('product_id', '=',order_line.product_id.id)], limit=1)
            order_line.last_purchase_price = order_line_item.price_unit
