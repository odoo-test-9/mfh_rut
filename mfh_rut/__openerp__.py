# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2016 MARLON FALCON HDEZ (<http://www.marlonfalcon.cl>).
# contact: contacto@marlonfalcon.cl

######################################################################

# __openerp__.py

{
    'name': 'Rut mfh-1',
    'version': '1.0',
    'author': 'Marlon Falcon Hernandez',
    'category': 'Accounting & Finance',
    'summary': 'Ejemplo de un módulo de Odoo',
    'sequence': 30,
    'website': 'https://www.marlonfalcon.cl',
    'description': """
Es un módulo de ejemplo
======================
Con este modulo haremos nuestra primera aplicación en Odoo.
 * Uno
 * Dos
Nota: Necesita Ventas.
    """,
    'license' : 'AGPL-3',
    'depends': ['sale','base_setup', 'product', 'analytic', 'report'],
    'data': [
        'res_company_view.xml',
    ],
    'installable': True,
    'active': False,
    'auto_install': False,
}