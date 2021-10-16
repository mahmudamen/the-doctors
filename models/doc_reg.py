# -*- coding: utf-8 -*-
# Part of Xamltech. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta



class DocReg(models.Model):
    _name = 'doc.doc_reg'
    _rec_name = 'reg_id'
    _inherit = 'mail.thread'
    _description = 'New patient registration'

    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            else:
                rec.age = "No Date Of Birth!!"

    reg_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient", required= True)
    name = fields.Char(string='ID', readonly=True)
    last_name = fields.Char('Last Name')
    date_of_birth = fields.Date(string="Date of Birth")
    sex = fields.Selection([('m', 'Male'), ('f', 'Female')], string="Sex")
    age = fields.Char(compute=onchange_age, string="Patient Age", store=True)

    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            else:
                rec.age = "No Date Of Birth!!"

    photo = fields.Binary(string="Picture")
    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string="Blood Type")
    rh = fields.Selection([('-+', '+'), ('--', '-')], string="Rh")
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    reg_address = fields.Char(string="patient address")
    reg_date = fields.Date(string="patient registration date")
    reg_level = fields.Many2one('doc.doc_room',string="patient level")
    reg_room = fields.Char(string="patient room number")
    reg_bed = fields.Char(string='patient bed number')
    reg_reason = fields.Char(string='patient reason desc')
    reg_surgery = fields.Many2one('doc.doc_surgery',domain=[('is_surgery','=',True)],string="surgery")
    reg_date_out = fields.Date(string='patient date out')
    reg_day = fields.Float(string='count days')
    r_name = fields.Many2one('res.partner',domain=[('is_patient_relative','=',True)],string="patient's relative" )
    r_level = fields.Char(string="patient's relative level")
    r_id = fields.Integer(string="patient relative id")
    r_job = fields.Char(string="patient relative job")
    r_address = fields.Char(string='patient relative address')
    r_tel = fields.Char(string='patient relative mobile')
    doc_name = fields.Many2one('doc.doc_doctor',domain=[('is_doctor','=',True)],string="doctor")
    doc_drugs = fields.Many2one('doc.doc_doctor', domain=[('is_doctor_drugs', '=', True)], string="doctor drugs")
    doc_assist = fields.Many2one('doc.doc_doctor', domain=[('is_doctor_assist', '=', True)], string="doctor assist")
    nurse_name = fields.Many2one('doc.doc_nurse',domain=[('is_nurse','=',True)],string="nurse")
    ensure = fields.Float(string='ensure')
    reg_other_debit = fields.Float(string='patient other debit')
    reg_flag = fields.Selection([('1', 'open patient'), ('0', 'close patient')],default='1', string="patinet flag")
    reg_state = fields.Char(string='patient state')

    def action_patient_open(self):
        self.reg_flag = "1"
        self.reg_state = "open patient"

    def action_patient_close(self):
        self.reg_flag = "0"
        self.reg_state = "close patient"

    reg_discount = fields.Float(string='patient discount')
    reg_level_debit = fields.Float(string='level debit')
    reg_surgery_debit = fields.Float(string='surgery debit')
    attach_flag = fields.Selection([('1', 'attach'), ('0', 'no attach')],default='0', string="attach flag")
    attach_room = fields.Float('attach room debit')
    reg_mech = fields.Many2one('doc.doc_mech',string='machine name')
    reg_mech_debit = fields.Float(string='machine debit')

    @api.onchange('reg_mech')
    def onchange_reg_mech(self):
        if self.reg_mech:
            v = self.reg_mech[0]['id']
            for x in self:
                rec_mech_debit = self.env['doc.doc_mech'].search_read([('id', '=', v)])
                print(x.reg_mech[0])
            for rec in rec_mech_debit:
                self.reg_mech_debit = rec['mech_debit']


    def get_mech_debit(self):
        if self.reg_mech:
            v = self.reg_mech[0]['id']
            for x in self:
                rec_mech_debit = self.env['doc.doc_mech'].search_read([('id', '=', v)])
                print(x.reg_mech[0])
            for rec in rec_mech_debit:
                self.reg_mech_debit = rec['mech_debit']

    c_arm = fields.Float(string='c arm debit')

    @api.model
    def default_get(self,fields):
        rec = super(DocReg,self).default_get(fields)
        rec['reg_flag'] = '1'
        return rec
