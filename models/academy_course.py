from odoo import models, fields, api


class academyCourse(models.Model):
    _name = 'academy.course'
    _description = 'openacademy Course '
    name = fields.Char(string='title', required=True)
    description = fields.Text()
