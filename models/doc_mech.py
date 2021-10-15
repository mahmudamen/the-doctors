from odoo import fields, models, api


class DocMech(models.Model):
    _name = 'doc.doc_mech'
    _description = 'machine list'

    mech_id = fields.Many2one('res.partner',domain=[('is_mech','=',True)],string="machine", required= True)
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