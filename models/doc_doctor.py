from odoo import fields, models, api


class DocDoctor(models.Model):
    _name = 'doc.docdoctor'
    _description = 'doctors list'

    doctor_id = fields.Many2one('res.partner', domain=[('is_doctor', '=', True)], string="doctor", required=True)
    name = fields.Char(string='doctor name')
    state = fields.Selection([('open', 'open'), ('close', 'close'), ('append', 'append')], string="doctor state",
                             defualt='open')
    activity_states = fields.Char(string="activity state", default='open')

    @api.model
    def default_get(self, fields):
        rec = super(DocDoctor, self).default_get(fields)
        rec['state'] = 'open'
        rec['activity_states'] = 'open'
        return rec
