<template>
  <div>
    <div class="remocon">
      <div id="dot1" class="dotcase active" @click="scrollMoveTop">
        <div class="toTop" style="color:white;" >TOP</div>
      </div>
      <div id="dot2" class="dotcase" @click="scrollMoveToID('description1')">
        <div class="dot"></div>
      </div>
      <div id="dot3" class="dotcase" @click="scrollMoveToID('description2')">
        <div class="dot"></div>
      </div>
      <div id="dot4" class="dotcase" @click="scrollMoveToID('description3')">
        <div class="dot"></div>
      </div>
      <div id="dot5" class="dotcase" @click="scrollMoveToID('description4')">
        <div class="dot"></div>
      </div>
      <div id="dot6" class="dotcase" @click="scrollMoveToID('description5')">
        <div class="dot"></div>
      </div>
      
    </div>
    <div id="con">
      <div class="mycontent">
          <div class="title-container">
            
            <h1 class="mytitle stagger-item">VISION SPACE</h1>

              <div class="bird-container bird-container--one">
                <div class="bird bird--one"></div>
              </div>
              
              <div class="bird-container bird-container--two">
                <div class="bird bird--two"></div>
              </div>
              
              <div class="bird-container bird-container--three">
                <div class="bird bird--three"></div>
              </div>
              
              <div class="bird-container bird-container--four">
                <div class="bird bird--four"></div>
              </div>
            
            <svg class="pulse" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                  <circle id="Oval" cx="512" cy="512" r="512"></circle>
                  <circle id="Oval" cx="512" cy="512" r="512"></circle>
              <circle id="Oval" cx="512" cy="512" r="512"></circle>
           </svg>
            
          </div>
          <!-- <input placeholder="코드를 입력해주세요" v-model="boardCode" class="roomCodeInput">
          <a @click="toBoard">보드 참가</a>
          <p @click="$router.push({name:'SignupForm'})">계정이 없으신가요? 비전 스페이스는 간편하게 가입하여 이용가능합니다.</p> -->
      </div>
    </div>
    <div style="width:100%;">
      <div>
        <p class="center-text" style="font-size: 20px;font-weight:bold; padding-top:20px;color:#ed6274;">
          <v-icon class="jump" style="font-size:22px;transform:rotate(180deg);color:#495464;" @click="scrollMoveToID('description1')">mdi-triangle</v-icon>
        </p>
      </div>
      <v-row class="description" id="description1">
        <v-col class="des1col" cols="12" style="display:flex;align-items:center;flex-direction:column;height:100%"
          ><h2 class="mt-10 mb-5 introduce3 des1title">
            Vision Space는?
          </h2>
          <h2 class="mb-5 introduce2">
            Vision Space는 코르크 보드를 모티브로 하여 자신의 아이디어를 노트에 적어 보드 위에 자유롭게 배치하고, 이를 실시간으로
            공유할 수 있는 화상 회의 플랫폼입니다.
          </h2>
          <h2 class="mb-5 introduce2">
            Vision Space에서 서로의 비전을 공유하세요.
          </h2>
          <img style="height:300px;" src="../assets/Home/1.png">
        </v-col>
      </v-row>
      <v-row class="description"  id="description2">
        <v-col cols="6" 
          >
          <div style="display:flex;justify-content:center;">
          <img style="width:450px;" src="@/assets/Home/2.gif" alt="" class="mt-10 mmain" />
          </div>
        </v-col>
        <v-col cols="6" class="des2col" 
          ><h2 class="mt-10 mb-5 introduce3">
            링크 공유를 통한 멤버 초대
          </h2>
          <h2 class="mb-5 introduce2" style="width:100%;">
            보드 이름을 클릭하면 보드의 주소가 복사됩니다.
          </h2>
          <h2 class="mb-5 introduce2" style="width:100%;">
            초대하고 싶은 멤버에게 이를 공유하여 간편하게 초대하세요.
          </h2>
        </v-col>
      </v-row>
      <v-row class="description"  id="description3">
        <v-col cols="6" class="des3col"
          ><h2 class="mt-10 mb-5 introduce3">
            탭 추가 및 전환 기능
          </h2>
          <h2 class="mb-5 introduce2" style="width:100%;">
            탭을 전환하여 각 탭에 다른 노트를 담을 수 있습니다.
          </h2>
          <h2 class="mb-5 introduce2" style="width:100%;">
            탭 기능을 통해 보드를 더욱 다채롭게 활용해 보세요.
          </h2>          
        </v-col>
        <v-col cols="6"
          >
          <div style="display:flex;justify-content:center;">
            <img src="@/assets/Home/3.png" alt="" class="mt-10 mmain" />
          </div>
        </v-col>
      </v-row>
      <v-row class="description"  id="description4">
        <v-col cols="6"
          >
          <div style="display:flex;justify-content:center;">
            <img style="height:450px;" src="@/assets/Home/4.png" alt="" class="mt-10 mmain" />
          </div>
        </v-col>
        <v-col cols="6" class="des4col"
          ><h2 class="mt-10 mb-5 introduce3">
            채팅을 통한 소통
          </h2>
          <h2 class="mb-5 introduce2">
            마이크를 사용할 수 없는 상황이라면 
            채팅을 통해 대화하세요.
          </h2>
        </v-col>
      </v-row>
      <v-row class="description"  id="description5">
        <v-col cols="12" class="des5col" style="display:flex;align-items:center;flex-direction:column;"
          ><h2 class="mt-10 mb-5 introduce3 text-center">
            Team Members
          </h2>
          <div style="display:flex;align-items:center;flex-direction:row;width:100%;justify-content:space-around;margin-top:5%;">
            <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;width:10%;"><img style="width:80%;margin-bottom: 20px;" src="@/assets/members/장종하.jpg"><p style="text-align:center;">장종하</p></div>
            <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;width:10%;"><img style="width:80%;margin-bottom: 20px;" src="@/assets/members/김시영.jpg"><p style="text-align:center;">김시영</p></div>
            <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;width:10%;"><img style="width:80%;margin-bottom: 20px;" src="@/assets/members/안재완.jpg"><p style="text-align:center;">안재완</p></div>
            <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;width:10%;"><img style="width:80%;margin-bottom: 20px;" src="@/assets/members/최재혁.jpg"><p style="text-align:center;">최재혁</p></div>
            <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;width:10%;"><img style="width:80%;margin-bottom: 20px;" src="@/assets/members/홍순종.jpg"><p style="text-align:center;">홍순종</p></div>
          </div>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import cookies from "vue-cookies";

