<template>
  <v-app :style="{ background: $vuetify.theme.themes.light.background }">
    <v-layout row>
      <v-flex md8>
        <v-app :style="{ background: $vuetify.theme.themes.dark.background }" class="rounded-tr-xl rounded-br-xl">
          <v-container>
            <v-row>
              <v-col cols="12" sm="12">
                <v-app-bar color="rgba(0,0,0,0)" flat class="mx-8 mb-8 mt-3">
                  <v-select :items="cameras" v-model="selected_camera" class="choice-camera mr-3" label="Choice camera"
                    dense>
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
                <v-card class="mx-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n15">
                  <v-list-item three-line id="video-analysis">
                    <img src="http://127.0.0.1:8000/video_feed/" class="w-100 h-100" alt="">
                  </v-list-item>
                </v-card>
              </v-col>
              <v-col cols="12" sm="12">
                <canvas id="myChart" width="400" height="200"></canvas>
              </v-col>
              <v-col cols="12" sm="12">
                <canvas id="myChartLine" width="400" height="200"></canvas>
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
                          <v-list-item-title>{{ task.car }}</v-list-item-title>
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
                          <v-list-item-title>{{ task.truck }}</v-list-item-title>
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
                          <v-list-item-title>{{ task.motorcycle }}</v-list-item-title>
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
                          <v-list-item-title>{{ task.bus }}</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12" sm="12">
                <v-list>
                  <v-list-item class="d-flex justify-content-between pl-0 pr-0">
                    <v-item-content style="width: 30%" v-for="item in list_time_analysis_choice" :key="item.id"
                      class="item-analysis">
                      <v-btn class="mr-3" style="width: 100%" :class="item.active ? 'btn-analysis-active' : ''"
                        @click="choiceTimeHandle(item.id)">{{ item.name }}</v-btn>
                    </v-item-content>
                  </v-list-item>
                </v-list>
              </v-col>
              <v-col v-show="list_time_analysis_choice[0].active == true" cols="12" sm="12" class="mb-3">
                <select v-model="selected_month" class="select-month text-center mr-4" style="width: 40%"
                  :items="months">
                  <!-- <option v-for="i in months.key">
                    {{ i.name }}
                  </option> -->
                </select>
                <select v-model="selected_year" class="select-month text-center" ref="selected_year" style="width: 20%">
                  <option v-for="(year, index) in years" :key="index">
                    {{ year }}
                  </option>
                </select>
                <v-btn class="ml-3" style="background-color: #00897b; color: #fff" @click="getTime()">Request</v-btn>
              </v-col>
              <v-col cols="12" sm="12" class="mb-3" v-show="list_time_analysis_choice[1].active == true">
                <v-card class="mr-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n4"
                  color="teal lighten-5" flat>
                  <date-picker v-model="date" :config="options" @dp-change="onChange" class="text-center"></date-picker>
                </v-card>
              </v-col>
              <v-col cols="12" sm="12" class="mb-3" v-show="list_time_analysis_choice[2].active == true">
                <v-card
                  class="mr-12 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-xl mt-n4 d-flex justify-center"
                  flat>
                  <select v-model="selected_year" class="select-month text-center" style="width: 50%">
                    <option v-for="(year, index) in years" :key="index">
                      {{ year }}
                    </option>
                  </select>
                </v-card>
              </v-col>
              
              <v-col cols="12" sm="12">
                <v-btn text>Your Traitment
                  <v-icon right> mdi-chevron-down </v-icon>
                </v-btn>
              </v-col>
              <v-col cols="12" sm="12">
                <canvas id="myChartDougnut" width="400" height="400"></canvas>
              </v-col>
            </v-row>
          </v-container>
        </v-app>
      </v-flex>
    </v-layout>
  </v-app>
</template>
<script src="https://cdn.jsdelivr.net/npm/chart.js@3.8.0/dist/chart.min.js"></script>
<script type="text/javascript" src="https://yourweb.com/inc/chart.utils.js"></script>
<script>

import axios from 'axios';

