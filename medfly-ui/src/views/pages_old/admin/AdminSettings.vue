<template>
  <vs-tabs :position="isSmallerScreen ? 'top' : 'left'" class="tabs-shadow-none" id="profile-tabs" :key="isSmallerScreen">

    <!-- GENERAL -->
    <vs-tab icon-pack="feather" icon="icon-plus-square" :label="!isSmallerScreen ? 'Hospital' : ''">
      <div class="tab-general md:ml-4 md:mt-0 mt-4 ml-0">
        <AdminHospital/>
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-layers" :label="!isSmallerScreen ? 'Department' : ''">
      <div class="tab-social-links md:ml-4 md:mt-0 mt-4 ml-0">
        <AdminDepartment />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-package" :label="!isSmallerScreen ? 'Procedure' : ''">
      <div class="tab-social-links md:ml-4 md:mt-0 mt-4 ml-0">
        <AdminProcedure />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-users" :label="!isSmallerScreen ? 'Role' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <AdminRole />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-user-plus" :label="!isSmallerScreen ? 'User' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <AdminUser />
      </div>
    </vs-tab>
     <vs-tab icon-pack="feather" icon="icon-git-pull-request" :label="!isSmallerScreen ? 'Role Permissions' : ''">
      <div class="tab-text md:ml-4 md:mt-0 mt-4 ml-0">
        <AdminRolePermissions />
      </div>
    </vs-tab>
    <vs-tab icon-pack="feather" icon="icon-lock" :label="!isSmallerScreen ? 'Change Password' : ''">
      <div class="tab-change-pwd md:ml-4 md:mt-0 mt-4 ml-0">
        <AdminChangePassword />
      </div>
    </vs-tab>
  </vs-tabs>
</template>

<script>
import AdminChangePassword from './AdminChangePassword.vue'
import AdminHospital from './AdminHospital.vue'
import AdminRole from './AdminRole.vue'
import AdminProcedure from './AdminProcedure.vue'
import AdminDepartment from './AdminDepartment.vue'
import AdminUser from './AdminUser.vue'
import AdminRolePermissions from './AdminRolePermissions.vue'
export default {
  components: {
    AdminChangePassword,
    AdminHospital,
    AdminRole,
    AdminProcedure,
    AdminUser,
    AdminDepartment,
    AdminRolePermissions
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
