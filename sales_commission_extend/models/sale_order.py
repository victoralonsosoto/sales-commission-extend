
from odoo import _, api, fields, models

class SaleCommissionLine(models.Model):
    _inherit = "sale.order"


    @api.onchange('pricelist_id')
    def onchange_pricelist_id(self):
        for rec in self:
            if rec.pricelist_id:
                if rec.product_comm_level_ids:
                    rec.product_comm_level_ids = [(5, 0, 0)]
                    if rec.user_id.partner_id.commission_ids:
                        sales = 0
                        for lin in rec.user_id.partner_id.commission_ids:
                            sales = lin.commission_level_id.id
                        rec.product_comm_level_ids.create({
                            'sale_order_id': rec.id,
                            'commission_level_id': sales,
                            'user_partner_id': rec.user_id.partner_id.id,
                           
                        })
                    else:
                        rec.product_comm_level_ids.create({
                            'sale_order_id': rec.id,
                            'user_partner_id': rec.user_id.partner_id.id,
                           
                        })
                else:
                    if rec.user_id.partner_id.commission_ids:
                        sales = 0
                        for lin in rec.user_id.partner_id.commission_ids:
                            sales = lin.commission_level_id.id
                        rec.product_comm_level_ids.create({
                            'sale_order_id': rec.id,
                            'commission_level_id': sales,
                            'user_partner_id': rec.user_id.partner_id.id,
                           
                        })
                    else:
                        rec.product_comm_level_ids.create({
                            'sale_order_id': rec.id,
                            'user_partner_id': rec.user_id.partner_id.id,
                           
                        })
