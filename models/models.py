# -*- coding: utf-8 -*-

# from odoo import models, fields, api

# class sales_ext(models.Model):
#     _name = 'sales_ext.sales_ext'
#     _description = 'sales_ext.sales_ext'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