export default {
  data() {
    return {
      boardCode: "",
    };
  },
  methods: {
    scrollMoveTop() {
      window.scrollTo({top:0, left:0, behavior:'smooth'});
    },
    scrollMoveToID(id){
      let location = document.querySelector('#' + id).offsetTop;
      window.scrollTo({top:location, behavior:'smooth'});
    },
    toBoard() {
      if (this.boardCode == '') {
        alert('코드를 입력해주세요')
        return;
      }
      this.fetchRoomInfo();
    },
    fetchRoomInfo() {
      let config = {
        headers: {
          Authorization: "Bearer " + cookies.get("auth-token"),
        },
      };
      axios
        .get(SERVER.URL + "/api/v1/board/" + this.boardCode + "/", config)
        .then((res) => {
          // console.log('@@@@@@@@')
          // console.log(res.data);
          this.$router.push({
            name: "board",
            params: { code: this.boardCode },
          });
          this.host = res.data.admin_username;
          this.roomName = res.data.name;
        })
        .catch(() => {
          this.$router.push({ name: "NoBoardFound" });
          console.log('err');
        });
    },
  },
  mounted() {
    let dot1 = document.querySelector("#dot1");
    let dot2 = document.querySelector("#dot2");
    let dot3 = document.querySelector("#dot3");
    let dot4 = document.querySelector("#dot4");
    let dot5 = document.querySelector("#dot5");
    let dot6 = document.querySelector("#dot6");
    let des1 = document.querySelector("#description1");
    let des2 = document.querySelector("#description2");
    let des3 = document.querySelector("#description3");
    let des4 = document.querySelector("#description4");
    let des5 = document.querySelector("#description5");
    let des1col = document.querySelector(".des1col");
    let des2col = document.querySelector(".des2col");
    let des3col = document.querySelector(".des3col");
    let des4col = document.querySelector(".des4col");
    let des5col = document.querySelector(".des5col");
    let des1location = des1.offsetTop;
    let des2location = des2.offsetTop;
    let des3location = des3.offsetTop;
    let des4location = des4.offsetTop;
    let des5location = des5.offsetTop;

    window.addEventListener("scroll", () => {
      dot1.classList.toggle("active", des1location/2 > window.scrollY);
      dot2.classList.toggle("active", (des2location + des1location)/2 > window.scrollY && window.scrollY > des1location/2);
      des1col.classList.toggle("down", (des2location + des1location)/2 > window.scrollY && window.scrollY > des1location/2);
      dot3.classList.toggle("active", (des3location + des2location)/2 > window.scrollY && window.scrollY > (des2location + des1location)/2);
      des2col.classList.toggle("right", (des3location + des2location)/2 > window.scrollY && window.scrollY > (des2location + des1location)/2);
      dot4.classList.toggle("active", (des4location + des3location)/2 > window.scrollY && window.scrollY > (des3location + des2location)/2);
      des3col.classList.toggle("left", (des4location + des3location)/2 > window.scrollY && window.scrollY > (des3location + des2location)/2);
      dot5.classList.toggle("active", (des5location + des4location)/2 > window.scrollY && window.scrollY > (des4location + des3location)/2);
      des4col.classList.toggle("right", (des5location + des4location)/2 > window.scrollY && window.scrollY > (des4location + des3location)/2);
      dot6.classList.toggle("active", window.scrollY > (des5location + des4location)/2);
      des5col.classList.toggle("down", window.scrollY > (des5location + des4location)/2);
    })
  }
};
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&display=swap');

