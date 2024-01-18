<template>
  <v-row justify="center">
    <v-col cols="12" sm="8" md="6">
      <div
        v-if="loading"
        class="w-100 d-flex flex-column align-center accent--text mt-16"
      >
        <v-progress-circular indeterminate />
        <div>Loading last known data...</div>
      </div>
      <div
        v-else
        class="w-100 d-flex flex-column align-center accent--text text-center mt-16"
      >
        <div>lux level at home: {{ lux }}</div>
        <div>
          device time when sending this information was
          {{ sent_at.toLocaleString() }}
        </div>
        <div>or in jalaali: {{ sent_at.toLocaleString('fa') }}</div>

        <v-btn @click="ToggleLamp" class="mt-16" color="info"
          >Toggle Lamp</v-btn
        >
      </div>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      loading: true,
      lux: 0,
      time: new Date(),
    }
  },
  methods: {
    ToggleLamp() {
      this.$axios.put('/api/home-light/').then((res) => {
        console.log(res)
      })
    },
  },
  created() {
    this.$axios.get('/api/home-light/').then((res) => {
      this.loading = false
      this.lux = res.data.lux
      this.sent_at = new Date(Date.parse(res.data.sent_at))
    })
  },
}
</script>
