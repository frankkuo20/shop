$(document).ready(function () {
  tinymce.init({
    selector: '.tinymceTextarea',
    setup: function (editor) {
      editor.on('change', function (e) {
        editor.save();
      });
    }
  });
});

