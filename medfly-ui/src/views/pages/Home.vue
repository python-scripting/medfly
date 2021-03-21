<template>
  <div>
<vx-card>
  <div class="flex">
  <div class="w-5/6">Patient Information</div>
  <div class="w-1/6">
    
    <p><i class="las la-video text-danger"></i> status will display here</p>
  </div>
   
</div>
 <vs-divider position="left">
</vs-divider>
      <div class="tabs-container px-1">
     

        <div class="con-tab-ejemplo">
        	<vs-row>
		        <vs-col vs-w="5" vs-xs="12">
               <form>
          <vs-row>
	<div>
    <div class="flex -mx-1">
      <div class="w-1/3 mr-1">
    
        <!-- <vs-input size="small" class="w-full mb-3" icon-pack="line-awesome" icon="icon-la-battery-three-quarters"/> -->
        <vx-input-group id="mf_id" prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
              <small class="text-dark">MFID</small>
            </div>
          </template>
      <vs-input/>
    </vx-input-group>
      </div>
      <div class="w-1/3 mr-1">
        <vx-input-group prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
              <small class="text-dark">ALT</small>
            </div>
          </template>
      <vs-input/>
    </vx-input-group>
      </div>
      <div class="w-1/3 mr-1">
        <vs-input size="small" class="w-full mb-3" icon-pack="feather" icon="icon-calendar" />
      </div>
    </div>

	  <div class="flex -mx-1">
		<div class="w-1/3 mr-1">
	    	<vx-input-group prependClasses="border border-solid border-grey border-r-0">
          <template slot="prepend">
            <div class="prepend-text">
              <small class="text-dark">Age</small>
            </div>
          </template>
      <vs-input/>
    </vx-input-group>
      
		</div>
		<div class="w-1/3 mr-1">
		        <v-select v-model="selected_gender" placeholder="Select Gender" :options="genders" class="w-full"></v-select>
		</div>
		<div class="w-1/3 mr-1">
		        <vs-input size="small" type="email" class="w-full mb-3" icon-pack="feather" icon="icon-smartphone" />
		</div>
	   </div>
    </div>
    <div>
	</div>

<vs-row vs-w="12" vs-xs="12">
  <vs-col vs-lg="2" vs-sm="6" vs-xs="12">
  <span>Name</span>
  </vs-col>
  <vs-col vs-lg="10" vs-sm="6" vs-xs="12">
    <vs-input class="w-full mb-3"/>
  </vs-col>
  
</vs-row>

<vs-row vs-w="12" vs-xs="12">
  <vs-col  vs-lg="2" vs-sm="6" vs-xs="12">
  <span>Procedure</span>
  </vs-col>
  <vs-col vs-lg="10" vs-sm="6" vs-xs="12">
    <v-select :options="procedures" class="w-full mb-3"></v-select>
  </vs-col>
</vs-row>

<vs-row vs-w="12" vs-xs="12">
  <vs-col  vs-lg="2" vs-sm="6" vs-xs="12" >
  <span>Doctor</span>
  </vs-col>
  <vs-col  vs-lg="10" vs-sm="6" vs-xs="12">
     <v-select :options="doctors" class="w-full mb-3"></v-select>
  </vs-col>
</vs-row>

<vs-row vs-w="12" vs-xs="12">
  <vs-col  vs-lg="2" vs-sm="6" vs-xs="12" >
  <span>Referrer</span>
  </vs-col>
  <vs-col vs-lg="10" vs-sm="6" vs-xs="12">
    <v-select :options="referrers" class="w-full mb-3"></v-select>
  </vs-col>
</vs-row>

<vs-row vs-w="12" vs-xs="12">
  <vs-col vs-lg="2" vs-sm="6" vs-xs="12" >
  <span>Anaesthesist</span>
  </vs-col>
  <vs-col vs-lg="10" vs-sm="6" vs-xs="12">
     <v-select :options="anesthesists" class="w-full mb-3"></v-select>
  </vs-col>
</vs-row>

<vs-row vs-w="12" vs-xs="12">
  <vs-col  vs-lg="2" vs-sm="6" vs-xs="12" >
  <span>Nurse</span>
  </vs-col>
  <vs-col vs-lg="10" vs-sm="6" vs-xs="12">
     <v-select :options="nurses" class="w-full mb-3"></v-select>
  </vs-col>
</vs-row>

<vs-row vs-w="12" vs-xs="12">
  <vs-col vs-lg="2" vs-sm="6" vs-xs="12" >
  <span>Status</span>
  </vs-col>
  <vs-col  vs-lg="10" vs-sm="6" vs-xs="12">
   <v-select size="small" :options="rstatus" v-model="selected_value" class="w-full mb-3"></v-select>
  </vs-col>
