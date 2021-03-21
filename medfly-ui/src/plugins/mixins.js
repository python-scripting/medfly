//const user = store.getters.getuser;
//import store from '../store'
import Vue from 'vue'
import VueToastr2 from 'vue-toastr-2'
import 'vue-toastr-2/dist/vue-toastr-2.min.css'
import mprofileImage from "@/assets/images/mprofile.svg"
import fprofileImage from "@/assets/images/fprofile.svg"
import clientProfile from "@/assets/images/client_profile.png"


 
window.toastr = require('toastr')
 
Vue.use(VueToastr2)

import _ from "lodash";
export default {

  computed:{
    currentRoute(){
     
       return this.$route.name.trim() ;
      
    
},
},
  
  mounted(){
  
    
    this.userdata = this.$store.getters['getuser']; 
    
  },

  watch: {
    
  },

  data: () => ({
    
    
    formSubmited:false,
    tenantId:'',
    userdata:null,
    openFilter:false,
    closeFileSelection:false,
    enableFileSelectionFromDocuments:true,
  }),
  
  methods: {
    
    checkProperty(object =null ,mainKey='' ,subKey =''){
      if(object != null && mainKey !='' ){
          if(_.has(object ,mainKey)){

              if(subKey !=''){
                  if( _.has(object[mainKey] ,subKey )){
                      return object[mainKey][subKey];

                  }else{
                      return '--';

                  }


              }else{
                  return object[mainKey];

              }


          }else{
              return '--';
          }


      }else{
          return '--';
      }

  },
    setAltImg(event) { 
      event.target.src = clientProfile
  },
  getProfilePhoto(event ,gender='M'){
   
    if(gender=='M' || gender=='O'){
      event.target.src = mprofileImage
    }else if(gender=='F'){
      event.target.src = fprofileImage
    } else {
      event.target.src =  mprofileImage
    }
   
    
  },
    notify({message='' ,title='' ,type="success"}){
      if(type=="success"){
         this.$toastr.success(message, title, {});
      }else{
          this.$toastr.error(message, title, {});
      }
    
      
    },
    showLoading(){
      this.show_loading =true;
      this.formSubmited =true;
    },
    closeLoading(){
      this.show_loading = false;
      this.formSubmited = false;
    },
    log(data){
      console.log(data);
    },
    
    download_file(value) {
      if(_.has(value , "path")){
        value['url'] = value['path'];
      }
    /*
      value.url = value.url.replace(
        "https://lnaccounting.s3.ap-south-1.amazonaws.com/",
        ""
      );
      */
      // let postdata = { keyName: value.path , "taskId": this.taskDetails['_id']};
      let postdata = { keyName: value.url };

      this.$store.dispatch("getSignedUrl", postdata).then((response) => {
        
        window.open(response.data.result.data);
      });
    },
    
    randomStr(length =5) {
      var result           = '';
      var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
      var charactersLength = characters.length;
      for ( var i = 0; i < length; i++ ) {
         result += characters.charAt(Math.floor(Math.random() * charactersLength));
      }
      return result;
   },
   toggleBodyClass(addRemoveClass, className) {
    const el = document.body;
   
    if (addRemoveClass === 'addClass') {
      el.classList.add(className);
    } else {
      el.classList.remove(className);
    }
  },
    
    
  },
  components: {
   

  },
  created () {
    document.title = "Medfly";
    
    //this.userdata = this.$store.getters['getuser'];


    
},
beforeCreate() {
  //alert();
  //console.log(this.$store.getters['getuser'])
  //this.userdata = this.$store.getters['getuser'];
  //console.log(this.showLoading);
}

  

 }

 