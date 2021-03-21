<template>
<div>
    <div class="vx-row mb-1 w-full" :key="params" v-for="params in 15">
      <div class="vx-col sm:w-1/3">
        <span>Parameter 1</span>
      </div>
       <div class="vx-col sm:w-3/3">
        <span>:</span>
       </div>
      <div class="vx-col sm:w-1/2">
        <!-- <vs-input class="w-full" size="small" v-model="input1" /> -->
     <!--   <v-select  @click="simpleSuggestionMethod()" :options="ParameterValueList" v-model="SelectedParametervalue">
  </v-select> -->
        <input class="autowidth" type="text" v-model="name"/>
      </div>
</div>
    </div> 
</template>

<script>
// import VueSimpleSuggest from 'vue-simple-suggest'
// import 'vue-simple-suggest/dist/styles.css'
// import vselect from 'vue-select'
import VueInputAutowidth from 'vue-input-autowidth'

export default {
  components:{
    VueInputAutowidth,
  },
 data() {
      return {
       
      }
    },
  
}
</script>
<style>
.autowidth{
  width:630px;
}
</style>