* {

}

#con{
    /* position: absolute; */
    /* top: 5%;
    left: 5%;
    right: 5%;
    bottom: 5%; */
    width: 100%;
    height: calc(100vh - 90px);
    display: flex;
    justify-content: center;
    align-items: center;
    background: url('../assets/space.jpg') #151729 no-repeat;
    background-size: cover;
    box-shadow: 0 15px 30px rgba(0, 0, 0, .5);
    z-index: 10000;
    background-repeat: no-repeat;
    background-size: cover;
}

.left {
  float: left;
}
.introduce {
  font-size: 48px;
  font-weight: 400;
  letter-spacing: -0.5px;
  line-height: 56px;
}
.introduce2 {
  color: #313131;
  font-size: 20px;
  font-weight: 400;
  letter-spacing: initial;
  line-height: 28px;
  width: 50%;
}
.codeinput {
  /* padding: 0; */
}
.main {
  max-width: 100%;
  height: auto;
}
hr {
  border: solid #dadce0;
  border-width: 1px 0 0;
  clear: both;
  height: 0;
  margin-bottom: 19px;
}
.router-link {
  text-decoration: none;
}
.introduce3 {
  font-size: 36px;
  font-weight: 400;
  letter-spacing: -0.25px;
  line-height: 44px;
}
.center-text {
  text-align: center;
}
.time {
  text-align: center;
}
.home-btn {
  width: 80px;
  height: 80px !important;
  padding: 0px !important;
}
.material-icons {
  font-size: 40px !important;
}
#con .mycontent{
    width: 100%;
    height: 100%;
    text-align: center;
}
#con .mycontent h2{
    font-size: 60px;
    color: #fff;
    line-height: 1em;
    margin-bottom: 20px;
}
#con .mycontent h4{
    position: relative;
    font-size: 1.5em;
    margin-bottom: 20px;
    color: #111;
    background: #fff;
    font-weight: 300;
    padding: 10px 20px;
    display: inline-block;
}
#con .mycontent p{
    color: #fff;
    font-size: 1em;
    margin-top: 40px;
    cursor: pointer;
    
}
#con .mycontent p:hover{
  text-decoration: underline;
}
#con .mycontent a{
    position: relative;
    display: block;
    padding: 10px 25px;
    background: #ff0562;
    color: #fff;
    text-decoration: none;
    margin-top: 25px;
    border-radius: 25px;
    border-bottom: 4px solid #d00d56;
    margin-left: auto;
    margin-right: auto;
    width: 180px;
}
.roomCodeInput {
    position: relative;
    font-size: 1.5em;
    margin-bottom: 20px;
    color: #111;
    background: #fff;
    font-weight: 300;
    padding: 10px 20px;
    display: inline-block;
    outline: none;
}
 @import url('https://fonts.googleapis.com/css?family=Lobster+Two');

