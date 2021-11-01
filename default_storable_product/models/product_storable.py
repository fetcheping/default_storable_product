from odoo import api, fields, _, models
from odoo.exceptions import ValidationError, RedirectWarning, UserError


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    type = fields.Selection(default='product')
    available_in_pos = fields.Boolean(default=True)


class PurchaseOrderLineInherit(models.Model):
    _inherit = 'purchase.order.line'

    in_stock = fields.Float(string='Stock', related='product_id.qty_available')
    quotient = fields.Float(string='Coef.Margin', compute='_compute_quotient')
    public_price = fields.Float(string='Sales Price', related='product_id.list_price')
    product_category = fields.Many2one(string='Category', related='product_id.categ_id', readonly=False)

    @api.depends(
        "public_price",
        "price_unit",
    )
    def _compute_quotient(self):
        for line in self:
            if line.public_price == 0 or line.price_unit == 0:
                line.quotient = 0
            else:
                line.quotient = line.public_price / line.price_unit
