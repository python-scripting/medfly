 <template>
 <!--header with button-->
 <vx-card>
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="left" vs-align="left" vs-lg="12" vs-sm="4" vs-xs="12" >
    <p>FIND PATIENT RECORDS</p>
  </vs-col>
    
  <vs-divider position="left">
    </vs-divider>
</vs-row> 
<!--eof-->
 <vs-table  v-model="selected" pagination max-items="5" search :data="patients">

    <template slot="thead">
      <vs-th sort-key="sno">S.No</vs-th>
      <vs-th sort-key="mf_id">Mf Id</vs-th>
      <vs-th sort-key="alt_id">Alt Id</vs-th>
      <vs-th sort-key="mobile">Mobile</vs-th>
      <vs-th sort-key="pt_name">Pat Name</vs-th>
      <vs-th sort-key="dor">Reg Date</vs-th>
      <vs-th sort-key="doc_name">Doc Name</vs-th>
      <vs-th sort-key="referrer">Referrer</vs-th>
      <vs-th sort-key="procedure">Procedure</vs-th>
      <vs-th sort-key="procedure">Visit</vs-th>
      <vs-th>Actions</vs-th>
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
         <vs-td>
         <select><option v-for="visit in visits" :value="visit">{{visit}}</option></select>
        </vs-td>
        <vs-td>
          <vs-row>
            <vs-button  type="filled" color="rgb(67,70,77)" size="small">select</vs-button>
          </vs-row>
        </vs-td>

      </vs-tr>
    </template>

  </vs-table>
 
</vx-card>
</template>

<script>
import axios from 'axios';
import patients from '@/views/ag-grid-table/patients.json'
export default {
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
      visits:['1','2','3'],
    }
  },
}
</script>



