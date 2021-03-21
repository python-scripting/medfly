<template>
 <div>
<vx-card>
  <vs-row>
   <vs-col vs-lg="10" vs-sm="12" vs-xs="12">
        <div class="bg-dark h-12">
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-lg="6" vs-sm="4" vs-xs="12">
   <template>
  <vs-button @click="activePrompt = true" type="transparent" size="small"><feather-icon icon="TypeIcon"/></vs-button>
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
    <vs-button @click="activePromptUpload = true" type="transparent" size="small"><feather-icon icon="ImageIcon"/></vs-button>
    <vs-button type="transparent" size="small"><feather-icon icon="CalendarIcon" @click="activePromptDate = true" /></vs-button>
    <vs-button size="small" type="transparent" 
@click="active=!active, notExpand = true"><feather-icon icon="ClockIcon"/></vs-button>
  </template>
  </vs-col>
</vs-row>
</div>
   	   <img src="https://wallpapermemory.com/uploads/592/purple-background-hd-2560x1440-405397.jpg" width="100%" height="455vh"/>
  <vs-slider step=10 v-model="value1"/>
    <div class="bg-dark h-12">
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-lg="6" vs-sm="4" vs-xs="12">
   <template>
  <vs-button type="transparent" size="small"><feather-icon icon="PlayIcon"/></vs-button>
 <!--  <vs-button type="transparent"  color="dark"><feather-icon icon="PauseIcon"/></vs-button>
  <vs-button type="transparent"  color="dark"><feather-icon icon="StopCircleIcon"/></vs-button> -->
  <vs-button type="transparent"  size="small"><feather-icon icon="CameraIcon"/></vs-button>
 <vs-button type="transparent" size="small" 
       ><feather-icon icon="DiscIcon"/></vs-button>
  <vx-input class="bg-dark text-white pt-3"> {{value1}} / 1:00:00</vx-input>
</template>
   
  </vs-col>
  <vs-col vs-type="flex"  vs-lg="4" vs-sm="4" vs-xs="12">

  </vs-col>
  <vs-col vs-type="flex"  vs-lg="2" vs-sm="4" vs-xs="12">
  <template>
    <vs-button size="small" type="transparent"><feather-icon icon="Volume2Icon"/></vs-button>
    <vs-button size="small" type="transparent" 
@click="active=!active, notExpand = true"><feather-icon icon="ToolIcon"/></vs-button>
  </template>
  </vs-col>
