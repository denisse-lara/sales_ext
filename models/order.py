# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Order(models.Model):
    _inherit = "sale.order"

    salesperson = fields.Many2one("hr.employee", string="Salesperson")
