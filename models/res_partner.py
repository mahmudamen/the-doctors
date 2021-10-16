# -*- coding: utf-8 -*-
# Part of Nuca Erp create by Mahmudamen. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class res_partner(models.Model):
    _inherit = 'res.partner'

    relationship = fields.Char(string='Relationship')
    relative_partner_id = fields.Many2one('res.partner',string="Relative_id")
    is_doctor = fields.Boolean(string="Doctor")
    is_patient = fields.Boolean(string='Patient')
    is_surgery = fields.Boolean(string='Surgery')
    is_patient_relative = fields.Boolean(string='Patient Relative')
    is_doctor_drugs = fields.Boolean(string='Doctor Drugs')
    is_doctor_assist = fields.Boolean(string='Doctor Assist')
    is_nurse = fields.Boolean(string='Nurse')
    reference = fields.Char('ID Number')


