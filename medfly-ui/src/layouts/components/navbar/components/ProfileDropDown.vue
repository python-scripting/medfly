<template>
  <div class="the-navbar__user-meta flex items-center" >

    <div class="text-right leading-tight hidden sm:block">
      <p class="font-semibold">{{ activeUserInfo.displayName }} </p>
      <small>Available</small>
    </div>
    

    <vs-dropdown vs-custom-content vs-trigger-click class="cursor-pointer">

      <div class="con-img ml-3">

        <img  key="onlineImg" :src="checkProperty(activeUserInfo , 'photoURL')" @error="getProfilePhoto($event, 'O')" alt="user-img" width="40" height="40" class="rounded-full shadow-md cursor-pointer block" />
        
      </div>

      <vs-dropdown-menu class="vx-navbar-dropdown">
        <ul style="min-width: 9rem">

          <li class="flex py-2 px-4 cursor-pointer hover:bg-primary hover:text-white">
            <feather-icon icon="EditIcon" svgClasses="w-4 h-4" />
            <span class="ml-2">Edit</span>
          </li>


          <li class="flex py-2 px-4 cursor-pointer hover:bg-primary hover:text-white"   @click="$router.push('/apps/chat').catch(() => {})">
            <feather-icon icon="MessageSquareIcon" svgClasses="w-4 h-4" />
            <span class="ml-2">Chat</span>
          </li>

          <vs-divider class="m-1" />

          <li
            class="flex py-2 px-4 cursor-pointer hover:bg-primary hover:text-white"
            @click="logout">
            <feather-icon icon="LogOutIcon" svgClasses="w-4 h-4" />
            <span class="ml-2">Logout</span>
          </li>
        </ul>
      </vs-dropdown-menu>
    </vs-dropdown>
  </div>
</template>

<script>
  import _ from "lodash";
export default {
  data() {
    return {

    }
  },
  computed: {
    activeUserInfo() {
      if(_.has(this.$store.state , 'user')){
         return this.$store.state.user;

      }else{
        alert();

      return JSON.parse(localStorage.getItem('user'));

      }
     
    }
  },
  methods: {
    logout() {
       this.$store.dispatch("logout")
       .then((res)=>{
          this.$router.push('/login').catch(() => {})
       });
        
    },
    
  }
}
</script>
