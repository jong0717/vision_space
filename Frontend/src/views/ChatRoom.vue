<template>
  <div>
      <Message-List :msgs="msgDatas" class="msg-list"></Message-List>
      <Message-Form v-on:submitMessage="sendMessage" class="msg-form"></Message-Form>
  </div>
</template>

<script>
import {mapMutations, mapState} from 'vuex';
import MessageList from '@/components/Chat/MessageList.vue'
import MessageForm from '@/components/Chat/MessageForm.vue'
import Constant from '@/Constant'

export default {
    name :'ChatRoom',
    data() {
        return {
            datas: [],
        }
    },
    components: {
        MessageList,
        MessageForm,
    },
    computed: {
        ...mapState({
            'msgDatas': state => state.socket.msgDatas,
        }),
    },
    created() {
        const $ths = this;
        this.$socket.on('chat', (data) => {
            this.pushMsgData(data);
            $ths.datas.push(data);
        });
    },
    methods: {
        ...mapMutations({
            'pushMsgData': Constant.PUSH_MSG_DATA,
        }),
        sendMessage(msg) {
            this.pushMsgData({
                from: {
                    name: '나',
                },
                msg,
            });
            this.$sendMessage({
                name: this.$route.params.username,
                msg,
            });
        }
    }
}
</script>

<style scoped>
.msg-form {
  bottom: -28px;
  position: absolute;
  left: 0;
  right: 0;
}
.msg-list {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 60px;
  overflow-x: scroll;
}
</style>