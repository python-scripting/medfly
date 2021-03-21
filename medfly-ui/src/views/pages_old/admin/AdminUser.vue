<template>
 <vx-card class="CustomHeight">

   <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> USERS SECTION</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="8" vs-sm="4" vs-xs="12" >
   
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
     <vs-button @click="popupActive2=true" color="rgb(67,70,77)" type="filled">New User</vs-button>
  </vs-col>

   <vs-divider position="left"></vs-divider>
</vs-row> 
<!--eof-->

    <template>
      <div class="flex">
       
        <vs-popup classContent="popup-example" title="Add New User" :active.sync="popupActive2">
        <form>
          <div class="flex mb-4">
            <div class="w-1/4 h-12">
              <span>Role</span>
            </div>
            <div class="w-3/4 h-12">
              <v-select placeholder="Select Role..." :options="roleoptions"></v-select>
            </div>
          </div>

          <div class="flex mb-4">          
            <div class="w-1/4 h-12">Name</div>
            <div class="w-3/4 h-12"><vs-input class="w-full mb-3" v-model="value1"/></div>
          </div>
           <div class="flex mb-4">          
            <div class="w-1/4 h-12">Mobile</div>
            <div class="w-3/4 h-12"><vs-input class="w-full mb-3"/></div>
          </div>

          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button color="rgb(67,70,77)" type="filled" id="button-with-loading" class="vs-con-loading__container mr-2" @click="saveloader">Save User</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
            <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i>  new user created.</p>

        </vs-popup>
      </div>
</template>
    <!-- Save & Reset Button -->
   <vs-table v-model="selected" pagination max-items="5" search :data="users">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="dept_name">DEPARTMENT NAME</vs-th>
      <vs-th sort-key="user">USER</vs-th>
      <vs-th sort-key="mobile">MOBILE</vs-th>
      <vs-th sort-key="user_username">USERNAME</vs-th>
       <vs-th sort-key="user_pwd">PASSWORD</vs-th>
      <vs-th sort-key="created_on">CREATED_ON</vs-th>
      <vs-th sort-key="status">STATUS</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

        <vs-td :data="data[indextr].sno">
          {{ data[indextr].sno }}
        </vs-td>

        <vs-td :data="data[indextr].dept_name">
          {{ data[indextr].dept_name }}
        </vs-td>
         <vs-td :data="data[indextr].user">
          {{ data[indextr].user }}
        </vs-td>
        <vs-td :data="data[indextr].mobile">
          {{ data[indextr].mobile }}
        </vs-td>
        <vs-td :data="data[indextr].user_username">
          {{ data[indextr].user_username }}
        </vs-td>
        <vs-td :data="data[indextr].user_pwd">
          {{ data[indextr].user_pwd }}
        </vs-td>
        <vs-td :data="data[indextr].created_on">
          {{ data[indextr].created_on }}
        </vs-td>
        <vs-td :data="data[indextr].status">
          <vs-chip transparent  color="success">{{ data[indextr].status }}</vs-chip>
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

import vSelect from 'vue-select'
import roles from '@/views/ag-grid-table/data.json'
import users from '@/views/ag-grid-table/users.json'
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
      users,
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



<style lang="scss">
.tr_line{
    border-top:1px solid #f2f0f0;
  }
.CustomHeight{
      height: 530px;
      max-height: 700px;
  }
</style>