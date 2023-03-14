/*!
* Start Bootstrap - Landing Page v6.0.5 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

const form = document.getElementById('contactForm');
const textbox = document.getElementById('input_tb');

// Add an event listener to the form submit event
form.addEventListener('submit', function(event) {
  // Prevent the default form submission behavior
  event.preventDefault();
  
  // Store the input value in a variable or cookie
  const inputValue = textbox.value;
  localStorage.setItem('myInput', inputValue);
  
  // Submit the form programmatically (optional)
  form.submit();
});

// Set the default value of the textbox to the stored value (if it exists)
const storedValue = localStorage.getItem('myInput');
if (storedValue) {
  textbox.value = storedValue;
}




