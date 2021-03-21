<template>
  <vx-card>
  <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> REFFERERS SECTION</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="7" vs-sm="4" vs-xs="12">
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="3" vs-sm="4" vs-xs="12">
    <vs-button @click="popupActive2=true" color="dark" type="filled">New Referrer</vs-button>
  </vs-col>
  <vs-divider position="left">
    </vs-divider>
</vs-row> 
<!--eof-->
    <template>
      <div class="flex">
       
        <vs-popup classContent="popup-example" title="Add New Referrer" :active.sync="popupActive2">
        <form>
          <div class="flex mb-4">
            <div class="w-1/4 h-12">Name</div>
            <div class="w-3/4 h-12"><vs-input class="w-full mb-3"  v-model="value1"/></div>
          </div>

          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button color="dark" type="filled" id="button-with-loading" class="vs-con-loading__container mr-2" @click="saveloader">Save Referrer</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
        
 <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i>  new referred created.</p>
        </vs-popup>
      </div>
</template>
    <!-- Save & Reset Button -->
   <vs-table  v-model="selected" pagination max-items="5" search :data="referrers">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="name">NAME</vs-th>
      <vs-th sort-key="created_on">CREATED ON</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

        <vs-td :data="data[indextr].sno">
          {{ data[indextr].sno }}
        </vs-td>

        <vs-td :data="data[indextr].name">
          {{ data[indextr].name }}
        </vs-td>

        <vs-td :data="data[indextr].created_on">
          {{ data[indextr].created_on }}
        </vs-td>

        <vs-td>
          <vs-row>
            <vs-button radius type="filled" color="dark" class="mr-2" size="small" icon-pack="feather" icon="icon-edit-2"></vs-button>
            <vs-button radius type="filled" color="danger" size="small" icon-pack="feather" icon="icon-x"></vs-button>
          </vs-row>
        </vs-td>

      </vs-tr>
    </template>

  </vs-table>
 
</vx-card>
</template>

<script>
import axios from 'axios';
import referrers from '@/views/ag-grid-table/referrer.json'
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
      referrers,
      value1: '',
      value2: '',
      popupActive2: false,
      popupActive3: false,
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


