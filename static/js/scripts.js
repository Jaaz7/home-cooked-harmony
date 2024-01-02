$(document).ready(function () {
  var currentYear = new Date().getFullYear();
  $("#copyright").text(function (i, origText) {
    return origText + " " + currentYear;
  });
  CKEDITOR.replace("postBody");

  $(document).on("click", "#logout-link", function (e) {
    if (!window.confirm("Are you sure you want to logout?")) {
      e.preventDefault();
    }
  });
});
