# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# res_company.py

from openerp.osv import fields, osv
from openerp.tools.translate import _

class res_partner(osv.osv):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_columns = {
	   'rut' : fields.char('Rut' , size=10 , help='Este es rut'),
	   'emaildte' : fields.char('Emaildte' , size=256 , help='Este es mail para el dte'),
	   'giro' : fields.char('Giro' , size=256 , help='Este es el Giro'),
	}


	_defaults = {
       'giro' : 'Obras de Inegieria',
	}

res_partner()