<template>
  <Navbar></Navbar>
  <div class="container-fluid mt-3 position-relative">
    <ToastMessages></ToastMessages>
    <router-view />
  </div>
  <div class="container mt-5">
    <form class="row justify-content-center" @submit.prevent="signIn">
      <div class="col-md-6">
        <h1 class="h3 mb-3 font-weight-normal">請先登入</h1>
        <div class="mb-2">
          <label for="inputEmail" class="sr-only">Email address</label>
          <input
            type="email"
            id="inputEmail"
            class="form-control"
            placeholder="Email address"
            required
            autofocus
            v-model="user.username"
          />
        </div>
        <div class="mb-2">
          <label for="inputPassword" class="sr-only">Password</label>
          <input
            type="password"
            id="inputPassword"
            class="form-control"
            placeholder="Password"
            required
            v-model="user.password"
          />
        </div>
        <div class="text-end mt-4">
          <button class="btn btn-lg btn-primary btn-block" type="submit">
            登入
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import ToastMessages from '@/components/ToastMessages.vue'
import emitter from '@/methods/emitter'

export default {
  components: {
    Navbar,
    ToastMessages
  },
  provide() {
    return {
      emitter
    }
  },
  data() {
    return {
      user: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    signIn() {
      const api = `${process.env.VUE_APP_API}admin/signin`
      this.$http
        .post(api, this.user)
        .then((res) => {
          if (res.data.success) {
            const { token, expired } = res.data
            document.cookie = `hexToken=${token}; expires=${new Date(expired)}`
            this.$router.push('/dashboard/products')
          } else {
            emitter.emit('push-message', {
              style: 'danger',
              title: '登入失敗',
              content: res.data.message.join('、')
            })
          }
        })
        .catch((err) => {
          emitter.emit('push-message', {
            style: 'danger',
            title: '登入失敗',
            content: err.response.data.message.join('、')
          })
        })
    }
  }
}
</script>
