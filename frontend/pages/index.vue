<template>
  <v-row justify="center">
    <v-col cols="12" sm="8" md="6">
      <div
        v-if="loading"
        class="w-100 d-flex flex-column align-center accent--text mt-16"
      >
        <v-progress-circular indeterminate />
        <div>Loading last known data...</div>
        <div>socket: {{ socket?.readyStatus }}</div>
      </div>
      <div
        v-else
        class="w-100 d-flex flex-column align-center accent--text text-center mt-16"
      >
        <div>
          <v-icon x-large>mdi-lightbulb-{{ on ? 'on' : 'off' }}</v-icon>
        </div>
        <br />
        <div>lights status at home: {{ on ? 'ON' : 'OFF' }}</div>
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
      on: true,
      time: new Date(),
      socket: null,
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
      this.on = res.data.on
      this.sent_at = new Date(Date.parse(res.data.sent_at))

      this.socket = new WebSocket(
        window.location.toString().replace('http', 'ws') + 'api/ws/home-light/', // TODO check
        ['notif', this.$auth.strategy.token.get().slice(7)]
      )
      this.socket.onmessage = (msg) => {
        try {
          const data = JSON.parse(msg.data)
          this.on = data.on
          this.sent_at = data.sent_at
        } catch (err) {
          console.error(err)
        }
      }
    })
  },
  beforeDestroy() {
    this.socket?.close()
  },
}
</script>
