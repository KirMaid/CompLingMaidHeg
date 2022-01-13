<template>
  <div class="container-fluid">
    <h1>{{ msg }}</h1>
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
  },
  mounted() {
    this.getPosts();
  },
  props: {
    msg: String,
  },
};
</script>

<style scoped>
</style>
