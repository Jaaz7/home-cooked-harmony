$(document).ready(function () {
  var currentYear = new Date().getFullYear();
  $("#copyright").text(function (i, origText) {
    return origText + " " + currentYear;
  });
  tinymce.init({
    selector: "textarea",
    plugins:
      "mentions anchor autolink charmap codesample emoticons link lists visualblocks wordcount checklist mediaembed casechange export formatpainter pageembed permanentpen footnotes advtemplate advtable advcode editimage tableofcontents mergetags powerpaste tinymcespellchecker autocorrect a11ychecker typography inlinecss",
    toolbar:
      "undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat",
  });

  $(document).on("click", "#logout-link", function (e) {
    e.preventDefault();
    var logoutUrl = this.href;
    $("#confirmLogoutModal").modal("show");
    $("#confirmLogout").on("click", function () {
      window.location.href = logoutUrl;
    });
  });

  $(document).on("click", "#delete-button", function (e) {
    e.preventDefault();
    var form = this.form;
    $("#confirmDeletePostModal").modal("show");
    $("#confirmDeletePost").on("click", function () {
      form.submit();
    });
  });
});
