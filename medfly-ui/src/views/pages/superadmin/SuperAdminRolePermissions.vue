<template>
  <vx-card class="CustomHeight">
   <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="left" vs-align="left" vs-lg="12" vs-sm="12" vs-xs="12" >
    <p> ROLE PERMISSIONS SECTION</p>
  </vs-col>

   <vs-divider position="left"></vs-divider>
</vs-row> 
<!--eof-->

<div class="vx-row">
    <div class="vx-col sm:w-1/2 w-full">

   
   <vs-table v-model="selected" pagination max-items="5" :data="roles">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="role_name">ROLE NAME</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

        <vs-td :data="data[indextr].sno">
          {{ data[indextr].sno }}
        </vs-td>

        <vs-td :data="data[indextr].role_name">
          {{ data[indextr].role_name }}
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
       
    </div>

    <div class="vx-col sm:w-1/2 w-full">
         <vs-table  v-model="selected" pagination max-items="5" :data="description">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="description">DESCRIPTION</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

        <vs-td :data="data[indextr].sno">
          {{ data[indextr].sno }}
        </vs-td>

        <vs-td :data="data[indextr].function_description">
          {{ data[indextr].function_description }}
        </vs-td>

        <vs-td :data="data[indextr].switch5">
         <vs-switch color="success" icon-pack="feather" v-model="data[indextr].switch5">
              <span slot="on">Yes</span>  
              <span slot="off">No</span>
            </vs-switch>
        </vs-td>

      </vs-tr>
    </template>

  </vs-table>
    </div>
  </div>
</vx-card>
</template>

<script>
import axios from 'axios';

import vSelect from 'vue-select'
import roles from '@/views/ag-grid-table/roles.json'
import description from '@/views/ag-grid-table/access_description.json'
export default {
  components:{
    'v-select': vSelect,
  },
  data() {
    return {
      selected: [],
      switch5:[],
      roleoptions:['Doctor','Nurse','Admin','Assistant'],
      'tableList': [
        'vs-th: Component',
        'vs-tr: Component',
        'vs-td: Component',
        'thread: Slot',
        'tbody: Slot',
        'header: Slot'
      ],
      roles,
      description,
      popupActive2: false,
      popupActive3: false,
    }
  },
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
