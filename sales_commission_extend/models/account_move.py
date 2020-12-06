
from odoo import _, api, fields, models

class AccountMove(models.Model):
    _inherit = "account.move"
    
    @api.model
    def create(self, vals):
        res = super(AccountMove, self).create(vals)
        sale = self.env['sale.order'].search([('name', '=', res.invoice_origin)])
        if sale:
            for rec in sale:
                if rec.product_comm_level_ids:
                    vals = []
                    for lin in rec.product_comm_level_ids:
                        vals.append({
                            'invoice_id': res.id,
                            'commission_level_id': lin.commission_level_id.id,
                            'user_partner_id': lin.user_partner_id.id,
                            })
                    level = self.env['product.commission.level'].create(vals)

        return res
