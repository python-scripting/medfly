<template>

 <vx-card>
  <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> HOSPITAL SECTION</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="8" vs-sm="4" vs-xs="12" >
    <!-- <vs-upload single-upload limit="1" automatic  action="https://jsonplaceholder.typicode.com/posts/" @on-success="successUpload"></vs-upload> -->
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
   <vs-button @click="popupActive2=true" color="dark" type="filled">New Hospital</vs-button>
  </vs-col>
  <vs-divider position="left">
    </vs-divider>
</vs-row> 
<!--eof-->

<vs-table v-model="selected" pagination max-items="5" search :data="hospitals">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="name">NAME</vs-th>
      <vs-th sort-key="created_on">CREATED ON</vs-th>
      <vs-th sort-key="admin_username">ADMIN USERNAME</vs-th>
      <vs-th sort-key="admin_pwd">ADMIN PWD</vs-th>
      <vs-th sort-key="acc_type">A/C TYPE</vs-th>
      <vs-th sort-key="acc_status">A/C STATUS</vs-th>
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
        <vs-td :data="data[indextr].admin_username">
          {{ data[indextr].admin_username }}
        </vs-td>
       
        <vs-td :data="data[indextr].admin_pwd">
          {{ data[indextr].admin_pwd }}
        </vs-td>
        <vs-td :data="data[indextr].acc_type">
           <vs-chip color="success" transparent><span class="text-xs font-semibold">{{ data[indextr].acc_type }}</span></vs-chip>
        </vs-td>

         <vs-td :data="data[indextr].acc_status">
          <vs-chip color="success" transparent><span class="text-xs font-semibold">{{ data[indextr].acc_status }}</span></vs-chip>

        </vs-td>

        <vs-td>
          <vs-row>
            <vs-button type="border" @click="popupActive4=true" color="primary" class="mr-2" size="small" icon-pack="feather" icon="icon-settings"></vs-button>

            <vs-button  type="border" @click="popupActive5=true" color="rgb(30,144,255)" class="mr-2" size="small" icon-pack="feather" icon="icon-pocket"></vs-button>
            
            <vs-button  type="border" @click="popupActive9=true" color="rgb(128,0,128)" class="mr-2" size="small" icon-pack="feather" icon="icon-file-text"></vs-button>

            <vs-button  type="border" color="dark" class="mr-2" size="small" icon-pack="feather" icon="icon-edit-2"></vs-button>

            <vs-button  type="border" color="danger" size="small" icon-pack="feather" icon="icon-x"></vs-button>
          </vs-row>
        </vs-td>

      </vs-tr>
    </template>

  </vs-table>

  <vs-popup  classContent="popup-example" title="Payment History" :active.sync="popupActive9">
    <div class="flex">
       <div class="w-1/2"><vs-button @click="popupActive5=true" color="dark" type="filled">Make New Payment</vs-button></div>
       <div class="w-1/2"><STRONG>APOLLO HOSPITALS</STRONG></div>
    </div>
 <!-- Table for Payment History-->
 <vs-table v-model="selected" pagination max-items="5" search :data="payment_history">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="hosp_name">HOSP.NAME</vs-th>
      <vs-th sort-key="hosp_id">HOSP.ID</vs-th>
      <vs-th sort-key="billed_date">BILLED DATE</vs-th>
      <vs-th sort-key="invoice_no">INVOICE NO.</vs-th>
      <vs-th sort-key="paid_amount">PAID AMOUNT</vs-th>
      <vs-th sort-key="payment_mode">PAYMENT MODE</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

        <vs-td :data="data[indextr].sno">
          {{ data[indextr].sno }}
        </vs-td>

        <vs-td :data="data[indextr].hosp_name">
          {{ data[indextr].hosp_name }}
        </vs-td>

        <vs-td :data="data[indextr].hosp_id">
          {{ data[indextr].hosp_id }}
        </vs-td>
        <vs-td :data="data[indextr].billed_date">
          {{ data[indextr].billed_date }}
        </vs-td>
        <vs-td :data="data[indextr].invoice_no">
          {{ data[indextr].invoice_no }}
        </vs-td>
       
        <vs-td :data="data[indextr].paid_amount">
          {{ data[indextr].paid_amount }}
        </vs-td>

        <vs-td :data="data[indextr].payment_mode">
          {{ data[indextr].payment_mode }}
        </vs-td>

        <vs-td>
          <vs-row>
            <vs-button type="border" @click="popupActive10=true" color="dark" class="mr-2" size="small" icon-pack="feather" icon="icon-eye"></vs-button>
          </vs-row>
        </vs-td>
       

      </vs-tr>
    </template>
  </vs-table>
</vs-popup>
 <!-- end of Table for Payment History-->

