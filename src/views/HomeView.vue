<template>
  <v-app :style="{ background: $vuetify.theme.themes.light.background }">
    <v-layout row>
      <v-flex md8>
        <v-app
          :style="{ background: $vuetify.theme.themes.dark.background }"
          class="rounded-tr-xl rounded-br-xl"
        >
          <v-container>
            <v-row>
              <v-col cols="12" sm="12">
                <v-app-bar color="rgba(0,0,0,0)" flat class="mx-8 mb-8 mt-3">
                  <v-select
                    :items="cameras"
                    v-model="selected_camera"
                    class="choice-camera mr-3"
                    label="Choice camera"
                    dense
                  >
                  </v-select>
                  <v-btn color="primary" class="mr-3" elevation="2">Request</v-btn>
                  <span class="camera-name">You choose: {{ selected_camera }}</span>
                  <v-spacer></v-spacer>
                  <v-chip class="ma-2" color="white">
                    <v-icon left color="teal"> mdi-clock-time-nine </v-icon>
                    14:02 AM Today May,22
                  </v-chip>
                </v-app-bar>
              </v-col>
               <v-col cols="12" sm="12">
                <v-list two-line> </v-list>
              </v-col>
              <v-col cols="12" sm="24">
                <v-card
                  class="mx-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n15"
                >
                  <v-list-item three-line id="video-analysis">
                    <iframe
                      width="100%"
                      height="500"
                      src="https://www.youtube.com/embed/t8pPdKYpowI"
                      title="YouTube video player"
                      frameborder="0"
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen
                    ></iframe>
                  </v-list-item>
                </v-card>
              </v-col>
              <v-col cols="12" sm="12">
                <v-card
                  class="mx-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n10"
                >
                  <v-app-bar color="rgba(0,0,0,0)" flat class="ma-8">
                    <v-spacer></v-spacer>
                    <v-btn color="teal" text
                      >2019
                      <v-icon right> mdi-chevron-down </v-icon>
                    </v-btn>
                    <v-btn color="teal" rounded dark depressed>Year</v-btn>
                    <v-btn text>Mounth</v-btn>
                  </v-app-bar>
                  <line-chart
                    :data="{
                      '2017-05-13': 2,
                      '2017-05-14': 5,
                      '2017-05-15': 10,
                    }"
                  ></line-chart>
                </v-card>
              </v-col>
              <v-col cols="12" sm="6">
                <v-card
                  class="mx-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n4"
                  color="teal"
                  dark
                >
                  <v-list-item three-line>
                    <v-list-item-content class="pa-2">
                      <v-list-item-title class="headline mb-1">
                        Heart rate <br />
                        <h2>112 bpm</h2>
                      </v-list-item-title>
                    </v-list-item-content>

                    <v-list-item-avatar tile size="150" class="pr-10">
                      <v-icon size="100">fas fa-heartbeat</v-icon>
                    </v-list-item-avatar>
                  </v-list-item>
                </v-card>
              </v-col>
              <v-col cols="12" sm="6">
                <v-card
                  class="mx-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n12"
                >
                  <v-app-bar color="rgba(0,0,0,0)" flat class="ma-8">
                    <h5>Your activity</h5>
                    <v-spacer></v-spacer>
                    <v-btn color="teal" rounded dark depressed>Week</v-btn>
                    <v-btn text>Mounth</v-btn>
                  </v-app-bar>
                  <v-progress-circular
                    rotate="360"
                    size="100"
                    width="15"
                    value="50"
                    color="teal"
                    class="mt-n5 ml-5 mb-2"
                  >
                    50
                  </v-progress-circular>
                  <v-progress-circular
                    rotate="360"
                    size="100"
                    width="15"
                    value="70"
                    color="red"
                    class="mt-n5 ml-2 mb-2"
                  >
                    70
                  </v-progress-circular>
                  <v-progress-circular
                    rotate="360"
                    size="100"
                    width="15"
                    value="80"
                    color="blue"
                    class="mt-n5 ml-2 mb-2"
                  >
                    80
                  </v-progress-circular>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-app>
      </v-flex>
      <v-flex md4>
        <v-app :style="{ background: $vuetify.theme.themes.light.background }">
          <v-container>
            <v-row>
              <v-col cols="12" md="3">
                <v-row>
                  <v-col cols="12" md="8">
                    <v-list two-line subheader class="ml-n8" style="background-color: inherit">
                      <v-list-item class="v-boder-left v-border-blue">
                        <v-list-item-content>
                          <v-list-item-subtitle>Car</v-list-item-subtitle>
                          <v-list-item-title>100</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12" md="3">
                <v-row>
                  <v-col cols="12" md="10">
                    <v-list two-line subheader class="ml-n8">
                      <v-list-item class="v-boder-left v-border-yellow">
                        <v-list-item-content>
                          <v-list-item-subtitle>Truck</v-list-item-subtitle>
                          <v-list-item-title>78</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12" md="3">
                <v-row>
                  <v-col cols="12" md="10">
                    <v-list two-line subheader class="ml-n8">
                      <v-list-item class="v-boder-left v-border-red">
                        <v-list-item-content>
                          <v-list-item-subtitle>Motobike</v-list-item-subtitle>
                          <v-list-item-title>120</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12" md="3">
                <v-row>
                  <v-col cols="12" md="10">
                    <v-list two-line subheader class="ml-n8">
                      <v-list-item class="v-boder-left v-border-pink">
                        <v-list-item-content>
                          <v-list-item-subtitle>Bus</v-list-item-subtitle>
                          <v-list-item-title>8</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12" sm="12">
                <v-list>
                  <v-list-item class="d-flex justify-content-between pl-0 pr-0">
                    <v-item-content
                      style="width: 30%"
                      v-for="item in list_time_analysis_choice"
                      :key="item.id"
                      class="item-analysis"
                    >
                      <v-btn
                        class="mr-3"
                        style="width: 100%"
                        :class="item.active ? 'btn-analysis-active' : ''"
                        @click="choiceTimeHandle(item.id)"
                        >{{ item.name }}</v-btn
                      >
                    </v-item-content>
                  </v-list-item>
                </v-list>
              </v-col>
              <v-col
                v-show="list_time_analysis_choice[0].active == true"
                cols="12"
                sm="12"
                class="mb-3"
              >
                <select
                  v-model="selected_month"
                  class="select-month text-center mr-4"
                  style="width: 40%"
                >
                  <option v-for="(month, index) in months" :key="index">
                    {{ month }}
                  </option>
                </select>
                <select
                  v-model="selected_year"
                  class="select-month text-center"
                  style="width: 20%"
                >
                  <option v-for="(year, index) in years" :key="index">
                    {{ year }}
                  </option>
                </select>
                <v-btn
                  class="ml-3"
                  style="background-color: #00897b; color: #fff"
                  >Request</v-btn
                >
              </v-col>
              <v-col
                cols="12"
                sm="12"
                class="mb-3"
                v-show="list_time_analysis_choice[1].active == true"
              >
                <v-card
                  class="mr-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n4"
                  color="teal lighten-5"
                  flat
                >
                  <date-picker
                    v-model="date"
                    :config="options"
                    @dp-change="onChange"
                    class="text-center"
                  ></date-picker>
                </v-card>
              </v-col>
              <v-col
                cols="12"
                sm="12"
                class="mb-3"
                v-show="list_time_analysis_choice[2].active == true"
              >
                <v-card
                  class="mr-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n4 d-flex justify-center"
                  flat
                >
                  <select
                  v-model="selected_year"
                  class="select-month text-center"
                  style="width: 50%"
                >
                  <option v-for="(year, index) in years" :key="index">
                    {{ year }}
                  </option>
                </select>
                </v-card>
              </v-col>
              <v-col cols="12" sm="12">
                <v-card
                  class="mr-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n4 py-4"
                  color="teal lighten-5"
                  flat
                >
                  <pie-chart
                    :data="[
                      ['Car', 44],
                      ['Motobike', 23],
                      ['Truck', 18],
                    ]"
                  ></pie-chart>
                </v-card>
              </v-col>
              <v-col cols="12" sm="12">
                <v-btn text
                  >Your Traitment
                  <v-icon right> mdi-chevron-down </v-icon>
                </v-btn>
              </v-col>
              <v-col cols="12" sm="12">
                <v-card
                  class="mr-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n4"
                  color="teal lighten-5"
                  flat
                >
                  <column-chart
                    :data="[
                      ['Sun', 32],
                      ['Mon', 46],
                      ['Tue', 28],
                      ['Web', 21],
                      ['Thu', 20],
                      ['Fri', 13],
                      ['Sat', 27],
                    ]"
                  ></column-chart>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-app>
      </v-flex>
    </v-layout>
  </v-app>
