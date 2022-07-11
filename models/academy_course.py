from odoo import models, fields, api


class academyCourse(models.Model):
    _name = 'academy.course'
    _description = 'openacademy Course '
    name = fields.Char(string='title', required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string='Resonsible', ondelete="set null", index=True)
    session_ids = fields.One2many('academy.session', 'course_id', string='Session')
    _sql_constraints = [
        ("Check Name", "CHECK(name != description)", "name of course must be different about description"
         ),
        ("UNIQUE NAME", "UNIQUE(name)", "Course Name already Exist")
    ]

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}

        if not default.get('name'):
            default['name'] = f"copy of {self.name}"
        return super(academyCourse, self).copy(default)
