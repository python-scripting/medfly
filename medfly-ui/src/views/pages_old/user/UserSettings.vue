<template>
  <vs-tabs :position="isSmallerScreen ? 'top' : 'left'" class="tabs-shadow-none" id="profile-tabs" :key="isSmallerScreen">

    <!-- GENERAL -->
    <vs-tab icon-pack="feather" icon="icon-zap" :label="!isSmallerScreen ? 'Digital Signature' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <UserDigitalSignature />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-user" :label="!isSmallerScreen ? 'Anesthesist' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <SubRoleAnesthesist />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-user" :label="!isSmallerScreen ? 'Assistant' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <SubRoleAssistant />
      </div>
    </vs-tab>
     <vs-tab icon-pack="feather" icon="icon-user" :label="!isSmallerScreen ? 'Referrer' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <SubRoleReferrer />
      </div>
    </vs-tab>
     <vs-tab icon-pack="feather" icon="icon-user" :label="!isSmallerScreen ? 'Nurse' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <SubRoleNurse />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-lock" :label="!isSmallerScreen ? 'Change Password' : ''">
      <div class="tab-change-pwd md:ml-4 md:mt-0 mt-4 ml-0">
        <UserChangePassword />
      </div>
    </vs-tab>
  </vs-tabs>
</template>

<script>
import UserChangePassword from './UserChangePassword.vue'
import SubRoleNurse from './SubRoleNurse.vue'
import SubRoleReferrer from './SubRoleReferrer.vue'
import SubRoleAnesthesist from './SubRoleAnesthesist.vue'
import SubRoleAssistant from './SubRoleAssistant.vue'
import UserDigitalSignature from './UserDigitalSignature.vue'
export default {
  components: {
    UserChangePassword,
    SubRoleNurse,
    SubRoleReferrer,
    SubRoleAnesthesist,
    SubRoleAssistant,
    UserDigitalSignature,
  },
  data () {
    return {

    }
  },
  computed: {
    isSmallerScreen () {
      return this.$store.state.windowWidth < 768
    }
  }
}
</script>

<style lang="scss">
#profile-tabs {
  .vs-tabs--content {
    padding: 0;
  }
}
.tr_line{
    border-top:1px solid #f2f0f0;
  }
.CustomHeight{
      height: 530px;
      max-height: 700px;
  }
</style>