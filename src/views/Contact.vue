<template>
  <div class="contact">
    <h1>This is contact</h1>
    <v-date-picker :value="null" color="red" is-dark is-range />
    <v-btn text
      >November
      <v-icon right> mdi-chevron-down </v-icon>
    </v-btn>
    <div>Selected: {{ selected }}</div>

    <select v-model="selected" class="select-month">
      <option disabled value="">Please select one</option>
      <option>A</option>
      <option>B</option>
      <option>C</option>
    </select>
    <div>Selected: {{ selected }}</div>

    <select v-model="selected">
      <option disabled value="">Please select one</option>
      <option>A</option>
      <option>B</option>
      <option>C</option>
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selected: 'A'
    }
  }
};
</script>

<style lang="scss" scoped>
.select-month {
  padding: 10px;
  border: 2px solid #00897b;
  border-radius: 10px;
}
.select-month:focus {
  border-color: #00897b!important;
}
</style>
