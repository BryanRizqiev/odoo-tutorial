/** @odoo-module **/

import { Component, xml } from "@odoo/owl";

export class Card extends Component {
    static template = xml `
      <div class="card d-inline-block m-2" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title"><t t-slot="title"/></h5>
            <p class="card-text">
              <t t-slot="text"/>
            </p>
        </div>
      </div>
  `;
}
