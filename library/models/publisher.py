from odoo import models, fields


class Publisher(models.Model):
    _name = "library.publisher"
    _description = "Publisher"
    _rec_name = "f_name"

    f_name = fields.Char(string="First Name")
    l_name = fields.Char(string="Last Name")
    date_joined = fields.Date()
    active = fields.Boolean(default=True)
    national_id = fields.Char(string="National ID")
    image = fields.Binary()
    book_ids = fields.One2many("library.book", "publisher_id")
    new_books_ids = fields.Many2many("library.book")