export default {
  name: "home",
  type: 'bar',
  d: new Date(),
  data: () => ({


    BE : [],
    day: (new Date()).getDate(),
    month: (new Date()).getMonth() + 1,
    year: (new Date()).getFullYear(),
    cam: 'Cam1',
    task: [],
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
      scales: {
        y: {
          beginAtZero: true
        }
      },
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
    months: {
      "January": "01",
      "February": "02",
      "March": "03",
      "April": "04",
      "May": "05",
      "June": "06",
      "July": "07",
      "August": "08",
      "September": "09",
      "October": "10",
      "November": "11",
      "December": "12"
    },
    days: {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0,
        "13": 0,
        "14": 0,
        "15": 0,
        "16": 0,
        "17": 0,
        "18": 0,
        "19": 0,
        "20": 0,
        "21": 20,
        "22": 30,
        "23": 50,
        "24": 30,
        "25": 40,
        "26": 70,
        "27": 50,
        "28": 110,
        "29": 0,
        "30": 0
    },
    selected_month: 'January',
    years: ["2016", "2017", "2018", "2019", "2020", "2021", "2022"],
    selected_year: "2022",
    cameras: ["Camera 1", "Camera 2"],
    selected_camera: "Camera 1",
  }),
  computed: {
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    }
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
    get_Tasks() {
      axios({
        method: 'get',
        url: "http://localhost:8000/vehicle?year=" + this.year + "&day=" + this.day + "&month=" + this.month + "&camera=" + this.cam,

      }).then(response => this.task = response.data);
    },
    getTime() {
      // this.$refs.selected_month.value, this.$refs.selected_year.value
      // console.log(this.month)
      // this.month = this.$refs.selected_month.value;
      // this.year = this.$refs.selected_year.value;
      alert(this.selected_month)
      alert(this.selected_year)
      axios({
        method: 'get',
        url: "http://localhost:8000/vehicle?year=" + this.selected_year + "&day=" + "&month=" + this.selected_month.number + "&camera=" + this.cam,

      }).then(response => this.task = response.data);
      console.log('task: ', this.task)
    }
  },
  mounted() {
    
    console.log(Object.keys(this.months))
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {

          labels: Object.keys(this.months),
          datasets: [{
              label: ['# of Votes','Tuan'],
              data: [12, 19, 3, 5, 10, 3,6,8,16,6,12,6],
              backgroundColor: [
                  'rgba(255, 0, 0, 0.2)',
                  'rgba(255, 127, 0, 0.2)',
                  'rgba(255, 255, 0, 0.2)',
                  'rgba(127, 255, 0, 0.2)',
                  'rgba(0, 255, 0, 0.2)',
                  'rgba(0, 255, 127, 0.2)',
                  'rgba(0, 255, 255, 0.2)',
                  'rgba(0, 127, 255, 0.2)',
                  'rgba(0, 0, 255, 0.2)',
                  'rgba(127, 0, 255, 0.2)',
                  'rgba(255, 0, 255, 0.2)',
                  'rgba(255, 0, 127, 0.2)',
              ],
              borderColor: [
                  'rgba(255, 0, 0, 1)',
                  'rgba(255, 127, 0, 1)',
                  'rgba(255, 255, 0, 1)',
                  'rgba(127, 255, 0, 1)',
                  'rgba(0, 255, 0, 1)',
                  'rgba(0, 255, 127, 1)',
                  'rgba(0, 255, 255, 1)',
                  'rgba(0, 127, 255, 1)',
                  'rgba(0, 0, 255, 1)',
                  'rgba(127, 0, 255, 1)',
                  'rgba(255, 0, 255, 1)',
                  'rgba(255, 0, 127, 1)',
                  
              ],
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
    });
    const data_lines = {
      labels: Object.keys(this.days),
      datasets: [{
        label: 'My First Dataset',
        data: Object.values(this.days),
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }]
    }
    const data_doughnut = {
      labels: [
        'Truck',
        'Bus',
        'Car',
        'Motorbike'
      ],
      datasets: [{
        label: 'My First Dataset',
        data: [300, 50, 100,45],
        backgroundColor: [
          'rgb(154, 156, 233)',
          'rgb(162, 185, 237)',
          'rgb(163, 220, 239)',
          'rgb(174, 238, 224)'
        ],
        hoverOffset: 4
      }]
    };
    console.log("Component")
    const ctxDougnut = document.getElementById('myChartDougnut').getContext('2d');
    const myChartDougnut = new Chart(ctxDougnut, {
        type: 'doughnut',
        data:data_doughnut,
    });
    const ctxLine = document.getElementById('myChartLine').getContext('2d');
    const myChartLine = new Chart(ctxLine, {
        type: 'line',
        data:data_lines,
    });
  }
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
  border-left: 3px solid rgb(241, 184, 194);
  ;
}

.v-boder-left.v-border-blue {
  border-left: 3px solid rgb(166, 166, 255);
  ;
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
