from odoo import fields, models, api


class DocSurgery(models.Model):
    _name = 'doc.doc_surgery'
    _description = 'Description'

    surgery_id = fields.Many2one('res.partner', domain=[('is_surgery', '=', True)], string="surgery", required=True)
    name = fields.Char(string='surgery name')
    surgery_debit = fields.Float(string='surgery debit')
    state = fields.Selection([('open', 'open'), ('close', 'close'), ('append', 'append')], string="surgery state",defualt='open')
    activity_states = fields.Char(string="activity state", default='open')

    @api.model
    def default_get(self, fields):
        rec = super(DocSurgery, self).default_get(fields)
        rec['state'] = 'open'
        rec['activity_states'] = 'open'
        return rec
