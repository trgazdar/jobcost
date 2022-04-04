# Copyright 2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    group_contracted_disable_adding_lines = fields.Boolean(
        string='Disable adding more lines to SOs',
        implied_group='sale_contracted_order.contracted_orders_disable_adding_lines')
