# -*- coding: utf-8 -*-
# Part of Xamltech. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from dateutil.relativedelta import relativedelta

class DocReg(models.Model):
    _inherit = ['sale.order']
    _order = 'id desc'
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



    date_of_birth = fields.Date(string="Date of Birth")
    sex = fields.Selection([('m', 'Male'), ('f', 'Female')], string="Sex")
    age = fields.Char(compute=onchange_age, string="Patient Age", store=True)
    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1, context={'default_is_patient': 1},
        domain="['|', ('company_id', '=', False),  ('is_patient', '=', True),('company_id', '=', company_id)]", )

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
    reg_surgery = fields.Many2one('doc.doc_surgery',domain=[('state','=','open')],string="surgery")
    reg_date_out = fields.Date(string='patient date out')
    reg_day = fields.Float(string='count days')
    r_name = fields.Many2one('res.partner',domain=[('state','=','open')],string="patient's relative" )
    r_level = fields.Char(string="patient's relative level")
    r_id = fields.Integer(string="patient relative id national")
    r_job = fields.Char(string="patient relative job")
    r_address = fields.Char(string='patient relative address')
    r_tel = fields.Char(string='patient relative mobile')
    doc_name = fields.Many2one(
        'res.partner', string='Doctor name', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('is_doctor', '=', 1),('company_id', '=', company_id)]",)
    doc_drugs = fields.Many2one(
        'res.partner', string='Drugs Doctor', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('is_doctor_drugs', '=', 1),('company_id', '=', company_id)]",)
    doc_assist = fields.Many2one(
        'res.partner', string='Assist Doctor', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False),('is_doctor_assist', '=', 1), ('company_id', '=', company_id)]",)
    nurse_name = fields.Many2one(
        'res.partner', string='Nurse Name', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False),('is_nurse', '=', 1), ('company_id', '=', company_id)]",)
    ensure = fields.Float(string='ensure')
    reg_other_debit = fields.Float(string='patient other debit')
    reg_flag = fields.Selection([('1', 'open patient'), ('0', 'close patient')],default='1', string="patinet flag")
    reg_state = fields.Char(string='patient state')
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def action_patient_open(self):
        self.reg_flag = "1"
        self.reg_state = "open patient"

    def action_patient_close(self):
        self.reg_flag = "0"
        self.reg_state = "close patient"


    attach_flag = fields.Selection([('1', 'attach'), ('0', 'no attach')],default='0', string="attach flag")
    attach_room = fields.Float('attach room debit')
    reg_mech = fields.Many2one('doc.doc_mech',string='machine name',domain=[('state','=','open')])
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


    order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True, auto_join=True)


    @api.model
    def default_get(self,fields):
        rec = super(DocReg,self).default_get(fields)
        rec['reg_flag'] = '1'
        return rec

class SaleOrderLineReg(models.Model):
    _inherit = 'sale.order.line'

    doc_reg_id = fields.Many2one('sale.order', string='Reg Reference',  ondelete='cascade', index=True, copy=False)
    is_medical = fields.Boolean(string="Is Medical item")
    is_consumables = fields.Boolean(string='Is Consumables')

class ProductProductReg(models.Model):
    _inherit = 'product.product'

    is_medical = fields.Boolean(string="Is Medical item")
    is_consumables = fields.Boolean(string='Is Consumables')

class ProductProductTemplateReg(models.Model):
    _inherit = 'product.template'

    is_medical = fields.Boolean(string="Is Medical item")
    is_consumables = fields.Boolean(string='Is Consumables')