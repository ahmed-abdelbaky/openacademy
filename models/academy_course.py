from odoo import models, fields, api


class academyCourse(models.Model):
    _name = 'academy.course'
    _description = 'openacademy Course '
    name = fields.Char(string='title', required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string='Resonsible', ondelete="set null", intex=True)
    session_ids = fields.One2many('academy.session', 'course_id', string='Session')
    _sql_constraints = [
        ("Check Name", "CHECK(name != description)", "name of course must be different about description"
         ),
        ("UNIQUE NAME", "UNIQUE(name)", "Course Name already Exist")
    ]
