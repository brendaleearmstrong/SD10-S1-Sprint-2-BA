
// Function to return a string describing the wedding details
function getWeddingDetailsString(weddingData) {
    return `Wedding Theme: ${weddingData.weddingDetails.theme}<br>
    Venue: ${weddingData.weddingDetails.venue}<br>
    Location: ${weddingData.weddingDetails.location}<br>
    Date: ${weddingData.weddingDetails.date}<br>
    Budget: $${weddingData.weddingDetails.budget}`;
  }
  
  // Function to return a string describing the checklist items
  function getChecklistString(weddingData) {
    let checklistString = '';
    weddingData.checklistItems.forEach(category => {
      checklistString += `<h3>${category.category}</h3>`;
      category.items.forEach(item => {
        checklistString += `${item}<br>`;
      });
    });
    return checklistString;
  }
  
  // Call the fetch function to read the JSON file
  fetch('data.json')
    .then(response => {
      return response.json();
    })
    .then(data => {
      console.log(data); // Display the JSON data in the browser console
      // Call the functions to process and display the JSON data
      document.getElementById('weddingDetails').innerHTML = getWeddingDetailsString(data);
      document.getElementById('checklist').innerHTML = getChecklistString(data);
    })
    .catch(error => {
      console.log('Error reading the JSON file', error);
    });