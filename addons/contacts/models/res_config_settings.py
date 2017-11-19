# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_phone_validation = fields.Boolean(string="Phone Validation")
    phone_valid_method = fields.Selection(related="company_id.phone_international_format", required=True)
