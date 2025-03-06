/** @odoo-module **/

import { Component  } from "@odoo/owl";

export class Counter extends Component {
    static template = "awesome_clicker.AwesomeClicker";

    static props = ["increment"];
}