.mytitle {
	// font-family: 'Lobster Two', cursive;
	font-size: 5rem;
	text-shadow: 0px 1px 0px rgba(255, 255, 255, 1);
	color: rgb(255, 255, 255);
}

.title-container {
	position: relative;
	z-index: 0;
	display: flex;
	align-items: center;
	justify-content: center;
	height: 100%;
	overflow: hidden;
  // margin-top: 220px;
}
h2, p {
  font-family: 'Nanum Myeongjo', serif;
}
.pulse {
	z-index: -1;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	min-width: 30rem;
	
	circle {
		fill: #ffffff;
		transform: scale(0);
		opacity: 0;
		transform-origin: 50% 50%;
		animation: pulse 2s cubic-bezier(.5,.5,0,1) infinite;
		
		&:nth-child(2) {
			fill: white;
			animation: pulse 2s 0.75s cubic-bezier(.5,.5,0,1) infinite;
		}
		
		&:nth-child(3) {
			fill: white;
			animation: pulse 2s 1.5s cubic-bezier(.5,.5,0,1);
		}
		
	}
	
}

@keyframes pulse {
	
	25% {
		opacity: 0.4;
	}
	
	100% {
		transform: scale(1);
	}
	
}

@keyframes showItem {
  from {
    // transform: translateY(50px);
    opacity: 0;
    // color: aqua;
  }

  to {
    transform: translateY(0px);
    opacity: 1;
  }
}

.down {
  animation: showItemDown 1s !important;
}
.right {
  animation: showItemRight 1s !important;
}
.left {
  animation: showItemLeft 1s !important;
}

@keyframes showItemDown {
  from {
    transform: translateY(50px);
    opacity: 0;
    // color: aqua;
  }

  to {
    transform: translateY(0px);
    opacity: 1;
  }
}

@keyframes showItemRight {
  from {
    transform: translateX(100px);
    opacity: 0;
    // color: aqua;
  }
  to {
    transform: translateY(0px);
    opacity: 1;
  }
}

@keyframes showItemLeft {
  from {
    transform: translateX(-100px);
    opacity: 0;
    // color: aqua;
  }
  to {
    transform: translateY(0px);
    opacity: 1;
  }
}
.stagger-item {
  animation: showItem 5s;
  animation-fill-mode: both;
}

@import url('https://fonts.googleapis.com/css?family=Arima+Madurai:300');

*,
*::before,
*::after {
	box-sizing: border-box;
}

h1 {
	// font-family: 'Arima Madurai', cursive;
	color: black;
	font-size: 4rem;
	letter-spacing: -3px;
	text-shadow: 0px 1px 1px rgba(255,255,255,0.6);
	position: relative;
	z-index: 3;
}

.title-container {
	z-index: 1;
	position: relative;
	overflow: hidden;
	display: flex;
	align-items: center;
	justify-content: center;
	// min-height: 100vh;
	min-height: 35rem;
	// background-image: linear-gradient(to bottom,  rgba(255,168,76,0.6) 0%,rgba(255,123,13,0.6) 100%), url('https://images.unsplash.com/photo-1446824505046-e43605ffb17f');
	background-blend-mode: soft-light;
	background-size: cover;
	background-position: center center;
	padding: 2rem;
  width: 100%;
}

.bird {
	background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/174479/bird-cells-new.svg);
	background-size: auto 100%;
	width: 88px;
	height: 125px;
	will-change: background-position;
	
	animation-name: fly-cycle;
	animation-timing-function: steps(10);
	animation-iteration-count: infinite;

	&--one {
		animation-duration: 1s;
		animation-delay: -0.5s;		
	}
	
	&--two {
		animation-duration: 0.9s;
		animation-delay: -0.75s;
	}
	
	&--three {
		animation-duration: 1.25s;
		animation-delay: -0.25s;
	}
	
	&--four {
		animation-duration: 1.1s;
		animation-delay: -0.5s;
	}

}

