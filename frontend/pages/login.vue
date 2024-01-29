<template>
  <v-row justify="center">
    <v-col cols="12" sm="8" md="6" class="d-flex flex-column pt-16">
      <div class="text-h3 w-100 text-center my-16">Welcome!</div>

      <v-form v-model="valid" @submit.prevent="handleLogin" class="w-100 mt-16">
        <v-text-field
          v-model="username"
          :rules="[requiredRule]"
          label="Username"
          filled
        />
        <v-text-field
          v-model="password"
          @click:append="showPassword = !showPassword"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          :type="showPassword ? 'text' : 'password'"
          :rules="[requiredRule]"
          label="Password"
          filled
        />

        <v-btn
          color="success"
          class="mt-4"
          width="100%"
          type="submit"
          :ripple="false"
          :disabled="!valid"
          large
        >
          Login
        </v-btn>
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
      valid: true,
      username: '',
      password: '',
      showPassword: false,
      requiredRule: (value) => {
        if (value) return true

        return 'this value is required!'
      },
    }
  },
  methods: {
    async handleLogin() {
      try {
        await this.$auth
          .loginWith('local', {
            data: { username: this.username, password: this.password },
          })
          .then((res) => {
            if (res.headers['content-type'] !== 'application/json')
              throw new Error('Invalid response received!')
          })
      } catch (err) {
        console.error(err)
      }
    },
  },
}
</script>
