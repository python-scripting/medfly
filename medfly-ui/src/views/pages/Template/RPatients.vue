<template>
<div>
  <vs-row>
  <vs-col vs-w="6">
    <div class="vx-row mb-1" :key="params" v-for="params in 5">
      <div class="vx-col sm:w-1/3">
        <span class="font">Parameter 1</span>
      </div>
       <div class="vx-col sm:w-3/3">
        <span>:</span>
       </div>
      <div class="vx-col sm:w-1/3 w-full">
        <vs-label class="w-full" size="small" v-model="input1">Hello</vs-label>
      </div>
    </div>
  </vs-col>
   <vs-col  vs-w="6">
    <div class="vx-row mb-1" :key="params" v-for="params in 5">
      <div class="vx-col sm:w-1/3">
        <span>Parameter 2</span>
      </div>
       <div class="vx-col sm:w-3/3">
        <span>:</span>
       </div>
      <div class="vx-col sm:w-1/3 w-full">
        <vs-label class="w-full" size="small" v-model="input1">Patient Info</vs-label>
      </div>
    </div>
  </vs-col>
</vs-row>
    <vs-divider/> 
</div>
</template>