</vs-row>
 
<vs-row vs-w="12" class="mt-2" vs-xs="12">	  
	<vs-button color="rgb(67,70,77)" id="button-with-loading" class="vs-con-loading__container mr-1" @click="saveloader">Save</vs-button>
	<vs-button color="rgb(67,70,77)"  class="mr-1">Report</vs-button>
	<vs-button color="rgb(67,70,77)"  class="mr-1">Preview</vs-button>
	<vs-button color="rgb(67,70,77)"  class="mr-1">Print</vs-button>
	<vs-button color="rgb(67,70,77)">New</vs-button>
</vs-row>

  	</vs-row>
    </form>
  </vs-col>


  <vs-col vs-w="7" vs-xs="12" class="px-2">
 
    <!-- <img src="https://wallpapermemory.com/uploads/592/purple-background-hd-2560x1440-405397.jpg" width="100%" height="89%"> -->

     <video   ref="videosrc" width="100%" autoplay="true" height="89%"> </video>
 
  <vs-slider step=10 v-model="value1"/>
	<div class="bg-dark h-12">
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-lg="7" vs-sm="4" vs-xs="12">
   <template>
  <vs-button type="transparent" size="small"><feather-icon icon="PlayIcon"/></vs-button>
 <!--  <vs-button type="transparent"  color="rgb(67,70,77)"><feather-icon icon="PauseIcon"/></vs-button>
  <vs-button type="transparent"  color="rgb(67,70,77)"><feather-icon icon="StopCircleIcon"/></vs-button> -->
  <vs-button type="transparent"  size="small"><feather-icon icon="CameraIcon"/></vs-button>
 <vs-button type="transparent" size="small"><feather-icon icon="DiscIcon"/></vs-button>
  <p class="bg-dark text-white pt-3">00: {{value1}} :00/ 1:00:00</p>
</template>
  </vs-col>
  <vs-col vs-type="flex"  vs-lg="2" vs-sm="4" vs-xs="12">
  </vs-col>
  <vs-col vs-type="flex"  vs-lg="3" vs-sm="4" vs-xs="12">
  <template>
    <vs-button size="small" type="transparent" @click="ClipboardActive=true"><feather-icon icon="Share2Icon"/></vs-button>
    <vs-button size="small" type="transparent"><feather-icon icon="Volume2Icon"/></vs-button>
    <vs-button size="small" type="transparent"
@click="popupActive=true"><feather-icon icon="Maximize2Icon"/></vs-button>
  </template>
  </vs-col>
</vs-row> 
</div>
  
  </vs-col>
<vs-divider></vs-divider>
<div class="con-tab-ejemplo">
 
   <vs-col vs-lg="12" vs-sm="12" vs-xs="12">
    <vs-tabs>

      <vs-tab label="Snaps">
        <vs-row>
          <VuePerfectScrollbar class="scroll-area" v-once :settings="settings" @ps-scroll-y="scrollHandle">
          <vs-row>
            <div v-for="image in images">
              <div class="container mb-2">
                <img :src="image" alt="image" class="image w-full">
                <div class="overlay">
                  <div class="flex flex-col justify-between">
                    <div class="flex">
                          <vs-button color="success"  type="border" size="small" class="icon" icon-pack="feather" icon="icon-zoom-in"></vs-button>
                   
                     <div class="w-1/2 mt-1 ml-1">
                      
                       <vs-button size="small"  type="border" color="warning" class="mb-2" icon-pack="feather" icon="icon-edit-2"></vs-button>
                       <vs-button size="small" color="rgb(255,20,99)"  type="border" icon-pack="feather" icon="icon-trash"></vs-button>
                         </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
        </vs-row>
           </VuePerfectScrollbar>
       </vs-row>
  
      </vs-tab>

      <vs-tab label="Videos">
        <vs-row>
    <VuePerfectScrollbar class="scroll-area" v-once :settings="settings" @ps-scroll-y="scrollHandle">
      <vs-row>
      <div v-for="video in videos">
            <div class="container mb-2">
              <img :src="video" alt="video_file" class="image">
              <div class="overlay">
                <div class="flex flex-col justify-between">
                   <div class="flex">
                      <vs-button color="success"  type="border" size="small" class="icon" icon-pack="feather" icon="icon-play"></vs-button>
                   
                     <div class="w-1/2 mt-1 ml-1">
                      <vs-button size="small"  type="border" color="warning" class="mb-2" icon-pack="feather" icon="icon-edit-2"></vs-button>
                      <vs-button size="small" color="rgb(255,20,99)"  type="border" icon-pack="feather" icon="icon-trash"></vs-button>
                   </div>
              </div>
            </div>
          </div>
        </div>
    </div>
     </vs-row>
     </VuePerfectScrollbar>
      </vs-row>
    </vs-tab>

  <vs-tab label="Import">
    <vs-row>
      <VuePerfectScrollbar class="scroll-area" v-once :settings="settings" @ps-scroll-y="scrollHandle">
          <!-- <vs-upload multiple automatic action="https://jsonplaceholder.typicode.com/posts/" @on-success="successUpload"></vs-upload> -->
        
       </VuePerfectScrollbar>
    </vs-row>
  </vs-tab>

  </vs-tabs>

 </vs-col>
        </div>
