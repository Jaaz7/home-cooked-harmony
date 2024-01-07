$(document).ready(function () {
  // Update the copyright year dynamically
  const currentYear = new Date().getFullYear();
  $("#copyright").text(function (i, origText) {
    return origText + " " + currentYear;
  });

  // Initialize TinyMCE rich text editor
  tinymce.init({
    selector: "#postBody",
    plugins:
      "mentions anchor autolink charmap codesample emoticons link lists visualblocks wordcount checklist casechange formatpainter permanentpen footnotes advtemplate advcode powerpaste tinymcespellchecker autocorrect a11ychecker typography inlinecss",
    toolbar:
      "undo redo | formatselect | bold italic underline strikethrough | link | align | checklist numlist bullist indent outdent | emoticons charmap | removeformat",
  });

  // Handle logout link click with confirmation modal
  $(document).on("click", "#logout-link", function (e) {
    e.preventDefault();
    const logoutUrl = this.href;
    $("#confirmLogoutModal").modal("show");
    $("#confirmLogout").on("click", function () {
      window.location.href = logoutUrl;
    });
  });

  // Confirmation modal for post deletion
  $(document).on("click", "#delete-button", function (e) {
    e.preventDefault();
    const form = this.form;
    $("#confirmDeletePostModal").modal("show");
    $("#confirmDeletePost").on("click", function () {
      form.submit();
    });
  });

  // Form validation for adding a new post
  $("#add_post_form").on("submit", function (e) {
    const title = $("#postTitle").val();
    const description = tinyMCE
      .get("postBody")
      .getContent({ format: "text" })
      .trim();

    // Check conditions for title and description length
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

  // Dynamically adjust body margin-top
  // adding 30px to the height of the navbar
  const headerHeight = $(".navbar").outerHeight();
  const marginTop = (headerHeight + 30) + "px";
  $(".main").css("margin-top", marginTop);

  // Adjust body margin-top when navbar is shown
  $("#navbarSupportedContent").on("shown.bs.collapse", function () {
    const headerHeight = $(".navbar").outerHeight();
    $(".main").css("margin-top", headerHeight + 30 + "px");
  });

  // Reset body margin-top when navbar is hidden
  $("#navbarSupportedContent").on("hidden.bs.collapse", function () {
    $(".main").css("margin-top", (headerHeight + 30) + "px");
  });
});
