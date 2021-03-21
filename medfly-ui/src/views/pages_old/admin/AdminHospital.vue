<template>

 <vx-card class="CustomHeight">
  <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> HOSPITAL SECTION</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="8" vs-sm="4" vs-xs="12" >
    <!-- <vs-upload single-upload limit="1" automatic  action="https://jsonplaceholder.typicode.com/posts/" @on-success="SuccessUpload"></vs-upload> -->
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
   <vs-button @click="popupActive2=true" color="rgb(67,70,77)" type="filled">New Hospital</vs-button>
  </vs-col>
  <vs-divider position="left">
    </vs-divider>
</vs-row> 
<!--eof-->

<vs-table v-model="selected" pagination max-items="5" search :data="hospitalsList">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="Name">NAME</vs-th>
      <vs-th sort-key="Account_StartDate">CREATED ON</vs-th>
      <vs-th sort-key="admin_username">ADMIN USERNAME</vs-th>
      <vs-th sort-key="admin_pwd">ADMIN PWD</vs-th>
      <vs-th sort-key="acc_type">A/C TYPE</vs-th>
      <vs-th sort-key="acc_status">A/C STATUS</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr  :key="column"  v-for="(row, column) in data" class="tr_line">
        <vs-td :data="data[column].id">
           {{ data[column].id }}
        </vs-td>
 
        <vs-td :data="data[column].Name">
          {{ data[column].Name }}
        </vs-td>

        <vs-td :data="data[column].Account_StartDate">
           {{ data[column].Account_StartDate }}
        </vs-td>
        <vs-td :data="data[column].Owner_Username">
          {{ data[column].Owner_Username }}
        </vs-td>
       
        <vs-td :data="data[column].Owner_Password">
        {{ data[column].Owner_Password }}
        </vs-td>
        <vs-td :data="data[column].Account_Type">
           <vs-chip color="success" transparent><span class="text-xs font-semibold">
           {{ data[column].Account_Type }}  </span></vs-chip>
        </vs-td>

         <vs-td :data="data[column].Status">
          <vs-chip color="success" transparent><span class="text-xs font-semibold"> 
 {{ data[column].Status }} 
          </span></vs-chip>

        </vs-td>

        <vs-td>
          <vs-row>
           <vs-button  type="border" @click="popupActive2=true"  color="rgb(67,70,77)" class="mr-2" size="small" icon-pack="feather" icon="icon-edit-2"></vs-button>

            <vs-button type="border" @click="EditHospital(column.id)"  color="primary" class="mr-2" size="small" icon-pack="feather" icon="icon-settings"></vs-button>

            <vs-button  type="border" @click="popupActive5=true" color="rgb(30,144,255)" class="mr-2" size="small" icon-pack="feather" icon="icon-pocket"></vs-button>
            
            <vs-button  type="border" @click="popupActive9=true" color="rgb(128,0,128)" class="mr-2" size="small" icon-pack="feather" icon="icon-file-text"></vs-button>
            
            <vs-button  type="border" color="rgb(255,20,99)" size="small" icon-pack="feather" icon="icon-x"></vs-button>
          </vs-row>
        </vs-td>

      </vs-tr>
    </template>

  </vs-table>

  <vs-popup  classContent="popup-example" title="Payment History" :active.sync="popupActive9">
    <div class="flex">
       <div class="w-1/2"><vs-button @click="popupActive5=true" color="rgb(67,70,77)" type="filled">Make New Payment</vs-button></div>
       <div class="w-1/2"><STRONG>APOLLO HOSPITALS</STRONG></div>
    </div>
 <!-- Table for Payment History-->
 <vs-table v-model="selected" pagination max-items="5" search :data="payment_history">

    <template slot="thead">
      <vs-th sort-key="id">S.NO</vs-th>
      <vs-th sort-key="hosp_name">HOSP.NAME</vs-th>
      <vs-th sort-key="hosp_id">HOSP.ID</vs-th>
      <vs-th sort-key="billed_date">BILLED DATE</vs-th>
      <vs-th sort-key="invoice_no">INVOICE NO.</vs-th>
      <vs-th sort-key="paid_amount">PAID AMOUNT</vs-th>
      <vs-th sort-key="payment_mode">PAYMENT MODE</vs-th>
      <vs-th>ACTIONS</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr  :key="indextr" v-for="(tr, indextr) in data">

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
            <vs-button type="border" @click="popupActive10=true" color="rgb(67,70,77)" class="mr-2" size="small" icon-pack="feather" icon="icon-eye"></vs-button>
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
<vs-popup classContent="popup-example"  title="Add New Hospital" :active.sync="popupActive2">
        <form method="post">
          <div class="vx-row mb-4">
    <div class="vx-col sm:w-1/3 w-full">
      <span>Have Branchs ?</span>
    </div>
    <div class="vx-col sm:w-2/3 w-full">
      <vs-switch color="success" icon-pack="feather" v-model="hospital_branch_having">
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
              <v-select v-model="selected_branch"  placeholder="Select Branch..." :options="branchoptions"></v-select>
            </div>
          </div>
          <div class="vx-row mb-4">
    <div class="vx-col sm:w-1/3 w-full">
      <span>Hospital Name</span>
    </div>
    <div class="vx-col sm:w-2/3 w-full">
      <vs-input class="w-full"  icon-pack="feather" icon="icon-book" v-model="hospital_name" />
    </div>
  </div>
  <div class="vx-row mb-4">
    <div class="vx-col sm:w-1/3 w-full">
      <span>Email</span>
    </div>
    <div class="vx-col sm:w-2/3 w-full">
      <vs-input type="email" class="w-full" icon-pack="feather" icon="icon-mail" v-model="hospital_email" />
    </div>
  </div>
    <div class="vx-row mb-4">
      <div class="vx-col sm:w-1/3 w-full">
        <span>Mobile</span>
      </div>
         
      <div class="vx-col sm:w-1/3 w-full">
       <vs-input class="w-full" icon-pack="feather" v-model="hospital_mobile" icon="icon-smartphone"/>
      </div>
    </div>
    <div class="vx-row mb-4">
      <div class="vx-col sm:w-1/3 w-full">
          <span>LandLine</span>
        </div>
      <div class="vx-col sm:w-1/3 w-full">
        <vs-input class="w-full" icon-pack="feather" v-model="hospital_landline"  icon="icon-phone"/>
      </div>
     
    </div>

          <div class="row">
            <div class="flex">
              <div class="w-1/3">
              </div>
              <div class="w-1/3">
               <div class="w-full"><vs-button  color="rgb(67,70,77)" type="filled" id="button-with-loading" class="vs-con-loading__container mr-2" @click="saveloader">Save Hospital</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
         
        <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i> created new hospital.</p>
 </vs-popup>

      <!---EDIT HOSPITAL-modal for installation settings starts-->