</vs-row> <!--final close-->


 </div>

   </div>
</vx-card>
<template>
<div class="demo-alignment">
  <vs-popup  background-color="rgb(0,0,0,0.9)" fullscreen title="Video Fullscreen [click 'minimize icon' to exit fullscreen]" :active.sync="popupActive">
<vs-col vs-w="12" vs-xs="12" class="px-2">
<img src="https://wallpapermemory.com/uploads/592/purple-background-hd-2560x1440-405397.jpg" width="100%" height="475vh" min-height="50%">
<vs-slider step=10 v-model="value1"/>
<div class="bg-dark">
<vs-row vs-w="12">
  <vs-col vs-type="flex" vs-lg="7" vs-sm="4" vs-xs="12">
   <template>
  <vs-button type="transparent" size="small"><feather-icon icon="PlayIcon"/></vs-button>
 <!--  <vs-button type="transparent"  color="rgb(67,70,77)"><feather-icon icon="PauseIcon"/></vs-button>
  <vs-button type="transparent"  color="rgb(67,70,77)"><feather-icon icon="StopCircleIcon"/></vs-button> -->
  <vs-button type="transparent"  size="small"><feather-icon icon="CameraIcon"/></vs-button>
 <vs-button type="transparent" size="small"><feather-icon icon="DiscIcon"/></vs-button>
  <p class="bg-dark text-white pt-3"> {{value1}} :00:00/ 1:00:00</p>
</template>
  </vs-col>
  <vs-col vs-type="flex"  vs-lg="3" vs-sm="4" vs-xs="12">
  </vs-col>
  <vs-col vs-type="flex"  vs-lg="2" vs-sm="4" vs-xs="12">
  <template>
    <vs-button size="small" type="transparent"><feather-icon icon="Share2Icon"/></vs-button>
    
    <vs-button size="small" type="transparent"><feather-icon icon="Volume2Icon"/></vs-button>
    <vs-button size="small" type="transparent"
@click="popupActive=false"><feather-icon icon="Minimize2Icon"/></vs-button>
  </template>
  </vs-col>
</vs-row>
</div>
</vs-col>

      </vs-popup>
  </div>
</template>
<!-- clipboard popup-->
  <vs-popup class="holamundo" title="MedFly Clipboard" :active.sync="ClipboardActive">
  <template>
    <div class="flex flex-wrap">
  <div class="w-2/3 ml-auto"> <vs-input v-model="text2" class="w-full"/></div>
  <div class="w-1/3 mr-auto"><vs-button @click="onCopy">Copy Link</vs-button></div>
</div>
   
    
</template>
  </vs-popup>
 
</div>
</template>
<script>
// Vue Slider, for more info and examples you can check out https://github.com/NightCatSama/vue-slider-component
import vSelect from 'vue-select';
import axios from 'axios';
import VuePerfectScrollbar from 'vue-perfect-scrollbar';  

