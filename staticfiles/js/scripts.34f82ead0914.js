$(document).ready(function () {
  const currentYear = new Date().getFullYear();
  $("#copyright").text(function (i, origText) {
    return origText + " " + currentYear;
  });
  tinymce.init({
    selector: "#postBody",
    plugins:
      "mentions anchor autolink charmap codesample emoticons link lists visualblocks wordcount checklist casechange formatpainter permanentpen footnotes advtemplate advcode powerpaste tinymcespellchecker autocorrect a11ychecker typography inlinecss",
    toolbar:
      "undo redo | formatselect | bold italic underline strikethrough | link | align | checklist numlist bullist indent outdent | emoticons charmap | removeformat",
  });

  $(document).on("click", "#logout-link", function (e) {
    e.preventDefault();
    const logoutUrl = this.href;
    $("#confirmLogoutModal").modal("show");
    $("#confirmLogout").on("click", function () {
      window.location.href = logoutUrl;
    });
  });

  $(document).on("click", "#delete-button", function (e) {
    e.preventDefault();
    const form = this.form;
    $("#confirmDeletePostModal").modal("show");
    $("#confirmDeletePost").on("click", function () {
      form.submit();
    });
  });

  $(document).ready(function() {
    $('#add_post_form').on('submit', function(e) {
      const title = $('#postTitle').val();
      const description = $('#postBody').val();
  
      if (!title || !description) {
        e.preventDefault();
        $('#validationModal').modal('show');
      }
    });
  });

  $('#add_post_form').on('submit', function(e) {
    const description = $('#postBody').val();
    if (!description.trim()) {
        e.preventDefault();
        alert('Description cannot be empty.');
        return false;
    }
});
});
