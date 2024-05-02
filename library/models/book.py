from odoo import models, fields


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char('Title', required=True)
    code = fields.Char()
    active = fields.Boolean(default=True)
    date_published = fields.Date(default=fields.Date.context_today)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('published', 'Published'),
    ])

    image = fields.Binary()
    publisher_id = fields.Many2one("library.publisher")
