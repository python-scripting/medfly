<template>
  <vs-card class="p4">
     <vs-col  vs-w="12"><ROptions></ROptions></vs-col>
    <vs-col  vs-w="12"><RHeader></RHeader></vs-col>
    <vs-col  vs-w="12"><RPatients></RPatients></vs-col>
    <vs-col  vs-w="10" class="bodyheight"><RBody></RBody></vs-col>
    <vs-col  vs-w="2" vs-align="start"><RImages></RImages></vs-col>
    <vs-col  vs-w="12" ><RSignature></RSignature></vs-col>
    <vs-col  vs-w="12"><RFooter></RFooter></vs-col>
  </vs-card>
</template>

<script>
import RHeader from '../Template/RHeader.vue';
import RImages from '../Template/RImages.vue';
import RBody from '../Template/RBody.vue';
import RSignature from '../Template/RSignature.vue';
import RFooter from '../Template/RFooter.vue';
import RPatients from '../Template/RPatients.vue';
import ROptions from '../Template/ROptions.vue';

export default {
  components:{
    'RHeader': RHeader,
    'RImages':RImages,
    'RBody':RBody,
    'RSignature':RSignature,
    'RFooter':RFooter,
    'RPatients':RPatients,
    'ROptions':ROptions,
  },
  data () {
    return {
  }
}
}
</script>
<style lang="scss">
.p4{
     height: 900px;
     width:100%;
    border:1px solid #000;
}
</style>