<vs-popup fullscreen classContent="popup-example" title="Invoice Preview" :active.sync="popupActive10">
  <Invoice/>
</vs-popup>
 <!-- popup for hospital-->
<vs-popup classContent="popup-example" title="Add New Hospital" :active.sync="popupActive2">
        <form>
          <div class="vx-row mb-4">
    <div class="vx-col sm:w-1/3 w-full">
      <span>Have Branch ?</span>
    </div>
    <div class="vx-col sm:w-2/3 w-full">
      <vs-switch color="success" icon-pack="feather" v-model="switch5">
              <span slot="on">Yes</span>
              <span slot="off">No</span>
            </vs-switch>
    </div>
  </div>
          <div class="vx-row mb-4">
            <div class="vx-col sm:w-1/3 w-full">
              <span>Type of Branch</span>
            </div>
            <div class="vx-col sm:w-2/3 w-full">
              <v-select placeholder="Select Branch..." :options="branchoptions"></v-select>
            </div>
          </div>
          <div class="vx-row mb-4">
    <div class="vx-col sm:w-1/3 w-full">
      <span>Hospital Name</span>
    </div>
    <div class="vx-col sm:w-2/3 w-full">
      <vs-input class="w-full" icon-pack="feather" icon="icon-book" v-model="input5" />
    </div>
  </div>
  <div class="vx-row mb-4">
    <div class="vx-col sm:w-1/3 w-full">
      <span>Email</span>
    </div>
    <div class="vx-col sm:w-2/3 w-full">
      <vs-input type="email" class="w-full" icon-pack="feather" icon="icon-mail" v-model="input6" />
    </div>
  </div>
    <div class="vx-row mb-4">
      <div class="vx-col sm:w-1/3 w-full">
        <span>Mobile</span>
      </div>
         
      <div class="vx-col sm:w-1/3 w-full">
       <vs-input class="w-full" icon-pack="feather" icon="icon-smartphone"/>
      </div>
    </div>
    <div class="vx-row mb-4">
      <div class="vx-col sm:w-1/3 w-full">
          <span>LandLine</span>
        </div>
      <div class="vx-col sm:w-1/3 w-full">
        <vs-input class="w-full" icon-pack="feather" icon="icon-phone"/>
      </div>
     
    </div>

          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button  color="dark" type="filled" id="button-with-loading" class="vs-con-loading__container mr-2" @click="saveloader">Save Hospital</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
          
        <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i> created new hospital.</p>
 </vs-popup>


      <!--modal for installation settings starts-->
<vs-popup classContent="popup-example" title="Add New Hospital" :active.sync="popupActive4">
<form>
  <div class="vx-row mb-3">
    <div class="vx-col sm:w-1/3 w-full">
      <span>Account Type</span>
    </div>
    <div class="vx-col sm:w-2/3 w-full">
      <template>
        <ul class="vx-row">
          <li>
            <vs-radio v-model="radios2"  class="mr-4" vs-value="primary">Demo</vs-radio>
          </li>
          <li>
            <vs-radio color="success" v-model="radios2" vs-value="Success">Licensed</vs-radio>
          </li>
        </ul>
      </template>
    </div>
  </div>
          <div class="vx-row mb-3">
            <div class="vx-col sm:w-1/2 w-full">
              <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>DOI</small></span>
            </div>
          </template>
           <datepicker :minimumView="'day'" :maximumView="'month'"></datepicker>
        </vx-input-group>
            </div>
            <div class="vx-col sm:w-1/2 w-full">
              <v-select placeholder="Select Branch..." :options="branchoptions"></v-select>
            </div>
          </div>

  <div class="vx-row mb-3">
    <div class="vx-col sm:w-1/2 w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Starts</small></span>
            </div>
          </template>
           <datepicker :minimumView="'day'" :maximumView="'month'"></datepicker>
        </vx-input-group>
    </div>
    <div class="vx-col sm:w-1/2 w-full">
       <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Expires</small></span>
            </div>
          </template>
           <datepicker  :minimumView="'day'" :maximumView="'month'"></datepicker>
        </vx-input-group>
    </div>
  </div>

  <div class="vx-row mb-3">
    <div class="vx-col sm:w-1/2 w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Quote Amt</small></span>
            </div>
          </template>
            <vs-input type="number"/>
        </vx-input-group>
    </div>
    <div class="vx-col sm:w-1/2 w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Final Amt</small></span>
            </div>
          </template>
            <vs-input type="number"/>
        </vx-input-group>
    </div>
  </div>


  <div class="vx-row mb-3">
    <div class="vx-col sm:w-1/2 w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Pay.Type</small></span>
            </div>
          </template>
            <v-select placeholder="Select Payment Type..." :options="paytypeoptions"></v-select>
        </vx-input-group>
    </div>
    <div class="vx-col sm:w-1/2 w-full">
        <vx-input-group prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Tot.Devices</small></span>
            </div>
          </template>
            <v-select placeholder="Total Devices Issued..." :options="devicesoptions"></v-select>
        </vx-input-group>
    </div>
  </div>
   <div class="vx-row mb-3">
    <div class="vx-col sm:w-1/2 w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Followup</small></span>
            </div>
          </template>
            <vs-input />
        </vx-input-group>
    </div>
    <div class="vx-col sm:w-1/2 w-full">
        <vx-input-group prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>LeadBy</small></span>
            </div>
          </template>
          <vs-input />
        </vx-input-group>
    </div>
  </div>

   <div class="vx-row mb-3">
    <div class="vx-col w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Remarks</small></span>
            </div>
          </template>
            <vs-input class="w-full"/>
        </vx-input-group>
    </div>
  </div>
          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button @click="popupActive3=true" color="dark" type="filled">Save Hospital</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
 </form>
