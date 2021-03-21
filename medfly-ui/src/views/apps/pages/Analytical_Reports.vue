 <template>
  <!--header with button-->
 <vx-card>
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="left" vs-align="left" vs-lg="12" vs-sm="4" vs-xs="12" >
    <p> BUSINESS ANALYTICAL REPORTS</p>
  </vs-col>
    
  <vs-divider position="left">
    </vs-divider>
</vs-row> 
<!--eof-->
     

<form>
  <div class="flex mb-4">
  <div class="w-4/5">
      <vs-row vs-w="12">    
        <p class="mr-1">Records From</p>
        <datepicker :minimumView="'day'" :maximumView="'month'" class="mr-1"></datepicker>
        
        <datepicker :minimumView="'day'" :maximumView="'month'"></datepicker>      
      </vs-row>
  </div>
  
  <div class="w-1/5">
     <div class="row mb-4">
      <vs-button  color="primary" class="mr-2" size="small" type="gradient"><i class="las la-print la-2x"/></vs-button>
      <vs-button  color="primary" class="mr-2" size="small" type="gradient"><i class="las la-download la-2x"/></vs-button>
    </div>
   </div>
</div>
       
         <div class="vx-row mb-5">
        <div class="vx-col md:w-1/4 sm:w-1/2 w-full">
          <label class="text-sm opacity-75">Department</label>
          <v-select :options="departmentoptions" :clearable="false" class="mb-4 md:mb-0" />
        </div>
        <div class="vx-col md:w-1/4 sm:w-1/2 w-full">
          <label class="text-sm opacity-75">Procedure</label>
          <v-select :options="procedureoptions" :clearable="false" class="mb-4 md:mb-0" />
        </div>
        <div class="vx-col md:w-1/4 sm:w-1/2 w-full">
          <label class="text-sm opacity-75">Doctor</label>
          <v-select :options="doctoroptions" :clearable="false" class="mb-4 sm:mb-0" />
        </div>
        <div class="vx-col md:w-1/4 sm:w-1/2 w-full">
          <label class="text-sm opacity-75">Referrer</label>
          <v-select :options="referreroptions" :clearable="false"/>
        </div>

      </div>
       <!--  <div class="grid-demo__layout-container mb-3">
            <vs-row vs-w="12">
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
                   
                </vs-col>
                <vs-col vs-type="flex" vs-justify="left" vs-align="left" vs-lg="2" vs-sm="4" vs-xs="12">
                    Procedure
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12">
                   <v-select class="w-full" placeholder="Select Procedure..." :options="procedureoptions"></v-select>   
                </vs-col>
                 <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
                     
                </vs-col>
            </vs-row>
        </div>
        <div class="grid-demo__layout-container mb-3">
            <vs-row vs-w="12">
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
                   
                </vs-col>
                <vs-col vs-type="flex" vs-justify="left" vs-align="left" vs-lg="2" vs-sm="4" vs-xs="12">
                    Doctor
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12">
                   <v-select class="w-full" placeholder="Select Doctor..." :options="doctoroptions"></v-select>   
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
                     
                </vs-col>
                
            </vs-row>
        </div>
        <div class="grid-demo__layout-container mb-3">
            <vs-row vs-w="12">
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
                   
                </vs-col>
                <vs-col vs-type="flex" vs-justify="left" vs-align="left" vs-lg="2" vs-sm="4" vs-xs="12">
                    Referrer
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="4" vs-sm="4" vs-xs="12">
                   <v-select class="w-full" placeholder="Select Referrer..." :options="referreroptions"></v-select>   
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
                     
                </vs-col>
            </vs-row>
        </div>
         <div class="grid-demo__layout-container mb-3">
            <vs-row vs-w="12">
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
                   
                </vs-col>
                <vs-col vs-type="flex" vs-justify="left" vs-align="left" vs-lg="2" vs-sm="4" vs-xs="12">
                 
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
                    <vs-button type="filled" color="dark">View Reports</vs-button>
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
                     
                </vs-col>
            </vs-row>
        </div> -->
</form>



 <vs-table  v-model="selected" pagination max-items="5" :data="patients">

    <template slot="thead">
      <vs-th sort-key="sno">S.NO</vs-th>
      <vs-th sort-key="mf_id">MF ID</vs-th>
      <vs-th sort-key="alt_id">ALT ID</vs-th>
      <vs-th sort-key="mobile">MOBILE</vs-th>
      <vs-th sort-key="pt_name">PAT NAME</vs-th>
      <vs-th sort-key="dor">REG DATE</vs-th>
      <vs-th sort-key="doc_name">DOC NAME</vs-th>
      <vs-th sort-key="referrer">REFERRER</vs-th>
      <vs-th sort-key="procedure">PROCEDURE</vs-th>

    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

        <vs-td :data="data[indextr].sno">
          {{ data[indextr].sno }}
        </vs-td>

        <vs-td :data="data[indextr].mf_id">
          {{ data[indextr].mf_id }}
        </vs-td>

        <vs-td :data="data[indextr].alt_id">
          {{ data[indextr].alt_id }}
        </vs-td>
        <vs-td :data="data[indextr].mobile">
          {{ data[indextr].mobile }}
        </vs-td>
        <vs-td :data="data[indextr].pt_name">
          {{ data[indextr].pt_name }}
        </vs-td>
		<vs-td :data="data[indextr].dor">
          {{ data[indextr].dor }}
        </vs-td>
        <vs-td :data="data[indextr].doc_name">
          {{ data[indextr].doc_name }}
        </vs-td>
        <vs-td :data="data[indextr].referrer">
          {{ data[indextr].referrer }}
        </vs-td>
        <vs-td :data="data[indextr].procedure">
          {{ data[indextr].procedure }}
        </vs-td>
        

      </vs-tr>
    </template>

  </vs-table>
 
</vx-card>
</template>

<script>
import axios from 'axios';
import vSelect from 'vue-select'
import patients from '@/views/ag-grid-table/patients.json'
import Datepicker from 'vuejs-datepicker';
export default {
  components:{
    'v-select': vSelect,Datepicker
  },
  data() {
    return {
      selected: [],
      'tableList': [
        'vs-th: Component',
        'vs-tr: Component',
        'vs-td: Component',
        'thread: Slot',
        'tbody: Slot',
        'header: Slot'
      ],
      patients,
      departmentoptions: ['Endoscopy','Laparoscopy','ENT'],
      doctoroptions: ['Dr.Raj','Sub-Dr.manu'],
      referreroptions: ['Dr.Abc','Dr.Xyz'],
      procedureoptions: ['UpperGIEndoscopy','Laparoscopy'],
    }
  },
}
</script>


