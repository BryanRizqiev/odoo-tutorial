import { ListController } from '@web/views/list/list_controller';
import { useService } from "@web/core/utils/hooks";


export class DistrictListController extends ListController {
  setup() {
    super.setup();
    this.orm = useService("orm");
    this.uiService = useService("ui");
  }

  importButton() {
    // this.actionService.doActionButton({
    //   resModel: 'wilayah.subdistrict',
    //   name: 'import_data_subdistrict',
    //   context: this.context,
    //   type: 'object'
    // });

    this.uiService.block();
    this.orm.call("wilayah.subdistrict", "import_data_subdistrict", [])
    .then((val) => {
      console.log(val);
      this.uiService.unblock();
      setTimeout(() => {
        location.reload(); 
      }, 2000);
    }).catch((err) => {
      console.log(err);
      this.uiService.unblock();  
    });  
    
  }
}