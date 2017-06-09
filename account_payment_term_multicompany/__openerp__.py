# -*- coding: utf-8 -*-
# Copyright 2017 Davide Corio
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Payment Term Multicompany',
    'summary': """
        Multicompany Payment Terms""",
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Davide Corio,Odoo Community Association (OCA)',
    'website': 'http://davidecorio.com',
    'depends': [
        'account',
    ],
    'data': [
        'security/account_payment_term_security.xml',
        'views/account_payment_term.xml',
    ],
    'demo': [
    ],
}
