from odoo import models, fields, api


class partner(models.Model):

    _inherit = 'res.partner'
    instructor = fields.Boolean(string='Instructor')
    session_ids = fields.Many2many('academy.session', string='attendence', readonly=True)
