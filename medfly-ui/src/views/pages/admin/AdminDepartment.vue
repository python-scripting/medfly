<template>
 <vx-card class="CustomHeight">
   <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> DEPARTMENT SECTION</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="6" vs-sm="4" vs-xs="12" >
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12">
    <vs-button @click="deptpopup=true" color="rgb(67,70,77)" type="filled">Add Department </vs-button>
  </vs-col>

   <vs-divider position="left"></vs-divider>
</vs-row> 
<!--eof-->

    <template>
      <div class="flex">
       
        <vs-popup classContent="popup-example" title="Add Department" :active.sync="deptpopup">
        <form>
           
          <div class="flex mb-4">
            <div class="w-1/4 h-12">Name</div>
            <div class="w-3/4 h-12"><vs-input class="w-full mb-3"/></div>
            <div class="w-1/4 h-12"></div>
          </div>

          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button color="rgb(67,70,77)" type="filled" id="button-with-loading" class="vs-con-loading__container mr-2" @click="saveloader">Save Department</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
           <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i> new deparment created.</p>

        </vs-popup>
      </div>
</template>
    <!-- Save & Reset Button -->
   <vs-table  pagination max-items="5" search :data="departments">

    <template slot="thead">
      <vs-th sort-key="id">S.NO</vs-th>
      <vs-th sort-key="Department_Name">DEPARTMENT NAME</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template  slot-scope="{data}">
      <vs-tr :key="column"  v-for="(row, column) in data" class="tr_line">

         <vs-td :data="data[column].id">
            {{  data[column].id }}
        </vs-td>
        
        <vs-td :data="data[column].Department_Name">
         <b>{{  data[column].Department_Name.toUpperCase() }}</b>
        </vs-td>

        <vs-td>
          <vs-row>
            <vs-button  type="filled" color="rgb(67,70,77)" class="mr-2" size="small" icon-pack="feather" icon="icon-edit-2"></vs-button>
            <vs-button  type="filled" color="rgb(255,20,99)" size="small" icon-pack="feather" icon="icon-x" @click=""></vs-button>
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

      'tableList': [
        'vs-th: Component',
        'vs-tr: Component',
        'vs-td: Component',
        'thread: Slot',
        'tbody: Slot',
        'header: Slot'
      ],
      departments:[],
      deptpopup: false,
    }
  },  
  
   methods:{
    // this method will save the new department
    saveloader(){
      axios.post().then(response=>{
   })
      this.$vs.loading({
        background: this.backgroundLoading,
        color: this.colorLoading,
        container: "#button-with-loading",
        scale: 0.45
      })
      setTimeout( ()=> {
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