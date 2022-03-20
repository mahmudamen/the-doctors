from odoo import fields, models, api


class DocDoctor(models.Model):
    _name = 'doc.doc_doctor'
    _description = 'doctors list'

    name = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string="doctor name", required= True)
    job = fields.Selection([('doctor', 'doctor'), ('drug', 'drug'), ('assist', 'assist')], string="doctor state",
                             defualt='doctor')
    state = fields.Selection([('open', 'open'), ('close', 'close'), ('append', 'append')], string="doctor state",
                             defualt='open')
    activity_states = fields.Char(string="activity state", default='open')

    @api.model
    def default_get(self, fields):
        rec = super(DocDoctor, self).default_get(fields)
        rec['job'] = 'doctor'
        rec['state'] = 'open'
        rec['activity_states'] = 'open'
        return rec
