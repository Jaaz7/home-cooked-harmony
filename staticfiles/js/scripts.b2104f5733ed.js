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

  $("#add_post_form").on("submit", function (e) {
    const title = $("#postTitle").val();
    const description = tinyMCE
      .get("postBody")
      .getContent({ format: "text" })
      .trim();

    if (
      !title ||
      title.length < 5 ||
      title.length > 100 ||
      !description ||
      description.length < 10 ||
      description.length > 5000
    ) {
      e.preventDefault();
      $("#validationModal").modal("show");
    }
  });

  $("#id_labels").select2({
    maximumSelectionLength: 6,
    templateSelection: function (data) {
      $(data.element).attr('data-select2-id', data.id);
      let $option = $(
        "<span>" +
          data.text +
          '</span class="remove-option" data-select2-id="' +
          data.id +
          '">'
      );
      return $option;
    },
  });

  $(document).on("click", ".remove-option", function (e) {
    e.preventDefault();
    e.stopPropagation();
    var id = $(this).data("select2-id");
    var option = $("#id_labels").find('option[data-select2-id="' + id + '"]');
    option.remove();
    $("#id_labels").trigger("change");
  });
});
