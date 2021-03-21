<template>
 <vx-card class="CustomHeight">
   <!--header with button-->
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-justify="left" vs-align="left" vs-lg="12" vs-sm="12" vs-xs="12" >
    <p> ADMINISTRATOR PASSWORD SECTION</p>
  </vs-col>

   <vs-divider position="left"></vs-divider>
</vs-row> 
<!--eof-->

<form>
  <div class="flex mb-2">
      <div class="vx-col sm:w-1/4">User Name</div>
        <div class="vx-col sm:w-1/4">
         <vs-input  placeholder="Enter new username" v-model="value1"/>
      </div>
  </div>
  <div class="flex mb-4">
      <div class="vx-col sm:w-1/4">Password</div>
        <div class="vx-col sm:w-1/4">
         <vs-input  placeholder="Enter new password" v-model="value1"/>
      </div>
  </div>
  <div class="flex mb-4">
    
    <div class="vx-col">
       <vs-button type="filled" color="rgb(67,70,77)" icon-pack="feather" icon="icon-lock" id="button-with-loading" class="vs-con-loading__container mr-2" @click="saveloader">Update Password</vs-button>
    </div>
    <div class="vx-col">
      <vs-button type="flat" color="rgb(67,70,77)" class="mr-2" icon-pack="feather" icon="icon-refresh-cw">Reset</vs-button>
    </div>
  </div>
   
</form>
 <p class="mt-2"> <i class="las la-check-circle la-lg text-success"></i>  password updated successfully.</p>
</vx-card>
</template>

<script>
import axios from 'axios';
export default {

  data() {
    return {
      // used for button status after update button is clicked
      backgroundLoading:'success',
      colorLoading:'#fff',
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