<template>
 <vx-card>
  <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> REPORT PARAMETERS</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="7" vs-sm="4" vs-xs="12">
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12">
   <vs-button @click="add_parameter=true" color="rgb(67,70,77)" type="filled">Add Parameter</vs-button>
  </vs-col>
  <vs-divider position="left">
    </vs-divider>
</vs-row> 
<!--eof-->
      <!--popup for new paramater-->
    <template>
      <div class="flex">
       
        <vs-popup classContent="popup-example" title="Add New Parameter" :active.sync="add_parameter">
        <form>
          <div class="flex mb-4">
            <div class="w-1/4 h-12">Parameter Name</div>
            <div class="w-3/4 h-12">
              <vs-input class="w-full mb-3" v-model="pname"/>
            </div>
          </div>
           <div class="flex mb-4">
            <div class="w-1/4 h-12">Colon</div>
            <div class="w-3/4 h-12">
              <vs-input class="w-full mb-3" v-model="colon" />
            </div>
          </div>
           <div class="flex mb-4">
            <div class="w-1/4 h-12">Result</div>
            <div class="w-3/4 h-12">
            <vs-input class="w-full" v-model="result" />
            </div>
          </div>
               
                
          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button color="rgb(67,70,77)" type="filled" id="button-with-loading" class="vs-con-loading__container mt-2" @click="saveloader">Save Parameter</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
          <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i>  new parameter created.</p>

        </vs-popup>
      </div>
</template>
    <!-- Save & Reset Button -->
   <vs-table  v-model="selected" pagination max-items="5" search :data="parameters">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="name">Parameter Name</vs-th>
      <vs-th sort-key="created_on">Colon</vs-th>
      <vs-th sort-key="created_on">Result</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in parameters">

        <vs-td :data="data[indextr].sno">
          {{ data[indextr].sno }}
        </vs-td>

        <vs-td :data="data[indextr].pname">
          {{ data[indextr].pname }}
        </vs-td>
       <vs-td :data="data[indextr].colon">
          {{ data[indextr].colon }}
        </vs-td>
        <vs-td :data="data[indextr].result">
          {{ data[indextr].result }}
        </vs-td>

        <vs-td>
          <vs-row>
            <vs-button  type="filled" color="rgb(101, 119, 134)" class="mr-2" size="small" icon-pack="feather" icon="icon-edit-2"></vs-button>
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
import parameters from '@/views/ag-grid-table/parameters.json'
export default {
  data() {
    return {
      // used for button status after update button is clicked
      backgroundLoading:'success',
      colorLoading:'#fff',


      selected: [],
      'tableList': [
        'vs-th: Component',
        'vs-tr: Component',
        'vs-td: Component',
        'thread: Slot',
        'tbody: Slot',
        'header: Slot'
      ],
      parameters,
      pname: '',
      colon:':',
      add_parameter: false,
    }
  },
  methods:{
    saveloader(){
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


