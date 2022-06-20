from odoo import models, fields, api


class academySession(models.Model):
    _name = "academy.session"
    _description = "academy session to show courses session details"

    name = fields.Char(string="name", required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in day")
    number_of_seat = fields.Integer(string="number of seats")


