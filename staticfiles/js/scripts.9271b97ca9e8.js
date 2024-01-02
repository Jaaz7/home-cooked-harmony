$(document).ready(function () {
  var currentYear = new Date().getFullYear();
  $("#copyright").text(function (i, origText) {
    return origText + " " + currentYear;
  });
  CKEDITOR.replace("postBody");

  $(document).on("click", "#logout-link", function (e) {
    e.preventDefault();
    var form = this.form;
    $("#confirmLogoutModal").modal("show");
    $("#confirmLogout").on("click", function () {
      form.submit();
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
