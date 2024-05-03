from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, exceptions


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char('Title', required=True)
    code = fields.Char()
    _sql_constraints = [
        ("unique_code", "unique('code')", "Code must be unique")
    ]
    active = fields.Boolean(default=True)
    date_published = fields.Date()
    age = fields.Integer(compute='_compute_age')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('published', 'Published'),
    ], default='draft')

    image = fields.Binary()
    publisher_id = fields.Many2one("library.publisher")

    def action_add_publisher(self):
        action = self.env['ir.actions.actions']._for_xml_id('library.publisher_wizard_action')
        action['context'] = {
            'default_book_id': self.id,
        }
        return action

    # @api.constrains("publisher_id")
    # def _check_publisher_id(self):
    #     for book in self:
    #         if not book.publisher_id:
    #             raise exceptions.ValidationError("Publisher is required")

    def confirm(self):
        for rec in self:
            rec.state = "confirm"

    def published(self):
        for rec in self:
            rec.state = "published"

    def draft(self):
        for rec in self:
            rec.state = "draft"

    @api.model
    def _create(self, vals):
        res = super(Book, self)._create(vals)
        print("inside create method")
        return res

    def write(self, vals):
        res = super(Book, self).write(vals)
        print("inside write method")
        return res

    def unlink(self):
        res = super(Book, self).unlink()
        print("inside unlink method")
        return res

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, access_rights_uid=None):
        res = super(Book, self)._search(args, offset=0)
        print("inside search method")
        return res

    @api.depends('date_published')
    def _compute_age(self):
        for rec in self:
            if rec.date_published:
                rec.age = relativedelta(fields.Date.today(), rec.date_published).years
            else:
                rec.age = False
