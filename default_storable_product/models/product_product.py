from odoo import api, fields, _, models
from odoo.exceptions import ValidationError, RedirectWarning, UserError


class ProductProductInherit(models.Model):
    _inherit = 'product.product'

    available_in_pos = fields.Boolean(default=True)
