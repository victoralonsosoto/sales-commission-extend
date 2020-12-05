
from odoo import _, api, fields, models

class SaleCommissionLine(models.Model):
    _inherit = "sale.commission.line"


    def action_paid(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'paid'


