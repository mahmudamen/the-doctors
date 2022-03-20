from odoo import fields, models, api


class DocNurse(models.Model):
    _name = 'doc.doc_nurse'
    _description = 'nurse list'

    name = fields.Many2one('res.partner',domain=[('is_nurse','=',True)],string="nurse name", required= True)
    state = fields.Selection([('open', 'open'), ('close', 'close'), ('append', 'append')], string="nurse state",
                             defualt='open')
    activity_states = fields.Char(string="activity state", default='open')

    @api.model
    def default_get(self, fields):
        rec = super(DocNurse, self).default_get(fields)
        rec['state'] = 'open'
        rec['activity_states'] = 'open'
        return rec
