$(document).ready(function () {
	// Initial filter - show all products
	filterProducts();

	// Function to filter products based on category and subcategory parameters
	function filterProducts() {
	  var categoryParam = getParameterByName('category');
	  var subcategoryParam = getParameterByName('subcategory');

	  // Hide all product items
	  $(".product-item").hide();

	  if (categoryParam) {
		// Show products with the specified category
		$(".product-item[data-category='" + categoryParam + "']").show();
	  } else if (subcategoryParam) {
		// Show products with the specified subcategory
		$(".product-item[data-subcategory='" + subcategoryParam + "']").show();
	  } else {
		// Show all products if no category or subcategory is specified
		$(".product-item").show();
	  }
	}

	// Function to get parameter value from the URL
	function getParameterByName(name) {
	  var urlParams = new URLSearchParams(window.location.search);
	  return urlParams.get(name);
	}
  });
