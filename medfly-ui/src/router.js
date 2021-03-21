/*=========================================================================================
  File Name: router.js
  Description: Routes for vue-router. Lazy loading is enabled.
  ----------------------------------------------------------------------------------------
==========================================================================================*/


import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store/index'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    scrollBehavior () {
        return { x: 0, y: 0 }
    },
    routes: [

        {
    // =============================================================================
    // MAIN LAYOUT ROUTES
    // =============================================================================
            path: '',
            component: () => import('./layouts/main/Main.vue'),
            children: [
        // =============================================================================
        // Theme Routes= 
        // ============================================================================
        // =============================================================================
        // Role Routes
        // ==o=========================================================================
             
              {
                path: '/',
                name: 'home',
                meta: {
                  requiresAuth: true,
                  title:'Dashboard',
                  
                },
                component: () => import('./views/pages/Home.vue')
              },
              
         // =============================================================================
        // Superadmin Routes
        // ============================================================================

              {
                path: '/superadmin',
                name: 'SuperAdminSettings',
                component: () => import('./views/pages/superadmin/SuperAdminSettings.vue')
              },
              {
                path: '/admin',
                name: 'AdminSettings',
                component: () => import('./views/pages/admin/AdminSettings.vue')
              },
              {
                path: '/user',
                name: 'UserSettings',
                component: () => import('./views/pages/user/UserSettings.vue')
              },
        // =============================================================================
        // Template Designer
        // ============================================================================
            {
                 path: '/template/designer',
                 name: 'designer',
                 component: () => import('./views/pages/Template/RMain.vue'),
            },      
        // =============================================================================
        // General Routes(outside superadmin, admin,user) 
        // ============================================================================
            {
                 path: '/apps/chat',
                 name: 'chat',
                 component: () => import('./views/apps/chat/Chat.vue'),
                 meta: {
                     rule: 'editor',
                     no_scroll: true
                        }
            },
            {
                path: '/tagcontent',
                name: 'tags',
                component: () => import('./views/pages/Tag_Content.vue')
              },
               {
                path: '/invoice',
                name: 'Invoice',
                component: () => import('./views/pages/admin/Invoice.vue')
              },
              {
                path: '/business_reports',
                name: 'Business Reports',
                component: () => import('./views/pages/Analytical_Reports.vue')
              },
             
              {
                path: '/dashboard',
                name: 'Dashboard',
                component: () => import('./views/DashboardAnalytics.vue')
              },
               
              {
                path: '/videoeditor',
                name: 'Video Editor',
                component: () => import('./views/pages/VideoEditor.vue')
              },
               {
                path: '/templates',
                name: 'Templates',
                component: () => import('./views/pages/Templates.vue')
              },

              {
                path: '/reportdesigner',
                name: 'Report Desiger',
                component: () => import('./views/pages/ReportDesigner.vue')
              },
              {
                path: '/imageeditor',
                name: 'Image Editor',
                component: () => import('./views/pages/ImageEditor.vue')
              },
               {
                path: '/record_search',
                name: 'Search Patients',
                component: () => import('./views/pages/Search.vue')
              },
              {
                path: '/multiviewer',
                name: 'viewer',
                component: () => import('./views/pages/MultiViewer.vue')
              },
            ],
        },
    // =============================================================================
    // FULL PAGE LAYOUTS
    // =============================================================================
        {
            path: '',
            component: () => import('@/layouts/full-page/FullPage.vue'),
            children: [
        // =============================================================================
        // PAGES
        // =============================================================================
              {
                path: '/login',
                name: 'login',
                component: () => import('@/views/pages/Login.vue')
              },
              {
                path: '/pages/error-404',
                name: 'page-error-404',
                component: () => import('@/views/pages/Error404.vue')
              },
            ]
        },

        // Redirect to 404 page, if no match found
        {
            path: '*',
            redirect: '/pages/error-404'
        }
         
    ],

})



router.beforeEach((to, from, next) => {
  //const user = store.getters.getuser;
  
  
    if (!store.getters['isLoggedIn'] && to.path != '/login') {
      next('/login');
      return;
    }else if (store.getters['isLoggedIn'] && to.path == '/login') {
      next('/');
      return;
    }
    
  next()
})


router.afterEach(() => {
  // Remove initial loading
  const appLoading = document.getElementById('loading-bg')
    if (appLoading) {
        appLoading.style.display = "none";
    }
})

export default router
