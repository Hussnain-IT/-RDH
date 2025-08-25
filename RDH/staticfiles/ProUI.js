document.addEventListener("DOMContentLoaded", function() {
  const searchForm = document.getElementById("property-search-form");
  
  if (searchForm) {
    searchForm.addEventListener("submit", function(event) {
      // Get form fields
      const minPrice = document.querySelector("[name='min_price']").value.trim();
      const maxPrice = document.querySelector("[name='max_price']").value.trim();
      const propertyType = document.querySelector("[name='property_type']").value;
      
      if (!minPrice && !maxPrice && !propertyType) {
        event.preventDefault();
      
        let messageElement = document.getElementById("search-message");
        if (!messageElement) {
          messageElement = document.createElement("div");
          messageElement.id = "search-message";
          messageElement.className = "alert alert-warning mt-3";
          searchForm.after(messageElement);
        }
        
        messageElement.textContent = "Please fill required credentials.";
        messageElement.style.display = "block";
      }
    });
    
    console.log("Search form validation initialized");
  } else {
    console.error("Search form not found on page");
  }

  const propertyBoxes = document.querySelectorAll(".box");
  console.log("Found " + propertyBoxes.length + " property boxes");

  propertyBoxes.forEach(box => {
    box.addEventListener("mouseenter", function() {
      this.style.transform = "scale(1.03)";
      this.style.transition = "transform 0.3s ease";
    });

    box.addEventListener("mouseleave", function() {
      this.style.transform = "scale(1)";
    });
  });
});
