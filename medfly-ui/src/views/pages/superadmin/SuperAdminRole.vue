<template>
 <vx-card class="CustomHeight">
   <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> ROLES SECTION</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="8" vs-sm="4" vs-xs="12" >
   
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
    <vs-button @click="popupActive2=true" color="rgb(67,70,77)" type="filled">New Role</vs-button>
  </vs-col>

   <vs-divider position="left"></vs-divider>
</vs-row> 
<!--eof-->

    <template>
      <div class="flex">
       
        <vs-popup classContent="popup-example" title="Add New Role" :active.sync="popupActive2">
        <form>
          <div class="flex mb-4">
            <div class="w-1/4 h-12">Name</div>
            <div class="w-3/4 h-12"><vs-input v-model="rolename" class="w-full mb-3" placeholder="Ex: Doctor, Nurse etc.."  /></div>
          </div>

          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button color="rgb(67,70,77)" type="filled" id="button-with-loading" class="vs-con-loading__container mr-2" @click="saveloader">Save Role</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
          <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i>  new role created.</p>

        </vs-popup>
      </div>
</template>
    <!-- Save & Reset Button -->
   <vs-table  pagination max-items="5" search :data="roles">

    <template>
     <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="name">NAME</vs-th>
     
      <vs-th>ACTIONS</vs-th>
    </template>

    <template>
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in roles">

        <vs-td :data="data[indextr].id">
          {{ data[indextr].id }}
        </vs-td>

        <vs-td :data="data[indextr].Role_Name">
          {{ data[indextr].Role_Name }}
        </vs-td>

        
        <vs-td>
          <vs-row>
            <vs-button  type="filled" color="rgb(101, 119, 134)" class="mr-2" size="small" icon-pack="feather" icon="icon-edit-2"></vs-button>
            <vs-button  type="filled" color="rgb(255,20,99)" @click="" size="small" icon-pack="feather" icon="icon-x"></vs-button>
          </vs-row>
        </vs-td>

      </vs-tr>
    </template>

  </vs-table>
 
</vx-card>
</template>

<script>
import axios from 'axios';
//import roles from '@/views/ag-grid-table/data.json'
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
      rolename:'',
      roles:[],
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
       axios.post().then(response => { 
    setTimeout(()=> {
      this.loadRoles()
      this.rolename =''
      this.popupActive2= false
        this.$vs.loading.close("#button-with-loading > .con-vs-loading")
      }, 100);
       })
     
      
    },

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