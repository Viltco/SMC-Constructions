from odoo import models, fields, api


class StockField(models.Model):
    _inherit = 'stock.location'

    project_id = fields.Many2one('project.project', string='Project')


