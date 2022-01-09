import { createApp } from 'vue'
import App from './App.vue'
// import * as Vue from 'vue' // in Vue 3
import axios from 'axios'
import VueAxios from 'vue-axios'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

const app = createApp(App)
app.use(VueAxios, axios)
app.mount('#app')
    // createApp(App).mount('#app')