<template>
  <div class="msgList chat_window">
    <div v-for="(msg,index) in msgs" :key="index" >
        <span style="color:white;" v-if="(msg.name != $store.state.uid.username) && (msg.name != 'system')">{{ msg.name }}</span>
        <p v-if="msg.name == $store.state.uid.username" style="text-align:right;margin:0;color:white;">나</p>
        <div class="content" :class="{ me : msg.name == $store.state.uid.username, system : msg.name == 'system'}">
            {{ msg.message }}
        </div>
    </div>
  </div>
</template>

<script>


export default {
    name: 'MessageList',
    props:['msgs'],
    watch: {
        msgs() {
            // alert('asdf')

            // console.log(msgList.scrollHeight)
        }
    },

    updated() {
        let msgList = document.querySelector('.msgList');
        msgList.scrollTop = msgList.scrollHeight
    }
};
</script>

<style scoped>
.list-item {
    display: inline-block;
    margin-right:10px;
}
.list-enter-active, .list-leave-active {
    transition: all ls;
}
.list-enter, .list-leave-to {
    opacity: 0;
    transform: translateX(30px);
}
.msgList {
    padding: 10px;
    overflow-y: scroll;
    height: 100%;
    /* font-family: 'Nanum Pen Script', cursive; */
    font-family: 'HangeulNuri-Bold';
}
.content {
    border-radius: 0px 15px 15px 15px;
    background: white;
    padding: 10px 10px 10px 10px;
    margin-right: auto;
    width: 80%;
    white-space:normal;
    font-size: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.msgList::-webkit-scrollbar{
    width: 0.25rem;
}

.msgList::-webkit-scrollbar-track{
    background: #ffffff;
}

.msgList::-webkit-scrollbar-thumb{
    background: #FFF5D0;
}

.me {
    /* background: rgb(230, 230, 117); */
    background:#EBE7D9;
    border-radius: 15px 0px 15px 15px;
    margin: 0 0 0 auto;
}
.system {
    border-radius: 5px;
    width: 100%;
    height: 40px;
    padding: 5px;
    margin-top: 10px;
    background: pink;
}
</style>