</template>
<script>
export default {
  name: "home",
  data: () => ({
    width: 2,
    radius: 10,
    padding: 8,
    lineCap: "round",
    value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
    fill: false,
    type: "trend",
    autoLineWidth: false,
    date: new Date(),
    options: {
      format: "DD/MM/YYYY",
      useCurrent: true,
    },
    list_time_analysis_choice: [
      {
        id: 0,
        name: "Month",
        active: true,
      },
      {
        id: 1,
        name: "Day",
        active: false,
      },
      {
        id: 2,
        name: "Year",
        active: false,
      },
    ],
    chartData: {
      "2017-05-13": 2,
      "2017-05-14": 3,
      "2017-05-15": 4,
    },
    months: [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ],
    years: ["2016", "2017", "2018", "2019", "2020", "2021", "2022"],
    selected_year: "2022",
    selected_month: "January",
    cameras: ["Camera 1", "Camera 2"],
    selected_camera: "Camera 1",
  }),
  computed: {
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
  },
  methods: {
    onChange() {
      alert(this.date);
    },
    choiceTimeHandle(id) {
      this.list_time_analysis_choice
        .filter((x) => x.id === id)
        .map((x) => (x.active = true));
      this.list_time_analysis_choice
        .filter((x) => x.id !== id)
        .map((x) => (x.active = false));
    },
  },
};
</script>
<style lang="scss" scoped>
date-picker {
  input {
    padding: 10px;
    text-align: center;
  }
}
.v-boder-left {
  border-left: 3px solid #00897b;
}
.v-boder-left.v-border-red {
   border-left: 3px solid red;
}
.v-boder-left.v-border-yellow {
  border-left: 3px solid rgb(251, 251, 170);
}
.v-boder-left.v-border-pink {
  border-left: 3px solid rgb(241, 184, 194);;
}
.v-boder-left.v-border-blue {
  border-left: 3px solid rgb(166, 166, 255);;
}
.item-analysis {
  button {
    background-color: #fff !important;
    outline: 1px solid #00897b;
  }
  button:hover {
    background-color: #00897b !important;
    color: #fff !important;
  }
  .btn-analysis-active {
    background-color: #00897b !important;
    color: #fff !important;
  }
}
#video-analysis {
  overflow: hidden;
  height: 500px;
  padding: 0px;
}
.calendar-date {
  border: 1px solid #00897b;
}
.select-month {
  padding: 10px;
  border: 2px solid #00897b;
  border-radius: 10px;
}
.select-month:focus-visible {
  border: 2px solid #00897b;
}
</style>
