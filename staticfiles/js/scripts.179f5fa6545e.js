$(document).ready(function () {
  var currentYear = new Date().getFullYear();
  $("#copyright").text(function (i, origText) {
    return origText + " " + currentYear;
  });
  CKEDITOR.replace("postBody");

  $('#logout-link').click(function (e) {
    if (!confirm('Are you sure you want to logout?')) {
      e.preventDefault();
    }
  })
});
