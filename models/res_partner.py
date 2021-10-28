# -*- coding: utf-8 -*-
# Part of Nuca Erp create by Mahmudamen. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class res_partner(models.Model):
    _inherit = 'res.partner'

    relationship = fields.Char(string='Relationship')
    relative_partner_id = fields.Many2one('res.partner',string="Relative_id")
    is_doctor = fields.Boolean(string="Is Doctor")
    is_patient = fields.Boolean(string='Is Patient')
    is_mech = fields.Boolean(string="Is Mech")
    is_surgery = fields.Boolean(string='Is Surgery')
    is_patient_relative = fields.Boolean(string='Is Patient Relative')
    is_doctor_drugs = fields.Boolean(string='Is Doctor Drugs')
    is_doctor_assist = fields.Boolean(string='Is Doctor Assist')
    is_nurse = fields.Boolean(string='Is Nurse')
    is_room = fields.Boolean(string='Is Room')
    reference = fields.Char('ID Number')


