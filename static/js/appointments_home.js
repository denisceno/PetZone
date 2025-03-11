import flatpickr from "flatpickr";
import Swal from "sweetalert2";


document.addEventListener("DOMContentLoaded", function () {
  flatpickr("#appointment-date", {
    enableTime: true, // Enable time selection
    time_24hr: true, // Use 24-hour format
    minDate: "today", // Disable past dates
    minTime: "09:00", // Earliest appointment time
    maxTime: "17:00", // Latest appointment time
    dateFormat: "Y-m-d H:i", // Format compatible with Django
    defaultHour: 9, // Default start time
    defaultMinute: 0, // Default minute
    minuteIncrement: 20, // Minute step (30-minute intervals)
    inline: false, // Disable inline display of the calendar
    noCalendar: false, // Keep the calendar visible
    disableMobile: true, // Disable mobile-specific UI for consistency
  });
});

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("appointment-form")
    .addEventListener("submit", function (event) {
      event.preventDefault(); // Stop form submission

      // Access the form field value dynamically
      const name = document.getElementById("id_name").value; // Get the name value from the form
      const email = document.getElementById("id_email").value;
      const phone = document.getElementById("id_phone").value;

      // Show confirmation dialog
      Swal.fire({
        title: "Confirm Appointment",
        html:
          "Ensure your information is correct before scheduling the appointment.<br>Name: " +
          name +
          "<br>Email: " +
          email +
          "<br>Phone: " +
          phone,
        icon: "info",
        showCancelButton: true,
        cancelButtonColor: "#d33",
        confirmButtonColor: "#3085d6",
        confirmButtonText: "Yes, schedule it!",
      }).then((result) => {
        if (result.isConfirmed) {
          // Show success message before submitting the form
          Swal.fire({
            position: "center",
            icon: "success",
            title: "Your appointment has been scheduled successfully!",
            showConfirmButton: true, // Show the confirm button so it stays open
          });

          // Delay form submission so the success message is shown before submitting
          setTimeout(function () {
            event.target.submit(); // Submit the form after 1 second
          }, 3000); // Adjust the delay as needed (1000ms = 1 second)
        }
      });
    });
});
