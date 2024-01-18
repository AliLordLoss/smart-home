<template>
  <v-row justify="center">
    <v-col cols="12" sm="8" md="6">
      <div class="w-100 accent--text text-center text-h6 mt-16">
        Hello dear {{ $auth.user.username }}!
      </div>

      <div class="w-100 d-flex flex-column align-center mt-4">
        <div class="d-flex">
          <v-icon>
            mdi-weather-{{ $vuetify.theme.dark ? 'sunny' : 'night' }}
          </v-icon>
          <v-switch v-model="$vuetify.theme.dark" color="primary" />
        </div>

        <v-btn @click="handleLogout" class="mt-8" color="error" :ripple="false">
          Logout
        </v-btn>
      </div>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      dark: true,
    }
  },
  methods: {
    handleLogout() {
      this.$axios
        .post('/api/logout/', {
          refresh: this.$auth.strategy.refreshToken.get(),
        })
        .then(() => {
          this.$auth.reset()
        })
        .catch((err) => {
          console.error(err?.response)
          this.$auth.reset()
        })
    },
  },
}
</script>