<vs-popup title="MedFly Alert" :active.sync="popupActive3">
 <i class="las la-check-circle la-lg text-success"></i> New hospital created.
</vs-popup>

        </vs-popup>
        <!--end of modal for installation settings-->

              <!--modal for make payment -->
   <vs-popup classContent="popup-example" title=" Make Payment " :active.sync="popupActive5">
<form>
     <div class="vx-row mb-3">
    <div class="vx-col w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Hospital Name</small></span>
            </div>
          </template>
            <vs-input class="w-full" disabled/>
        </vx-input-group>
    </div>
  </div>
          
  
  <div class="vx-row mb-3">
    <div class="vx-col sm:w-1/3 w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Total</small></span>
            </div>
          </template>
            <vs-input type="number" disabled/>
        </vx-input-group>
    </div>
    <div class="vx-col sm:w-1/3 w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Paid</small></span>
            </div>
          </template>
            <vs-input type="number" disabled/>
        </vx-input-group>
    </div>
    <div class="vx-col sm:w-1/3 w-full">
        <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Due</small></span>
            </div>
          </template>
            <vs-input type="number" disabled/>
        </vx-input-group>
    </div>
  </div>
          <div class="vx-row mb-3">
            <div class="vx-col sm:w-1/2 w-full">
               <span class="text-dark"><small>Payable Amount</small></span>
            </div>
            <div class="vx-col sm:w-1/2 w-full">
              <vs-input type="number"/>
            </div>
          </div>

          <div class="vx-row mb-3">
            <div class="vx-col sm:w-1/2 w-full">
               <span class="text-dark"><small>Mode of Payment</small></span>
            </div>
            <div class="vx-col sm:w-1/2 w-full">
              <v-select placeholder="Select mode of payment..." :options="paytypeoptions"></v-select>
            </div>
          </div>

          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button @click="popupActive6=true" color="dark" type="filled">Make Payment</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
          <vs-popup title="MedFly Alert" :active.sync="popupActive6">
           <i class="las la-check-circle la-lg text-success"></i> Payment received successfully. <vs-button @click="popupActive9=true" size="small" color="dark" type="filled"><i class="las la-hand-pointer la-lg text-white"></i>  Check Payment History</vs-button>
          </vs-popup>

        </vs-popup>
        <!--modal for make payment-->

</vx-card>


</template>
<script>
import axios from 'axios';
import vSelect from 'vue-select'
import hospitals from '@/views/ag-grid-table/hospital_data.json'
import payment_history from '@/views/ag-grid-table/payment_history.json'
import Datepicker from 'vuejs-datepicker';
import Invoice from './Invoice.vue'
export default {
  components:{
    'v-select': vSelect,Datepicker,Invoice,
  },
  data() {
    return {

      // used for button status after update button is clicked
      backgroundLoading:'success',
      colorLoading:'#fff',
      
      radios2:'primary',
      switch5:false,
       branchoptions: ['Main','Sub-Branch'],
       devicesoptions:[1,2,3,4,5,6,7,8],
       paytypeoptions:['Cheque','Cash','NEFT'],
      selected: [],
      'tableList': [
        'vs-th: Component',
        'vs-tr: Component',
        'vs-td: Component',
        'thread: Slot',
        'tbody: Slot',
        'header: Slot'
      ],
      hospitals,
      payment_history,
      value1: '',
      value2: '',

      popupActive2: false,

      popupActive3: false,
      popupActive4: false,

      popupActive5: false,
      popupActive6: false,

      popupActive7: false,
      popupActive8: false,

      popupActive9: false,

      popupActive10: false,
    }
  },
   methods:{
    successUpload(){
      this.$vs.notify({color:'success',title:'MedFly Status',text:'uploaded logo, successfully'})
    },
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


