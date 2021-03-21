<template>
 <!--header with button-->
 <vx-card>
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12" >
    <p> DIGITAL SIGNATURE</p>
  </vs-col>
    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="8" vs-sm="4" vs-xs="12">
  </vs-col>
  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-lg="2" vs-sm="4" vs-xs="12">
  
  </vs-col>
  <vs-divider position="left">
    </vs-divider>
    <vs-upload single-upload limit="1" automatic  action="https://jsonplaceholder.typicode.com/posts/" @on-success="successUpload"></vs-upload>
</vs-row> 
<!--eof-->

 
</vx-card>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      methods:{
    successUpload(){
      this.$vs.notify({color:'success',title:'MedFly Status',text:'uploaded digital signature, successfully'})
    }
  }
 
    }
  },
}
</script>


