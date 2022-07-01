from odoo import models, fields, api


class academySession(models.Model):
    _name = "academy.session"
    _description = "academy session to show courses session details"

    name = fields.Char(string="name", required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in day")
    number_of_seat = fields.Integer(string="number of seats")
    instructor_id = fields.Many2one('res.partner', string='instructor', index=True, ondelete='cascade')
    course_id = fields.Many2one('academy.course', string='Courses', required=True, ondelete='cascade')
    attendence_ids = fields.Many2many('res.partner', string='set of attendees')
    taken_seats = fields.Float(string="taken seats ", compute="_taken_seats")

    @api.depends("attendence_ids", "number_of_seat")
    def _taken_seats(self):
        for record in self:
            if not record.number_of_seat:
                record.taken_seats = 0.0
            else:
                record.taken_seats = (100*len(record.attendence_ids) / record.number_of_seat)
