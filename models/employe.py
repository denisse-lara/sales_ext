# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _inherit = "hr.employee"

    LOGGED_IN = "logged_in"
    BUSY = "busy"
    LOGGED_OUT = "logged_out"
    session_status = fields.Selection(
        [(LOGGED_IN, "Online"), (BUSY, "Busy"), (LOGGED_OUT, "Offline")], "Status"
    )

    orders = fields.One2many("sale_ext.order", "seller", "Orders")
    assigned_orders = fields.Integer(
        string="# of orders", compute="_compute_orders_total", copy=False, default=0
    )

    @api.depends("orders")
    def _compute_orders_total(self):
        self.assigned_orders = len(self.orders)
