<template>
 <vx-card class="CustomHeight">
   <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> PROCEDURE SECTION</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="8" vs-sm="4" vs-xs="12" >
   
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
    <vs-button @click="popupActive2=true" color="rgb(67,70,77)" type="filled">Add Procedure </vs-button>
  </vs-col>

   <vs-divider position="left"></vs-divider>
</vs-row> 
<!--eof-->

    <template>
      <div class="flex">
       
        <vs-popup classContent="popup-example" title="Add Procedure" :active.sync="popupActive2">
        <form>
           <div class="flex mb-4">
            <div class="w-1/4 h-12">
              <span>Department</span>
            </div>
            <div class="w-3/4 h-12">
              <v-select placeholder="Select Department..." :options="departmentoptions" class="mr-1"></v-select> 
            </div>
            <div class="w-1/4 h-12">
             <vs-button  type="filled" color="rgb(101, 119, 134)" class="mr-2" size="small" icon-pack="feather" icon="icon-plus" @click="add_parameter=true"></vs-button>
           </div>
          </div>
          <div class="flex mb-4">
            <div class="w-1/4 h-12">Name</div>
            <div class="w-3/4 h-12"><vs-input  class="w-full mb-3"/></div>
            <div class="w-1/4 h-12"></div>
          </div>

          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button color="rgb(67,70,77)" type="filled" id="button-with-loading" class="vs-con-loading__container mr-2" @click="saveloader">Save Procedure</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
           <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i>  new procedure created.</p>

        </vs-popup>
      </div>
</template>
    <!-- Save & Reset Button -->
   <vs-table  v-model="selected" pagination max-items="5" search :data="procedures">

    <template slot="thead">
      <vs-th sort-key="Hosp_ID">S.NO</vs-th>
      <vs-th sort-key="Department_Name">DEPARTMENT NAME</vs-th>
      <vs-th sort-key="Procedure_Name">PROCEDURE NAME</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr   :key="indextr" v-for="(tr, indextr) in procedures" class="tr_line">

         <vs-td>
            {{  tr.Hosp_ID }}
        </vs-td>

        <vs-td>
         {{  tr.Department_Name }}
        </vs-td>

        <vs-td>
        {{  tr.Procedure_Name.toUpperCase() }}
        </vs-td>

        <vs-td>
          <vs-row>
            <vs-button  type="filled" color="rgb(67,70,77)" class="mr-2" size="small" icon-pack="feather" icon="icon-edit-2"></vs-button>
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

import vSelect from 'vue-select'
export default {
  components:{
    'v-select': vSelect,
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
      procedures:[],
      
      popupActive2: false,
    }
  },  
   methods:{
    saveloader(){
      axios.post().then(response=>{

   })
      this.$vs.loading({
        background: this.backgroundLoading,
        color: this.colorLoading,
        container: "#button-with-loading",
        scale: 0.45
      })
      setTimeout(()=> {
        this.$vs.loading.close("#button-with-loading > .con-vs-loading")
      }, 3000);

    }
  }

}
</script>

<style lang="scss">
.tr_line{
    border-top:1px solid #f2f0f0;
  }
.CustomHeight{
      height: 530px;
      max-height: 700px;
  }
</style>