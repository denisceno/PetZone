import flatpickr from "flatpickr";
import Swal from "sweetalert2";

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("order-form")
    .addEventListener("submit", function (event) {
      event.preventDefault(); // Stop form submission initially

      // Access the form field values dynamically
      const name = document.getElementById("id_name").value;
      const email = document.getElementById("id_email").value;
      const phone = document.getElementById("id_phone").value;

      // Show the confirmation dialog
      Swal.fire({
        title: "Confirm Appointment",
        html:
          "Ensure your information is correct before placing the order.<br>Name: " +
          name +
          "<br>Email: " +
          email +
          "<br>Phone: " +
          phone,
        icon: "info",
        showCancelButton: true,
        cancelButtonColor: "#d33",
        confirmButtonColor: "#3085d6",
        confirmButtonText: "Yes, place order!",
      }).then((result) => {
        if (result.isConfirmed) {
          // After confirmation, submit the form manually
          event.target.submit();
        }
      });
    });
});
