
<template>
    <div id="profile-page">
        <div class="vx-row">       
           <div class="vx-col w-full lg:w-1/2">
             <vx-card title="Hospital Video Devices List">

		    <VuePerfectScrollbar class="scroll-video-area" v-once :settings="settings" @ps-scroll-y="scrollHandle">
		    <div class="vx-row px-5">
 			 <div v-for="video in live_video_list">
 	 		 <div class="container mb-2">
                <img :src="video" alt="video_thumnails" class="video">
                <div class="video-overlay">
                  <div class="flex flex-col justify-between">
                    <div class="flex">
                          <vs-button color="success" type="border" size="small" class="icon" icon-pack="feather" icon="icon-play"></vs-button>
                     <div class="w-1/2">
                       <vs-label class="text-white mt-1 ml-1">OT-5</vs-label>
                     </div>
                     <div class="w-1/2">
                       	<vs-label class="text-white mt-1 ml-1">MF-2</vs-label>
                     </div>
                    </div>
                  </div>
                </div>
              </div>
          </div>        
    	</div>
    </VuePerfectScrollbar>
  </vx-card>
</div>
	     <div class="vx-col w-full lg:w-1/2">
            <vx-card>
            <video-player ref="player" class="media-video-player card-video" :options="playerOptions(media)"/>
            </vx-card>
         </div>

         </div>
        </div>
    </div>
</template>

<script>
import { videoPlayer } from 'vue-video-player'
import 'video.js/dist/video-js.css'
import VuePerfectScrollbar from 'vue-perfect-scrollbar'

export default {
  components: {
    videoPlayer,VuePerfectScrollbar
  },
  data () {
    return {
 
    	settings: {maxScrollbarLength: 60},
       live_video_list: [
        require('@/assets/images/profile/user-uploads/user-01.jpg'),
        require('@/assets/images/profile/user-uploads/user-02.jpg'),
        require('@/assets/images/profile/user-uploads/user-04.jpg'),
        require('@/assets/images/profile/user-uploads/user-03.jpg'),
        require('@/assets/images/profile/user-uploads/user-05.jpg'),
        require('@/assets/images/profile/user-uploads/user-06.jpg'),
        require('@/assets/images/profile/user-uploads/user-07.jpg'),
        require('@/assets/images/profile/user-uploads/user-08.jpg'),
        require('@/assets/images/profile/user-uploads/user-09.jpg'),
        require('@/assets/images/profile/user-uploads/user-06.jpg'),
        require('@/assets/images/profile/user-uploads/user-07.jpg'),
        require('@/assets/images/profile/user-uploads/user-08.jpg'),
        require('@/assets/images/profile/user-uploads/user-06.jpg'),
        require('@/assets/images/profile/user-uploads/user-07.jpg'),
        require('@/assets/images/profile/user-uploads/user-08.jpg'),
        require('@/assets/images/profile/user-uploads/user-06.jpg'),
        require('@/assets/images/profile/user-uploads/user-07.jpg'),
        require('@/assets/images/profile/user-uploads/user-08.jpg')
      ],
 
    }
},

 methods: {
    scrollHandle(evt) {
      console.log(evt)
    },
},
computed: {
    playerOptions () {
      return (media) => {
        return {
          height: '600',
          fluid: true,
          autoplay: false,
          muted: true,
          language: 'en',
          playbackRates: [0.7, 1.0, 1.5, 2.0],
          sources: 'http://vjs.zencdn.net/v/oceans.mp4',
          poster: require('@/assets/images/profile/user-uploads/user-04.jpg')
        }
      }
    }
  }

  }

</script>

<style lang="scss">
@import "@/assets/scss/vuexy/pages/profile.scss";

.scroll-video-area {
  position: relative;
  margin: auto;
  width: 100%;
  height: 490px;
}
.card-video {
.video-js {
    height: 530px;
}
 }
 
 /* Container needed to position the overlay. Adjust the width as needed */
.container {
  position: relative;
  width: 100%;
  max-width: 400px;
}

/* Make the video to responsive */
.video {
  width: 110px;
  height: 100px;

}

/* The overlay effect (full height and width) - lays on top of the container and over the image */
.video-overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100px;
  width: 125px;
  opacity: .9;
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
