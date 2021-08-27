<template>
    <div id="editor-root">
      <div id="editor" style="text-align: left"></div>
      <div v-html="content"></div>
      <button id="save" @click="save_content">保存</button>
    </div>
  </template>
  
  <script>
  import E from "wangeditor"
  export default {
    data(){
      return {
        content: "",
        editor: null
      }
    },
    mounted() {
      var _this = this
      var editor = new E('#editor');
      _this.editor = editor
      console.log(editor);
      _this.editor.config.uploadImgShowBase64 = true
      _this.editor.create();
    },
    methods: {
      save_content() {
        var _this=this;
        console.log(_this.content)
        _this.content=_this.editor.txt.html()
        console.log(_this.content)
      }
    }
    
  };
  </script>