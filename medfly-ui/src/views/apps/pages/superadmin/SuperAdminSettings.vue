<template>
  <vs-tabs :position="isSmallerScreen ? 'top' : 'left'" class="tabs-shadow-none" id="profile-tabs" :key="isSmallerScreen">

    <!-- GENERAL -->
    <vs-tab icon-pack="feather" icon="icon-plus-square" :label="!isSmallerScreen ? 'Hospital' : ''">
      <div class="tab-general md:ml-4 md:mt-0 mt-4 ml-0">
        <SuperAdminHospital/>
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-layers" :label="!isSmallerScreen ? 'Department' : ''">
      <div class="tab-social-links md:ml-4 md:mt-0 mt-4 ml-0">
        <SuperAdminDepartment />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-package" :label="!isSmallerScreen ? 'Procedure' : ''">
      <div class="tab-social-links md:ml-4 md:mt-0 mt-4 ml-0">
        <SuperAdminProcedure />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-users" :label="!isSmallerScreen ? 'Role' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <SuperAdminRole />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-user-plus" :label="!isSmallerScreen ? 'User' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <SuperAdminUser />
      </div>
    </vs-tab>
     <vs-tab icon-pack="feather" icon="icon-git-pull-request" :label="!isSmallerScreen ? 'Role Permissions' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <SuperAdminRolePermissions />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-lock" :label="!isSmallerScreen ? 'Change Password' : ''">
      <div class="tab-change-pwd md:ml-4 md:mt-0 mt-4 ml-0">
        <SuperAdminChangePassword />
      </div>
    </vs-tab>
  </vs-tabs>
</template>

<script>
import SuperAdminChangePassword from './SuperAdminChangePassword.vue'
import SuperAdminHospital from './SuperAdminHospital.vue'
import SuperAdminRole from './SuperAdminRole.vue'
import SuperAdminProcedure from './SuperAdminProcedure.vue'
import SuperAdminDepartment from './SuperAdminDepartment.vue'
import SuperAdminUser from './SuperAdminUser.vue'
import SuperAdminRolePermissions from './SuperAdminRolePermissions.vue'
export default {
  components: {
    SuperAdminChangePassword,
    SuperAdminHospital,
    SuperAdminRole,
    SuperAdminProcedure,
    SuperAdminUser,
    SuperAdminDepartment,
    SuperAdminRolePermissions
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
</style>
