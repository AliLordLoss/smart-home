<template>
  <v-app dark>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-bottom-navigation app shift grow color="teal">
      <v-btn
        v-for="route in routes"
        :key="route.path"
        :to="route.path"
        :ripple="false"
        style="height: inherit"
        ref="link"
        plain
      >
        <v-icon>{{ route.icon }}</v-icon>

        <span>{{ route.name }}</span>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      routes: [
        { path: '/', icon: 'mdi-home-automation', name: 'Home' },
        { path: '/profile', icon: 'mdi-account', name: 'Profile' },
      ],
    }
  },
}
</script>
