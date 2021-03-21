<template>
  <!-- NOTIFICATIONS -->
  <vs-dropdown vs-custom-content vs-trigger-click class="cursor-pointer">
    <feather-icon icon="WifiIcon" class="cursor-pointer mt-1 sm:mr-6 mr-2"/>

    <vs-dropdown-menu class="notification-dropdown dropdown-custom vx-navbar-dropdown">

      <div class="notification-top text-center p-5 bg-primary text-white">
        <h6 class="text-white">Available Wifi's</h6>
        <p class="opacity-75">Connect to your wifi network </p>
      </div>

      <component :is="scrollbarTag" ref="mainSidebarPs" class="scroll-area--nofications-dropdown p-0 mb-10" :settings="settings" :key="$vs.rtl">
        <ul class="bordered-items">
          <li v-for="ntf in unreadNotifications" :key="ntf.index" class="flex justify-between px-4 py-4 notification cursor-pointer">
            <div class="flex items-start">
              <feather-icon icon="WifiIcon"></feather-icon>
              <div class="mx-2">
                <small>Wifi 1</small>
              </div>
            </div>
           
          </li>
        </ul>
      </component>

      <div class="
        checkout-footer
        fixed
        bottom-0
        rounded-b-lg
        text-primary
        w-full
        p-2
        font-semibold
        text-center
        border
        border-b-0
        border-l-0
        border-r-0
        border-solid
        d-theme-border-grey-light
        cursor-pointer">
        <span>View All</span>
      </div>
    </vs-dropdown-menu>
  </vs-dropdown>
</template>

<script>
import VuePerfectScrollbar from 'vue-perfect-scrollbar'

export default {
  components: {
    VuePerfectScrollbar
  },
  data() {
    return {
      unreadNotifications: [
          {
            index    : 0,
            title    : 'Video Link Shared',
            msg      : 'Dr.xyz shares video link for verify',
            icon     : 'VideoIcon',
            category : 'primary'
          },
          { index    : 1,
            title    : 'MedFly Payment Reminder',
            msg      : 'Payment Due for the month February',
            icon     : 'PocketIcon',
          },
      ],
      settings: {
        maxScrollbarLength: 60,
        wheelSpeed: .60,
      },
    }
  },
  computed: {
    scrollbarTag() { return this.$store.getters.scrollbarTag }
  },
  methods: {
   
  }
}

</script>

