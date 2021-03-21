<template>
 <div>
<vx-card>
  <vs-row>
   <vs-col vs-lg="10" vs-sm="12" vs-xs="12">
   	   
    <div class="bg-dark h-12">
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-lg="6" vs-sm="4" vs-xs="12">
   <template>
  <vs-button type="transparent" size="small"><feather-icon icon="TypeIcon"/></vs-button>
  <vs-button type="transparent"  size="small"><feather-icon icon="SquareIcon"/></vs-button>
 <vs-button type="transparent" size="small"><feather-icon icon="CircleIcon"/></vs-button>
  <vs-button type="transparent" size="small"><feather-icon icon="MousePointerIcon"/></vs-button>
  <vs-button type="transparent" size="small"><feather-icon icon="HexagonIcon"/></vs-button>
  
</template>
   
  </vs-col>
  <vs-col vs-type="flex" vs-lg="4" vs-sm="4" vs-xs="12">

  </vs-col>
  <vs-col vs-type="flex" vs-lg="2" vs-sm="4" vs-xs="12">
  <template>
    <vs-button type="transparent" size="small"><feather-icon icon="ImageIcon"/></vs-button>
    <vs-button type="transparent" size="small"><feather-icon icon="CalendarIcon"/></vs-button>
    <vs-button size="small" type="transparent" 
@click="active=!active, notExpand = true"><feather-icon icon="ClockIcon"/></vs-button>
  </template>
  </vs-col>
</vs-row>
</div>
<img src="https://wallpapermemory.com/uploads/592/purple-background-hd-2560x1440-405397.jpg" width="100%" height="500vh"/>
</vs-col>
	<vs-col vs-lg="2" vs-sm="12" vs-xs="12">
	 <div class="ml-1 con-tab-ejemplo">
	  
	   <vs-col vs-lg="12" vs-sm="12" vs-xs="12">
	    <vs-tabs alignment="fixed" class="bg-dark">
	      <vs-tab label="Images" color="warning">
	        <vs-row>
	    <VuePerfectScrollbar class="scroll-area" v-once :settings="settings" @ps-scroll-y="scrollHandle">
	      <vs-row>
	      <img class="mb-1 ml-1" src="https://thumbs.dreamstime.com/b/futuristic-glowing-low-polygonal-human-stomach-isolated-dark-blue-background-made-lines-dots-light-spots-gastroenterology-163778690.jpg" width="100%" height="180vh">
	      <img class="mb-1 ml-1" src="https://image.freepik.com/free-vector/futuristic-glowing-low-polygonal-helicobacter-pylori-bacteria-cells-isolated-dark-blue-background_67515-1017.jpg" width="100%" height="180vh">
	      <img class="mb-1 ml-1" src="https://thumbs.dreamstime.com/b/futuristic-glowing-low-polygonal-human-stomach-isolated-dark-blue-background-made-lines-dots-light-spots-gastroenterology-163778690.jpg" width="100%" height="180vh">
	      <img class="mb-1 ml-1" src="https://image.freepik.com/free-vector/futuristic-glowing-low-polygonal-helicobacter-pylori-bacteria-cells-isolated-dark-blue-background_67515-1017.jpg" width="100%" height="180vh">
	      <img class="mb-1 ml-1" src="https://thumbs.dreamstime.com/b/futuristic-glowing-low-polygonal-human-stomach-isolated-dark-blue-background-made-lines-dots-light-spots-gastroenterology-163778690.jpg" width="100%" height="180vh">
	      <img class="mb-1 ml-1" src="https://image.freepik.com/free-vector/futuristic-glowing-low-polygonal-helicobacter-pylori-bacteria-cells-isolated-dark-blue-background_67515-1017.jpg" width="100%" height="180vh">
	     </vs-row>
	     </VuePerfectScrollbar>
	      </vs-row>
	    </vs-tab>
	 
	  </vs-tabs>
	 </vs-col>
	</div>

      </vs-col>
</vs-col>
</vs-row>
</vx-card>
</div>
</template>
<script>
import VuePerfectScrollbar from 'vue-perfect-scrollbar'

export default {
  components: {
    VuePerfectScrollbar
  },
  data() {
    return {
    
    	settings: {maxScrollbarLength: 60},
      }
  },
   methods: {
    scrollHandle(evt) {
      console.log(evt)
    }
  }   
    }

</script>
<style lang="scss">
.scroll-area {
  position: relative;
  margin: auto;
  width: 100%;
  height: 74vh;
}
</style>