export default {
  components:{
    'v-select': vSelect,VuePerfectScrollbar,
  },
  data () {
    return {
       peerConn : '',
      video:'',
      stream:'', 
      hasUserMedia:false,
       
      // used for button status after update button is clicked
      backgroundLoading:'success',
      colorLoading:'#fff',

       text2: 'https://google.com/',

       popupActive:false,
       ClipboardActive:false,

       badge1:2,
       value1:60,
       settings: {maxScrollbarLength: 60},
       selected_gender:'Male',
       genders: ['Male','Female','Others'],
       procedures: ['Dr.Sharath Chandra','Dr.Mahindra Jain'],
       doctors:['Dr.Sharath Chandra','Dr.Mahindra Jain'],
       referrers:['Dr.Mahesh MBBS','Matrix Hospitals'],
       anesthesists:['Dr.Raju MBBS','Dr.Bal Saxena'],
       nurses:['Yamini','Nisha'],
       rstatus:[{ text: 'Select Report Status...', value: null }, 'Normal', 'Abnormal'],
       selected_value:['Main'],
       // vue slider
       sliderValueCustom: '12:20:05',
       sliderDataCustom: ['One', 'Two', 'Three', 'Four'],
       sliderValueDouble: [200, 800],
      // to push images & videos into tabs
      images:[
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
      ],
       videos:[
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-02.jpg'),
        require('@/assets/images/profile/user-uploads/user-03.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-02.jpg'),
        require('@/assets/images/profile/user-uploads/user-03.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-02.jpg'),
        require('@/assets/images/profile/user-uploads/user-03.jpg'),
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-02.jpg'),
        require('@/assets/images/profile/user-uploads/user-03.jpg'),
      ],
      selected_status:null,
      dropdown_status:[
      { value: null, text: 'Select Patient Report Status' },
        { value: 1, text: 'Normal' },
        { value: 2, text: 'Abnormal' },
      ],

     selected_gender:null,
      dropdown_gender:[
        { value: null, text: 'Select Gender' },
        { value: 1, text: 'Male' },
        { value: 2, text: 'Female' },
        { value: 3, text: 'Others' },
      ],
}
  },
  created() {
    
  
  },
   mounted(){
  this.video = this.$refs.videosrc;
  this.videoSrc = true
  this.audioSrc = false
  if(this.$route.query.vsource){
 
   //var server = Peer({port: 9000, path: '/myapp'});
    navigator.getUserMedia =
      navigator.getUserMedia ||
      navigator.webkitGetUserMedia ||
      navigator.mozGetUserMedia ||
      navigator.msGetUserMedia ||
      navigator.oGetUserMedia;
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          //this.video = this.$refs.videosrc; // reInitializing as it doesn't work sometime.
          this.video.srcObject = stream;
          this.stream = stream;           
          this.hasUserMedia = true;
          
        })
        .catch(error => {
          console.log(error);
        });
      }
    }else{

       //var server = Peer({port: 9000, path: '/myapp'});
    navigator.getUserMedia =
      navigator.getUserMedia ||
      navigator.webkitGetUserMedia ||
      navigator.mozGetUserMedia ||
      navigator.msGetUserMedia ||
      navigator.oGetUserMedia;
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          //this.video = this.$refs.videosrc; // reInitializing as it doesn't work sometime.
          this.video.srcObject = stream;
          this.stream = stream;           
          this.hasUserMedia = true;
          
        })
        .catch(error => {
          console.log(error);
        });
      }
   
    }

   },
   methods: {

     
      
    scrollHandle(evt) {
      console.log(evt)
    },
    onCopy() {
            this.$vs.notify({
                title: 'MedFly Alert',
                text: 'Video link copied successfully',
                color: 'success',
                iconPack: 'feather',
                position: 'top-right',
                icon: 'icon-check-circle'
            })
     },
    onError() {
            this.$vs.notify({
                title: 'Failed',
                text: 'Error in copying text',
                color: 'danger',
                iconPack: 'feather',
                position: 'top-right',
                icon: 'icon-alert-circle'
            })
    },
     saveloader(){
      this.$vs.loading({
        background: this.backgroundLoading,
        color: this.colorLoading,
        container: "#button-with-loading",
        scale: 0.45
      })
      setTimeout( ()=> {
        this.$vs.loading.close("#button-with-loading > .con-vs-loading")
      }, 2000);
    }
  }
}
</script>
<style lang="scss">
@import "@/assets/scss/vuexy/pages/profile.scss";

.scroll-area {
  position: relative;
  margin: auto;
  width: 100%;
  height: 250px;
}
 
 /* Container needed to position the overlay. Adjust the width as needed */
.container {
  position: relative;
  width: 100%;
  max-width: 400px;
}

/* Make the image to responsive */
.image {
  width: 200px;
  height: 200px;
}

/* The overlay effect (full height and width) - lays on top of the container and over the image */
.overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  width: 100%;
  opacity: 0;
  transition: .3s ease;
  background: #090909ed;
}

/* When you mouse over the container, fade in the overlay icon*/
.container:hover .overlay {
  opacity: 1;
}

/* The icon inside the overlay is positioned in the middle vertically and horizontally */
.icon {
  color: white;
  font-size: 50px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
}

/* When you move the mouse over the icon, change color */
.fa-user:hover {
  color: primary;
}
</style>