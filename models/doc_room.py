from odoo import fields, models, api


class DocRoom(models.Model):
    _name = 'doc.doc_room'
    _description = 'doc room'

    name = fields.Many2one('res.partner',domain=[('is_room','=',True)],string="room name", required= True)
    room_grade = fields.Integer(string="room grade")
    room_number = fields.Integer(string="room number")
    room_price = fields.Float(string='room price')
    room_type = fields.Selection([('a','class a'),('b','class b'),('c','class c'),('d','class d')],string='room types')
    room_attach = fields.Float(string='room attach')
    state = fields.Selection([('open', 'open'), ('close', 'close'), ('append', 'append')], string="room state",
                             defualt='open')
    activity_states = fields.Char(string="activity state", default='open')

    @api.model
    def default_get(self, fields):
        rec = super(DocRoom, self).default_get(fields)
        rec['state'] = 'open'
        rec['activity_states'] = 'open'
        return rec