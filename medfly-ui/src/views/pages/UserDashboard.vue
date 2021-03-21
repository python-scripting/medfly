<template>
  <div id="dashboard-analytics">
    <div class="vx-row">
      <!-- CARD 1: CONGRATS -->
      <div class="vx-col w-full lg:w-1/2 mb-base">
        <vx-card slot="no-body" class="text-center bg-primary greet-user">
                   <img src="@/assets/images/pages/decor-bg.png" class="decore-left" alt="Decore Left" width="400">
                   <img src="@/assets/images/pages/decor-bg.png" class="decore-right" alt="Decore Left" width="400">
          <feather-icon icon="AwardIcon" class="p-6 mb-5 bg-primary inline-flex rounded-full text-white shadow" svgClasses="h-8 w-8"></feather-icon>
           <h3 class="xl:w-3/4 lg:w-4/5 md:w-2/3 w-4/5 mx-auto text-white mb-2">Top Referrer of the month</h3>
          <h1 class="mb-5 text-white"><!-- {{ checkpointReward.userName }} --> Continental Hospitals</h1>
           <h5 class="xl:w-3/4 lg:w-4/5 md:w-2/3 w-4/5 mx-auto text-white">Referred 140 patients in this month</h5>
        </vx-card>
      </div>

      <!-- CARD 2: patients-->
      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4 mb-base">
        <statistics-card-line icon="UsersIcon" statistic="2.2K" statisticTitle="Total Patients treated" :chartData="subscribersGained.series" type="area"></statistics-card-line>
      </div>

      <!-- CARD 3: printed test reports -->
      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4 mb-base">
        <statistics-card-line icon="ClipboardIcon" statistic="1.8K" statisticTitle="Total Test Reports" :chartData="ordersRecevied.series" color="success" type="area"></statistics-card-line>
      </div>
    </div>

 <div class="vx-row">
      <!-- CARD 1:  -->
      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4 mb-base">
        <statistics-card-line icon="UsersIcon" statistic="92.6k" statisticTitle="Total Patients treated" :chartData="subscribersGained.series" type="area"></statistics-card-line>
      </div>
      <!-- CARD 2: patients-->
      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4 mb-base">
        <statistics-card-line icon="UsersIcon" statistic="92.6k" statisticTitle="Total Patients treated" :chartData="subscribersGained.series" type="area"></statistics-card-line>
      </div>

      <!-- CARD 3:  -->
      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4 mb-base">
        <statistics-card-line icon="ClipboardIcon" statistic="97.5K" statisticTitle="Total Test Reports" :chartData="ordersRecevied.series" color="success" type="area"></statistics-card-line>
      </div>
      <!-- CARD 4  Data Usage-->
      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4 mb-base">

        <statistics-card-line icon="DatabaseIcon" statistic="2TB/Month" statisticTitle="Data Usage (limit exceeded)" :chartData="ordersRecevied.series" color="dark" type="area"></statistics-card-line>

      </div>
    </div>
    <div class="vx-row">
      <!-- CARD 9: DISPATCHED ORDERS -->
      <div class="vx-col w-full">
        <vx-card title="Pending Reports">
          <div slot="no-body" class="mt-4">
            <vs-table :data="dispatchedOrders" class="table-dark-inverted">
              <template slot="thead">
                <vs-th>S NO.</vs-th>
                <vs-th>MFID</vs-th>
                <vs-th>PNAME</vs-th>
                <vs-th>DOR</vs-th>
              </template>

              <template slot-scope="{data}">
                <vs-tr :key="indextr" v-for="(tr, indextr) in data">
                  <vs-td :data="data[indextr]">
                    <span>#{{data[indextr]}}</span>
                  </vs-td>
                </vs-tr>
              </template>
            </vs-table>
          </div>

        </vx-card>
      </div>
    </div>

  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import StatisticsCardLine from '@/components/statistics-cards/StatisticsCardLine.vue'
import analyticsData from '../ui-elements/card/analyticsData.js'
import VxTimeline from '@/components/timeline/VxTimeline'

export default {
  data () {
    return {
      checkpointReward: {},
      subscribersGained: {},
      ordersRecevied: {},
      salesBarSession: {},
      supportTracker: {},
      productsOrder: {},
      salesRadar: {},

      timelineData: [
        {
          color: 'primary',
          icon: 'PlusIcon',
          title: 'Client Meeting',
          desc: 'Bonbon macaroon jelly beans gummi bears jelly lollipop apple',
          time: '25 mins Ago'
        },
        {
          color: 'warning',
          icon: 'MailIcon',
          title: 'Email Newsletter',
          desc: 'Cupcake gummi bears soufflé caramels candy',
          time: '15 Days Ago'
        },
        {
          color: 'danger',
          icon: 'UsersIcon',
          title: 'Plan Webinar',
          desc: 'Candy ice cream cake. Halvah gummi bears',
          time: '20 days ago'
        },
        {
          color: 'success',
          icon: 'LayoutIcon',
          title: 'Launch Website',
          desc: 'Candy ice cream cake. Halvah gummi bears Cupcake gummi bears soufflé caramels candy.',
          time: '25 days ago'
        },
        {
          color: 'primary',
          icon: 'TvIcon',
          title: 'Marketing',
          desc: 'Candy ice cream cake. Halvah gummi bears Cupcake gummi bears.',
          time: '28 days ago'
        }
      ],


      analyticsData,
      dispatchedOrders: []
    }
  },
  components: {
    VueApexCharts,
    StatisticsCardLine,
    VxTimeline
  },
  created () {
    //  User Reward Card
    this.$http.get('/api/user/checkpoint-reward')
      .then((response) => { this.checkpointReward = response.data })
      .catch((error)   => { console.log(error) })

      // Subscribers gained - Statistics
    this.$http.get('/api/card/card-statistics/subscribers')
      .then((response) => { this.subscribersGained = response.data })
      .catch((error)   => { console.log(error) })

      // Orders - Statistics
    this.$http.get('/api/card/card-statistics/orders')
      .then((response) => { this.ordersRecevied = response.data })
      .catch((error)   => { console.log(error) })

      // Sales bar - Analytics
    this.$http.get('/api/card/card-analytics/sales/bar')
      .then((response) => { this.salesBarSession = response.data })
      .catch((error)   => { console.log(error) })

      // Support Tracker
    this.$http.get('/api/card/card-analytics/support-tracker')
      .then((response) => { this.supportTracker = response.data })
      .catch((error)   => { console.log(error) })

      // Products Order
    this.$http.get('/api/card/card-analytics/products-orders')
      .then((response) => { this.productsOrder = response.data })
      .catch((error)   => { console.log(error) })

      // Sales Radar
    this.$http.get('/api/card/card-analytics/sales/radar')
      .then((response) => { this.salesRadar = response.data })
      .catch((error)   => { console.log(error) })

      // Dispatched Orders
    this.$http.get('/api/table/dispatched-orders')
      .then((response) => { this.dispatchedOrders = response.data })
      .catch((error)   => { console.log(error) })
  }
}
</script>

<style lang="scss">
/*! rtl:begin:ignore */
#dashboard-analytics {
  .greet-user{
    position: relative;

    .decore-left{
      position: absolute;
      left:0;
      top: 0;
    }
    .decore-right{
      position: absolute;
      right:0;
      top: 0;
    }
  }

  @media(max-width: 576px) {
    .decore-left, .decore-right{
      width: 140px;
    }
  }
}
/*! rtl:end:ignore */
</style>
