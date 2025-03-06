import { Component, xml, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { Counter } from "./clicker";
import { Card } from "./card";

export class Root extends Component {
    static template = xml `
      <Card>
        <t t-set-slot="title">
          Counter App
        </t>
        <t t-set-slot="text">
          <Counter onIncrement.bind="increment"/>
          <Counter onIncrement.bind="increment"/>
          <div>
            <t t-esc="state.value"/>
          </div>
          </t>
      </Card>
    `;

    setup() {
      this.state = useState({ value: 0 });
    }

    increment() {
        this.state.value++;
    }

    static components = { Counter, Card };
}

registry.category("actions").add("awesome_clicker.clicker", Root);