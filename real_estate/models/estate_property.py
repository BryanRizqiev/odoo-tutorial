from odoo import api, fields, models, exceptions
from odoo.tools.float_utils import float_compare, float_is_zero

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property model"
    _order = "id desc"

    name = fields.Char("Name", default="Unknown", required=True)
    description = fields.Text("Description", required=True)
    postcode = fields.Char("Postcode", required=True)
    date_availability = fields.Datetime("Available From", default=fields.Date.today(), readonly=True)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", required=True)
    bedrooms = fields.Integer("Bedrooms", required=True, default=2)
    living_area = fields.Integer("Living Area (sqm)", required=True)
    facades = fields.Integer("Facades", required=True)
    garage = fields.Boolean("Garage", required=True)
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")],
        help="Garden orientation"
    )
    active = fields.Boolean(required=True, default=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type", required=True)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    state = fields.Selection(
        string="Status",
        selection=[("new", "New"), ("offer_received", "Offer Received"), ("offer_accepted", "Offer Accepted"), ("canceled", "Canceled"), ("sold", "Sold")],
        default="new",
        readonly=True,
    )
    best_offer = fields.Float("Best Offer", compute="_compute_best_offer", store=True)
    salesman_id = fields.Many2one("res.users", string="Salesman", index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    offer_ids = fields.One2many(
        "estate.property.offer",
        "property_id",
        string="Offers",
    )
    total_area = fields.Integer("Total Area (sqm)", compute="_compute_total_area")

    _sql_constraints = [
        ('positive_expected_price', 'CHECK(expected_price > 0)', 'Expected price must be strictly positive.'),
        ('positive_selling_price', 'CHECK(selling_price > 0)', 'Selling price must be strictly positive.'),
        ("unique_name", "unique(name)", "The property name already created"),
    ]

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for property_record in self:
            property_record.total_area = property_record.living_area + property_record.garden_area

    @api.constrains("expected_price", "selling_price")
    def _check_selling_price(self):
        for property_record in self:
            if float_is_zero(property_record.expected_price, precision_digits=2):
                continue

            lower_limit = property_record.expected_price * 0.9
            if float_compare(property_record.selling_price, lower_limit, precision_digits=2) == -1:
                raise exceptions.ValidationError("Selling price cannot be lower than 90% of the expected price.")

    @api.onchange("garden")
    def _ochange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = False
            self.garden_orientation = False

    def button_cancel(self):
        for record in self:
            if record.state == "sold":
                raise exceptions.UserError("A sold property cannot be calceled.")
            record.write({"state": "canceled"})

    def button_sold(self):
        for record in self:
            if record.state == "canceled":
                raise exceptions.UserError("A canceled property cannot be sold.")
            if not record.buyer_id:
                raise exceptions.UserError("Buyer required.")
            record.write({"state": "sold"})

    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for property_record in self:
            try:
                property_record.best_offer = max(property_record.offer_ids.mapped("price"))
            except:
                property_record.best_offer = 0

    @api.constrains("best_offer")
    def _check_best_offer(self):
        for record in self:
            if record.best_offer < 0:
                raise exceptions.ValidationError("Best offer price must be positive.")
            
    @api.ondelete(at_uninstall=False)
    def _prevent_record_delted(self):
        for record in self:
          if record.state == "new" or record.state == "canceled":
            raise exceptions.UserError("Can't delete an record because is New or Canceled.")