<vs-popup classContent="popup-example" title="Installation Details" :active.sync="popupActive4">
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
           <datepicker  v-model="hospitalDoi_edit" :minimumView="'day'" :maximumView="'month'"></datepicker>
        </vx-input-group>
            </div>
            <div class="vx-col sm:w-1/2 w-full">
              <v-select v-model="selected_branch" placeholder="Select Branch..." :options="branchoptions"></v-select>
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
           <datepicker v-model="Installation_Date" :minimumView="'day'" :maximumView="'month'"></datepicker>
        </vx-input-group>
    </div>
    <div class="vx-col sm:w-1/2 w-full">
       <vx-input-group  prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
               <span class="text-dark"><small>Expires</small></span>
            </div>
          </template>
           <datepicker  v-model="Account_ExpiryDate"   :minimumView="'day'" :maximumView="'month'"></datepicker>
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
               <div class="w-full"><vs-button @click="edithospitalSave" color="rgb(67,70,77)" type="filled">Save Hospital</vs-button>
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
               <div class="w-full"><vs-button @click="popupActive6=true" color="rgb(67,70,77)" type="filled">Make Payment</vs-button>
                </div>
              </div>
              <div class="w-1/3">
              </div>
            </div>
          </div>
        </form>
          <vs-popup title="MedFly Alert" :active.sync="popupActive6">
           <i class="las la-check-circle la-lg text-success"></i> Payment received successfully.<vs-button @click="popupActive9=true" size="small" color="rgb(67,70,77)" type="filled"><i class="las la-hand-pointer la-lg text-white"></i>  Check Payment History</vs-button>
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
      selected_branch:[],
       branchoptions: ['Main','SubBranch'],
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
      hospitalsList:[],
      payment_history,
      value1: '',
      value2: '',
      /*******************/
      selectedHospitalId:0,
      hospital_name :"",
      hospital_email :"",
      hospital_branch_having :'', 
      hospital_branch_type:"",
      hospital_mobile:'',
      hospital_landline :"",
      /*******************/

      popupActive2: false,

      popupActive3: false,
      popupActive4: false,

      popupActive5: false,
      popupActive6: false,

      popupActive7: false,
      popupActive8: false,

      popupActive9: false,

      popupActive10: false,

      hospitalDemo_edit :"",
      hospitalDoi_edit :"",
      Installation_Date : '',
      Account_ExpiryDate:"",
      //hospitalbranch_edit :"",
     // hospitalStatus_edit :"",
      //hospitalQuotAmt_edit :"",
      //hospitalFinelAmt_edit :"",
      //hospitalDevices_edit :"",
     // hospitalFollowup_edit :"",
     // hospitalLeadby_edit :"",
      //hospitalRemarks_edit :"",

    }
  },
  created() {
     // axios requests
     this.LoadHospitals()
  },
   methods:{
    EditHospital(hospid){
      this.selectedHospitalId = hospid
      //alert(hospid)
      axios.get(`http://127.0.0.1:8081/hospital/`,{params: { hospid: hospid }}).then(response => {
            if( response.data[0].Account_Type == "Demo" ){
              this.radios2 = 'primary'
            }else{
              this.radios2 = 'Success'
            }
      //this.hospitalDemo_edit = response.data[0].Name
       
      this.hospitalDoi_edit     = response.data[0].Account_StartDate
      this.hospital_branch_type = response.data[0].Branch_Type
      this.selected_branch      = response.data[0].Branch_Type
      this.hospitalStatus_edit  = response.data[0].Account_StartDate
      this.Installation_Date    = response.data[0].Installation_Date
      this.Account_ExpiryDate   = response.data[0].Account_ExpiryDate

      this.hospitalQuotAmt_edit  = response.data[0].Quoted
      this.hospitalFinelAmt_edit = response.data[0].Finalised_Cost
      this.hospitalDevices_edit  = response.data[0].Total_Devices
      this.hospitalFollowup_edit = response.data[0].Contact_Person
      this.hospitalLeadby_edit   = response.data[0].Lead_by
      this.hospitalRemarks_edit  = response.data[0].Status
        //alert( response.data[0].Name)
      })
      this.popupActive4 = true;
    },

    edithospitalSave(){
       alert("selectedHospitalId")
    },
     //function to load hospital data
    LoadHospitals(){

         axios.get(`http://127.0.0.1:8081/hospital/`)
    .then(response => {
      for (var y in response.data) {
        //this.procedures.push(response.data[y].title)
            this.hospitalsList.push(response.data[y])
        }
      //this.posts = response.data
    })
    .catch(e => {
      alert(e)
      this.errors.push(e)
    })


    },
    SuccessUpload(){
      this.$vs.notify({color:'success',title:'MedFly Status',text:'uploaded logo, successfully'})
    },
    saveloader(){

         this.$vs.loading({
        background: this.backgroundLoading,
        color: this.colorLoading,
        container: "#button-with-loading",
        scale: 0.45
      })
      var currentDate = new Date();
      var formatted_date = new Date().toJSON().slice(0,10).replace(/-/g,'/');
     axios.post('http://127.0.0.1:8081/hospital/', {
        headers: {
        'Content-type': 'application/x-www-form-urlencoded',
      },
      
        "hospital_branch_having":this.hospital_branch_having,
        "hospital_branch_type": "Main",
        "Name": this.hospital_name,
        "Email": this.hospital_email,
        "Mobile": 7276816871,
        "Location": "",
        "Account_Type": "Demo",
        "Owner_Username": this.hospital_mobile,
        "Owner_Password": "MedFly_Name",
        "Account_StartDate": formatted_date,
        "Status": "Active"
     
  
   }).then(response  => {

            this.$vs.loading.close("#button-with-loading > .con-vs-loading")
   });
    
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
