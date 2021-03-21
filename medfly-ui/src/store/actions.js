/*=========================================================================================
  File Name: actions.js
  Description: Vuex Store - actions
  ----------------------------------------------------------------------------------------
  Item Name: Vuexy - Vuejs, HTML & Laravel Admin Dashboard Template
  Author: Pixinvent
  Author URL: http://www.themeforest.net/user/pixinvent
==========================================================================================*/

import axios from '@/axios.js';

const actions = {
    

    // /////////////////////////////////////////////
    // COMPONENTS
    // /////////////////////////////////////////////

    // Vertical NavMenu
    updateVerticalNavMenuWidth({ commit }, width) {
      commit('UPDATE_VERTICAL_NAV_MENU_WIDTH', width)
    },

    // VxAutoSuggest
    updateStarredPage({ commit }, payload) {
      commit('UPDATE_STARRED_PAGE', payload)
    },

    // The Navbar
    arrangeStarredPagesLimited({ commit }, list) {
      commit('ARRANGE_STARRED_PAGES_LIMITED', list)
    },
    arrangeStarredPagesMore({ commit }, list) {
      commit('ARRANGE_STARRED_PAGES_MORE', list)
    },

    // /////////////////////////////////////////////
    // UI
    // /////////////////////////////////////////////

    toggleContentOverlay({ commit }) {
      commit('TOGGLE_CONTENT_OVERLAY')
    },
    updateTheme({ commit }, val) {
      commit('UPDATE_THEME', val)
    },

    // /////////////////////////////////////////////
    // User/Account
    // /////////////////////////////////////////////

    updateUserInfo({ commit }, payload) {
      commit('UPDATE_USER_INFO', payload)
    },
    
 userLogin({ commit }, item) {
  return new Promise((resolve,reject) => {
    axios.post("login/", item)
      .then((response) => {        //alert(JSON.stringify(response.data));
        
        localStorage.setItem('token', response.data.access)
        localStorage.setItem('user', response.data)
       
        const user = response.data;
        commit('auth_success', user)       
       resolve(response)
      })
      .catch((error) => { 
        //alert(JSON.stringify(error.response.data.result.error));
        reject(error) }
      )
  })
},

logout({ commit }, item) {
  return new Promise((resolve,reject) => {
     localStorage.removeItem('user');
     localStorage.removeItem('token');
      commit('logout');
      resolve('logout');
    
  })
},

getHospitalData({commit} ,payload){
  return new Promise((resolve ,reject)=>{

    axios.post("hospital/" ,payload)
    .then((res)=>{
      resolve(res);
    })
    .catch((err)=>{
      reject(reject);
    });

  });

}


}

export default actions
