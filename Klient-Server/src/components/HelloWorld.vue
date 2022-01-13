<template>
  <div class="container-fluid">
    <nav class="navbar navbar-light justify-content-center">
      <a class="navbar-brand" @click="Krauler">{{ Krauler_text }}</a>
    </nav>
    <ul class="list-group list-group-flush">
      <li class="list-group-item" v-for="new_one in news" :key="new_one._id">
        <p>{{ new_one.date }}</p>
        <p class="fw-bold">{{ new_one.title }}</p>
        <p>{{ new_one.content }}</p>
        <p>
          <a
            class="link-primary"
            target="_blank"
            v-bind:href="new_one.videolink"
            >{{ new_one.videolink }}</a
          >
        </p>
        <p>
          <a class="link-primary" target="_blank" v-bind:href="new_one.link">{{
            new_one.link
          }}</a>
        </p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      news: [],
      Krauler_text: "Запуск Краулера",
    };
  },
  methods: {
    getPosts() {
      this.$http
        .get("http://192.168.0.106:3000")
        .then((response) => {
          this.news = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    Krauler() {
      this.Krauler_text = "Краулер запущен, ожидайте";
      this.$http
        .post("http://192.168.0.106:3000", { timeout: 9 })
        .then((response) => {
          // data1 = response.data;
          console.log(response.data);
          if (response.data == "Ok") {
            this.getPosts();
            this.Krauler_text = "Запуск Краулера";
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    this.getPosts();
  },
};
</script>

<style scoped>
</style>