.bird-container {
	position: absolute;
	top: 20%;
	left: -10%;
	transform: scale(0) translateX(-10vw);
	will-change: transform;
	
	animation-name: fly-right-one;
	animation-timing-function: linear;
	animation-iteration-count: infinite;
	
	&--one {
		animation-duration: 15s;
		animation-delay: 0;
	}
	
	&--two {
		animation-duration: 16s;
		animation-delay: 1s;
	}
	
	&--three {
		animation-duration: 14.6s;
		animation-delay: 9.5s;
	}
	
	&--four {
		animation-duration: 16s;
		animation-delay: 10.25s;
	}
	
}

@keyframes fly-cycle {
	
	100% {
		background-position: -900px 0;
	}
	
}

@keyframes fly-right-one {
	
	0% {
		transform: scale(0.3) translateX(-10vw);
	}
	
	10% {
		transform: translateY(2vh) translateX(10vw) scale(0.4);
	}
	
	20% {
		transform: translateY(0vh) translateX(30vw) scale(0.5);
	}
	
	30% {
		transform: translateY(4vh) translateX(50vw) scale(0.6);
	}
	
	40% {
		transform: translateY(2vh) translateX(70vw) scale(0.6);
	}
	
	50% {
		transform: translateY(0vh) translateX(90vw) scale(0.6);
	}
	
	60% {
		transform: translateY(0vh) translateX(110vw) scale(0.6);
	}
	
	100% {
		transform: translateY(0vh) translateX(110vw) scale(0.6);
	}
	
}

@keyframes fly-right-two {
	
	0% {
		transform: translateY(-2vh) translateX(-10vw) scale(0.5);
	}
	
	10% {
		transform: translateY(0vh) translateX(10vw) scale(0.4);
	}
	
	20% {
		transform: translateY(-4vh) translateX(30vw) scale(0.6);
	}
	
	30% {
		transform: translateY(1vh) translateX(50vw) scale(0.45);
	}
	
	40% {
		transform: translateY(-2.5vh) translateX(70vw) scale(0.5);
	}
	
	50% {
		transform: translateY(0vh) translateX(90vw) scale(0.45);
	}
	
	51% {
		transform: translateY(0vh) translateX(110vw) scale(0.45);
	}
	
	100% {
		transform: translateY(0vh) translateX(110vw) scale(0.45);
	}
}

.description{
  padding: 100px;
  height: 100vh;
}

#description1,
#description3,
#description5 {
  background: #eeeeee;
}

.description h2:first-child:after{
    display: block;
    content: "";
    height: 2px;
    width: 200px;
    margin: 7px 20px 10px;
}

#description1 h2:first-child:after{
  background: #dfa767;
  margin: 7px auto 10px;
}
#description2 h2:first-child:after{
  background:#5d7de4;
}
#description3 h2:first-child:after{
  background:#dc93df;
}
#description4 h2:first-child:after{
  background:#a3df91;
}
#description5 h2:first-child:after{
  background:#9f8dec;
}
.remocon {
  position: fixed;
  height: 200px;
  width: 50px;
  border-radius: 45px;
  background: rgba(0,0,0,.2);
  transform: translateY(-50%);
  top: 50%;
  right: 40px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  z-index: 50000;
  padding: 20px 0 20px;
}
.dotcase {
  height: 20px;
  width: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.dot {
  height: 5px;
  width: 5px;
  border-radius: 50%;
  background: white;
}
.dotcase:hover .dot
{
  height: 10px;
  width: 10px;
}
.active .dot {
  height: 10px;
  width: 10px;
  background: rgb(0, 183, 255);
  border: 2px white solid;
}
.active .toTop {
  color:rgb(0, 183, 255) !important;
//  text-shadow: -1px 0 #F2F1F6, 0 1px #F2F1F6, 1px 0 #F2F1F6, 0 -1px #F2F1F6;
text-shadow: 1px 1px 0px #000000;
}

@keyframes jump {	
	0% {
		transform: translateY(-5px) rotate(180deg);
	}
  25% {
    transform: translateY(5px) rotate(180deg);
  }
  50% {
    transform: translateY(-5px) rotate(180deg);
  }
  75% {
    transform: translateY(5px) rotate(180deg);
  }
	100% {
		transform: translateY(-5px) rotate(180deg);
	}
}

.jump {
  animation: jump 2s infinite;
}
</style>
