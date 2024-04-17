from odoo import api, models, fields

class SyncLogs(models.Model):
    _name = 'sync.logs'

    model_id = fields.Many2one(string="Model", comodel_name="ir.model")
    action = fields.Selection(string="Action",
                              selection=[('create', 'Create'), ('edit', 'Edit'), ('delete', 'Delete')])
    action_type = fields.Char(compute="get_action_type")
    # for the following fields there is no need to create the fields, but I've created the fields anyway
    # user name ==> can use create_uid
    # time ==> can use create_date
    user_id = fields.Many2one(string="User Name", comodel_name="res.users")
    time = fields.Datetime(string="Time")

    @api.depends('action_type')
    def get_action_type(self):
        for rec in self:
            rec.action_type = 'NEW' if rec.action == 'create' else "PERFORM"


class AbstractSyncLog(models.AbstractModel):
    _name = 'abstract.sync.logs'
    """
    This abstract class, SyncLog, is designed to eliminate code 
    duplication and simplify data synchronization across various models in your application.

    Benefits:

    Reduced Redundancy: By inheriting from SyncLog, you eliminate the need to write the same sync logs
     logic (e.g., logging changes) in each model class.
     
    Improved Maintainability: Centralizing sync logs 
    logic makes it easier to maintain and update in one place.
    
    Flexible Model Integration: Any model requiring sync logs can seamlessly inherit abstract.sync.logs,
     promoting code reusability
    """

    def get_model_id(self, model_name):
        return self.env['ir.model'].search([('model', '=', model_name)], limit=1).id

    @api.model
    def create(self, values):
        self.env['sync.logs'].create({
            'model_id': self.get_model_id(self._name),
            'action': 'create',
            'user_id': self.env.uid,  # also this could be removed and added as a default in user_id field
            'time': fields.Datetime.now(),
        })
        return super(AbstractSyncLog, self).create(values)

    def write(self, values):
        for rec in self:
            self.env['sync.logs'].create({
                'model_id': self.get_model_id(rec._name),
                'action': 'edit',
                'user_id': self.env.uid,  # also this could be removed and added as a default in user_id field
                'time': fields.Datetime.now(),
            })
        return super(AbstractSyncLog, self).write(values)

    def unlink(self):
        for rec in self:
            self.env['sync.logs'].create({
                'model_id': self.get_model_id(rec._name),
                'action': 'edit',
                'user_id': self.env.uid,  # also this could be removed and added as a default in user_id field
                'time': fields.Datetime.now(),
            })
        return super(AbstractSyncLog, self).unlink()


class OpStudentInherit(models.Model):
    _inherit = ['op.student', 'abstract.sync.logs']
    _name = 'op.student'


class OpParentInherit(models.Model):
    _inherit = ['op.parent', 'abstract.sync.logs']
    _name = 'op.parent'