</vs-row>
</div>

      </vs-col>

      <vs-col vs-lg="2" vs-sm="12" vs-xs="12">
   <div class="ml-1 con-tab-ejemplo">
    
     <vs-col vs-lg="12" vs-sm="12" vs-xs="12">
      <vs-tabs alignment="fixed" class="bg-dark">
        <vs-tab label="Videos" colorx="warning">
          <vs-row>
      <VuePerfectScrollbar class="scroll-area" v-once :settings="settings" @ps-scroll-y="scrollHandle">
        <vs-row>
        <img class="mb-1 ml-1" src="https://64.media.tumblr.com/a0f08c2b5e77a99fa67fe8a8db9e9227/5e2823c5a4e19e61-df/s540x810/6d905df51a6cd28ae4a69651a1b0ac25262e23c6.gifv" width="220vh" height="180vh">
      <img class="mb-1 ml-1" src="https://i.pinimg.com/originals/d9/b9/b6/d9b9b6b9e3a1d6a39ffb74a1728ea5ae.gif" width="220vh" height="180vh">
      <img class="mb-1 ml-1" src="https://64.media.tumblr.com/a0f08c2b5e77a99fa67fe8a8db9e9227/5e2823c5a4e19e61-df/s540x810/6d905df51a6cd28ae4a69651a1b0ac25262e23c6.gifv" width="220vh" height="180vh">
      <img class="mb-1 ml-1" src="https://i.pinimg.com/originals/d9/b9/b6/d9b9b6b9e3a1d6a39ffb74a1728ea5ae.gif" width="220vh" height="180vh">
      <img class="mb-1 ml-1" src="https://64.media.tumblr.com/a0f08c2b5e77a99fa67fe8a8db9e9227/5e2823c5a4e19e61-df/s540x810/6d905df51a6cd28ae4a69651a1b0ac25262e23c6.gifv" width="220vh" height="180vh">
      <img class="mb-1 ml-1" src="https://i.pinimg.com/originals/d9/b9/b6/d9b9b6b9e3a1d6a39ffb74a1728ea5ae.gif" width="220vh" height="180vh">
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
<!-- tool window-->
<div id="parentx-static">
    
    <vs-sidebar position-right  :reduce="reduce" :reduce-not-hover-expand="notExpand" parent="body" default-index="1"  color="dark" class="sidebarx" spacer v-model="active">
      
      <vs-divider icon="minus" position="left"></vs-divider>
      
       <vs-sidebar-item :to="url" :index="sb.index" icon-pack="feather" v-for="sb in sidebarItems" :icon="sb.icon"></vs-sidebar-item>
       
      <div class="footer-sidebar" slot="footer">
        <vs-button icon="close" size="large" color="primary" type="filled"></vs-button>
      </div>
    </vs-sidebar>
  </div>

  <!--tool window code close-->
  <!--dialogue boxes for icons-->
   <vs-prompt title="Add Text"
      @cancel="val=''"
      @accept="acceptAlert"
      @close="close"
      :active.sync="activePrompt">
      <div class="con-exemple-prompt">
        <!-- <span>Add Text</span> -->
      <vs-input placeholder="enter text here" v-model="val" class="mt-3 w-full" />
      </div>
    </vs-prompt>

    <vs-prompt title="Upload Image"
      @cancel="val=''"
      @accept="acceptAlert"
      @close="close"
      :active.sync="activePromptUpload">
      <div class="con-exemple-prompt">
        <!-- <span>Add Text</span> -->
     
      <input type="file" class="form-control" id="customFile" />
      </div>
    </vs-prompt>

    <vs-prompt title="Date Picker" :active.sync="activePromptDate">
      <div class="centerx">
       <datepicker class="mydate" placeholder="Select Date" v-model="date"></datepicker>
      </div>
    </vs-prompt>
  <!--close dialogue boxes for icons-->
  </div>
</template>
<script>
import VuePerfectScrollbar from 'vue-perfect-scrollbar'
import Datepicker from 'vuejs-datepicker';
export default {
  components: {
    VuePerfectScrollbar,Datepicker
  },
  data() {
    return {
      date: null,
      activePrompt:false,
      activePromptUpload:false,
      activePromptDate:false,
      active:false,
      notExpand: false,
      reduce: true,
      sidebarItems: [
        {
        url: "/",
        index:1,
        name: "Dashboard",
        icon: "icon-square",
        i18n: "Dashboard",
        },
        {
        index:2,
        url: "/",
        name: "Colors",
        icon: "icon-circle",
        i18n: "Colors",
        },
        {
        index:3,
        url: "/",
        name: "Colors",
        icon: "icon-type",
        i18n: "Colors",
        },
        {
        index:4,
        url: "/",
        name: "Colors",
        icon: "icon-octagon",
        i18n: "Colors",
        },
        {
        index:5,
        url: "/",
        name: "Colors",
        icon: "icon-image",
        i18n: "Colors",
        }
      
    ],
    	value1:60,
    	settings: {maxScrollbarLength: 60},
      }
  },
   methods: {
    scrollHandle(evt) {
      console.log(evt)
    },
    successUpload(){
      this.$vs.notify({color:'success',title:'Upload Success',text:'Lorem ipsum dolor sit amet, consectetur'})
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
.header-sidebar {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 100%;
  }

  .mydate{
    width:200px !important;
    height:210px !important;
    max-height:240px !important;
  }

.footer-sidebar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  > button {
    border: 0px solid rgba(0, 0, 0, 0) !important;
    border-left: 1px solid rgba(0, 0, 0, 0.07) !important;
    border-radius: 0px !important;
  }
}
</style>

