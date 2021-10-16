from odoo import api, fields, models, _
from datetime import date,datetime


class DocMech(models.Model):
    _name = 'doc.doc_mech'
    _description = 'machine list'

    name = fields.Char(string='machine name')
    mech_debit = fields.Float(string='machine debit')
    state = fields.Selection([('open','open'),('close','close'),('append','append')],string="machine state", defualt='open' )
    activity_states = fields.Char(string="activity state",default='open' )

    @api.model
    def default_get(self,fields):
        rec = super(DocMech,self).default_get(fields)
        rec['state'] = 'open'
        rec['activity_states'] = 'open'
        return rec