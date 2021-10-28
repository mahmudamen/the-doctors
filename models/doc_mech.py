from odoo import api, fields, models, _
from datetime import date,datetime


class DocMech(models.Model):
    _name = 'doc.doc_mech'
    _description = 'machine list'

    name = fields.Many2one('res.partner',domain=[('is_mech','=',True)],string="mech name", required= True)
    mech_debit = fields.Float(string='machine debit')
    reg_state = fields.Selection([('open','open'),('close','close'),('append','append')],string="machine state", defualt='open' )
    activity_states = fields.Char(string="activity state",default='open' )
    currency_id = fields.Many2one('res.currency', 'Currency', default=lambda self: self.env.company.currency_id.id, required=True)
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True,default=lambda self: self.env.company)
    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)

    @api.model
    def default_get(self,fields):
        rec = super(DocMech,self).default_get(fields)
        rec['state'] = 'draft'
        rec['activity_states'] = 'open'
        return rec