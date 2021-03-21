
 <vx-card>
   <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> TEMPLATE SECTION</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="8" vs-sm="4" vs-xs="12" >
   
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
    <vs-button @click="Temppopup=true" color="rgb(67,70,77)" type="filled">Add Template </vs-button>  
  </vs-col>

   <vs-divider position="left"></vs-divider>
</vs-row> 
<!--eof-->
<!--popup for new paramater-->

    <template>
      <div class="flex">
       
        <vs-popup classContent="popup-example" title="Add Template" :active.sync="Temppopup">
        <form>
          <div class="flex mb-4">
            <div class="w-1/4 h-12">
              <span>Department</span>
            </div>
            <div class="w-3/4 h-12">
              <v-select placeholder="Select Department..." :options="departmentoptions" class="mr-1"></v-select> 
            </div>
            <div class="w-1/4 h-12">
             <vs-button  type="filled" color="rgb(101, 119, 134)" class="mr-2" size="small" icon-pack="feather" icon="icon-plus" @click="departmentcomponent.departmentpopup=true"></vs-button>
           </div>
          </div>
            <div class="flex mb-4">
            <div class="w-1/4 h-12">
              <span>Procedure</span>
            </div>
            <div class="w-3/4 h-12">
              <v-select placeholder="Select Procedure..." class="mr-1" :options="procedureoptions"></v-select>
            </div>
            <div class="w-1/4 h-12">
             <vs-button  type="filled" color="rgb(101, 119, 134)" class="mr-2" size="small" icon-pack="feather" icon="icon-plus" @click="add_parameter=true"></vs-button>
           </div>
          </div>
          <div class="flex mb-4">
            <div class="w-1/4 h-12">Name</div>
            <div class="w-3/4 h-12"><vs-input v-model="dname" class="w-full mb-3"/></div>
             <div class="w-1/4 h-12"></div>
          </div>

          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button color="rgb(67,70,77)" type="filled" id="button-with-loading" class="vs-con-loading__container mr-2" @click="saveloader">Save Template</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
           <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i>  new template created.</p>

        </vs-popup>
      </div>
</template>
    <!-- Save & Reset Button -->
   <vs-table  v-model="selected" pagination max-items="5" search :data="templates">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="dname">Department Name</vs-th>
      <vs-th sort-key="pname">Procedure Name </vs-th>
      <vs-th sort-key="tname">Template Name </vs-th>
      <vs-th sort-key="created_on">Created On</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="">
      <vs-tr   :key="indextr" v-for="(tr, indextr) in templates">

         <vs-td  >
            {{  tr.sno }}
        </vs-td>

        <vs-td >
         {{  tr.dname }}
        </vs-td>

        <vs-td  >
        {{  tr.pname }}
        </vs-td>

         <vs-td  >
        <b>{{  tr.tname }}</b>
        </vs-td>
        <vs-td  >
        {{  tr.created_on }}
        </vs-td>

        <vs-td>
          <vs-row>
             <vs-button  type="filled" color="rgb(101, 119, 134)" class="mr-2" size="small" icon-pack="feather" icon="icon-plus" @click="add_parameter=true"></vs-button>
            <vs-button  type="filled" color="rgb(82,121,152)" class="mr-2" size="small" icon-pack="feather" icon="icon-edit-2" @click="Temppopup=true"></vs-button>
            <vs-button  type="filled" color="rgb(255,20,99)" size="small" icon-pack="feather" icon="icon-x"></vs-button>
          </vs-row>
        </vs-td>

      </vs-tr>
    </template>

  </vs-table>
 
</vx-card>
</template>

<script>
import axios from 'axios';
//import procedures from '@/views/ag-grid-table/procedures.json'
import templates from '@/views/ag-grid-table/templates.json'
import departmentcomponent from './superadmin/SuperAdminDepartment.vue'

import vSelect from 'vue-select'
export default {
  components:{
    'v-select': vSelect,departmentcomponent
  },
  data() {
    return {
       // used for button status after update button is clicked
      backgroundLoading:'success',
      colorLoading:'#fff',
      selected: [],
      departmentoptions:[],

      'tableList': [
        'vs-th: Component',
        'vs-tr: Component',
        'vs-td: Component',
        'thread: Slot',
        'tbody: Slot',
        'header: Slot'
      ],
      templates,
      Temppopup: false,
      add_parameter:false,
      pname: '',
      colon:':',
     departmentpopup:false,
    }
  }
}
</script>

