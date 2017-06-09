# -*- coding: utf-8 -*-
# Copyright 2017 Davide Corio
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class AccountPaymentTerm(models.Model):

    _inherit = 'account.payment.term'

    # default company not set. this way it's easiere if you
    # want to share payment terms across different companies
    company_id = fields.Many2one('res.company', string='Company')
