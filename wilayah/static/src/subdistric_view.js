/** @odoo-module */

import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { DistrictListController } from './subdistrict_controller';

export const districtListView = {
  ...listView,
  Controller: DistrictListController,
  buttonTemplate: 'wilayah.ImportButton',
};

registry.category('views').add('subdistrict_list_button', districtListView);