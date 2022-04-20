from odoo import models, fields, api


class CreateLocation(models.Model):
    _inherit = 'project.project'

    location_id = fields.Many2one('stock.location', string='Stock Location')

    @api.model
    def create(self, vals):
        result = super(CreateLocation, self).create(vals)
        result = self.env['stock.location'].create(
            {'name': result['name']})
        return result

