// axios
import axios from 'axios'
// Vuex Store
import store from '@/store/index'


const baseURL = "http://localhost:8000/"

const instance = axios.create({
  baseURL: baseURL
  // You can add your headers here
})



instance.interceptors.request.use(function(config) {
  
  const token = store.getters['getuser']['token'];
  if ( token != null ) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, function(err) {
  
  return Promise.reject(err);
});

export default instance;