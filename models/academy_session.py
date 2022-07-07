from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import UserError


class academySession(models.Model):
    _name = "academy.session"
    _description = "academy session to show courses session details"

    name = fields.Char(string="name", required=True)
    start_date = fields.Date(default=fields.Date.today)
    active = fields.Boolean(default=True)
    duration = fields.Float(digits=(6, 2), help="Duration in day")
    number_of_seat = fields.Integer(string="number of seats")
    instructor_id = fields.Many2one('res.partner', string='instructor', index=True, ondelete='cascade')
    course_id = fields.Many2one('academy.course', string='Courses', required=True, ondelete='cascade')
    attendence_ids = fields.Many2many('res.partner', string='set of attendees')
    taken_seats = fields.Float(string="taken seats ", compute="_taken_seats")
    number_of_attendence = fields.Integer(compute="get_number_of_attendence", store=True)
    color =fields.Integer()
    @api.depends("attendence_ids")
    def get_number_of_attendence(self):
        for record in self:
            record.number_of_attendence = len(record.attendence_ids)

    @api.depends("attendence_ids", "number_of_seat")
    def _taken_seats(self):
        for record in self:
            if not record.number_of_seat:
                record.taken_seats = 0.0
            else:
                record.taken_seats = (100 * len(record.attendence_ids) / record.number_of_seat)

    @api.onchange("attendence_ids", "number_of_seat")
    def _on_change(self):
        if self.number_of_seat < 0:
            return {
                'warning': {
                    'title': 'invalid Number',
                    'message': 'number of seats must be positive',
                },
            }
        if self.number_of_seat < len(self.attendence_ids):
            return {
                'warning': {
                    'title': "invalid number",
                    'message': 'number of attends is greater than number of seats',
                },
            }

    @api.constrains('instructor_id', 'attendence_ids')
    def check_instructor(self):
        for record in self:
            if record.instructor_id in record.attendence_ids:
                raise UserError("instructor must be in attendence")
