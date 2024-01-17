<template>
  <v-row justify="center">
    <v-col cols="12" sm="8" md="6" class="d-flex flex-column pt-16">
      <div class="text-h3 w-100 text-center my-16">Welcome!</div>

      <v-form @submit.prevent="handleLogin" class="w-100 mt-16">
        <v-text-field v-model="username" label="Username" filled />
        <v-text-field
          v-model="password"
          @click:append="showPassword = !showPassword"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          :type="showPassword ? 'text' : 'password'"
          label="Password"
          filled
        />

        <v-btn color="success" class="mt-4" width="100%" type="submit" large
          >Login</v-btn
        >
      </v-form>
    </v-col>
  </v-row>
</template>

<script>
export default {
  layout: 'auth',
  auth: 'guest',
  data() {
    return {
      username: '',
      password: '',
      showPassword: false,
    }
  },
  methods: {
    async handleLogin() {
      try {
        await this.$auth.loginWith('local', {
          data: { username: this.username, password: this.password },
        })
        this.$router.push('/')
      } catch (err) {
        console.log(err)
      }
    },
  },
}
</script>
