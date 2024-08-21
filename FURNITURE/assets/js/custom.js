(function() {
	'use strict';

	var tinyslider = function() {
		var el = document.querySelectorAll('.testimonial-slider');

		if (el.length > 0) {
			var slider = tns({
				container: '.testimonial-slider',
				items: 1,
				axis: "horizontal",
				controlsContainer: "#testimonial-nav",
				swipeAngle: false,
				speed: 700,
				nav: true,
				controls: true,
				autoplay: true,
				autoplayHoverPause: true,
				autoplayTimeout: 3500,
				autoplayButtonOutput: false
			});
		}
	};
	tinyslider();

	


	var sitePlusMinus = function() {

		var value,
    		quantity = document.getElementsByClassName('quantity-container');

		function createBindings(quantityContainer) {
	      var product_quantity = quantityContainer.getElementsByClassName('product_quantity')[0];
	      var product_id = quantityContainer.getElementsByClassName('product_id')[0];
	      var increase = quantityContainer.getElementsByClassName('increase')[0];
	      var decrease = quantityContainer.getElementsByClassName('decrease')[0];
	      increase.addEventListener('click', function (e) { increaseValue(e,product_id, product_quantity); });
	      decrease.addEventListener('click', function (e) { decreaseValue(e,product_id, product_quantity); });
	    }

	    function init() {
	        for (var i = 0; i < quantity.length; i++ ) {
						createBindings(quantity[i]);
	        }
	    };

	    function increaseValue(event, product_id,product_quantity) {
	        value = parseInt(product_quantity.value, 10);
            product_id = parseInt(product_id);
            // var token = $ ('input[name = csrfmiddlewaretoken]').val();
	        console.log(product_quantity, product_quantity.value);

	        value = isNaN(value) ? 0 : value;
	        value++;
	        product_quantity.value = value;
            // $.ajax({
            //     method :"post",
            //     url : "/update_cart_item",
            //     data : {
            //       'product_id':product_id,
            //       'product_qty':value,
            //     //   csrfmiddlewaretoken: token
            //     },success : function(response){
            //       alertify.success(response.status)
            //     }
            //   });
            // $.ajax({
            //     type: 'POST',
            //     url: '/update_cart_item/',
            //     data: JSON.stringify({ 'name': 'John', 'age': 30 }),
            //     contentType: 'application/json',
            //     success: function(response) {
            //       console.log(response); // Handle the response from the view
            //     }
            //   });
           
           
	    }

	    function decreaseValue(event,product_id, product_quantity) {
	        value = parseInt(product_quantity.value, 10);

	        value = isNaN(value) ? 0 : value;
	        if (value > 0) value--;

	        product_quantity.value = value;
	    }
	    
	    init();
		
	};
	sitePlusMinus();


	
	
})()


$('.change_qauntity').click(function (e) {
	console.log("hhhh");
	e.preventDefault();
	var cart_id = $(this).closest(('.product_data')).find('.cart_id').val();
	var product_quantity = $(this).closest(('.product_data')).find('.product_quantity').val();
	var token = $('input[name = csrfmiddlewaretoken]').val();
	$.ajax({
		method :"POST",
		url : "/update_cart_item",
		data : {
		  'cart_id':cart_id,
		  'product_qty':product_quantity,
		  csrfmiddlewaretoken: token
		},success : function(response){
			console.log("asdsfdg");
			
		}
	  });
	
})


$('.removeItem').click('click', function () {
	var cart_id = $(this).closest(('.product_data')).find('.cart_id').val();
	var token = $('input[name = csrfmiddlewaretoken]').val();
	
    Swal.fire({
		title: "Are you sure?",
		icon: "warning",
		showCancelButton: true,
		confirmButtonColor: "#3085d6",
		cancelButtonColor: "#d33",
		confirmButtonText: "Yes, delete it!"
	}).then((result) => {
		if (result.isConfirmed) {
			
			$.ajax({
				method :"POST",
				url : "/remove_cart_item",
				data : {
					'cart_id':cart_id,
					csrfmiddlewaretoken: token
				},success : function(response){
					location.reload();
				}
			});
			
		 
		}
	  });
});

// document.getElementById('removeItem').addEventListener('click', function () {
// 	var product_id = $(this).closest(('.product_data')).find('.product_id').val();
// 	var token = $('input[name = csrfmiddlewaretoken]').val();
//     Swal.fire({
// 		title: "Are you sure?",
// 		icon: "warning",
// 		showCancelButton: true,
// 		confirmButtonColor: "#3085d6",
// 		cancelButtonColor: "#d33",
// 		confirmButtonText: "Yes, delete it!"
// 	  }).then((result) => {
// 		if (result.isConfirmed) {
		 
// 		  $.ajax({
// 			method :"POST",
// 			url : "/remove_cart_item",
// 			data : {
// 			  'product_id':product_id,
// 			  csrfmiddlewaretoken: token
// 			},success : function(response){
// 				location.reload();
// 			}
// 		  });

		 
// 		}
// 	  });
// });

// $('.try').click(function myFunction() {
// 	var token = $('input[name = csrfmiddlewaretoken]').val();

// });	
// $.ajax({
// 	method :"Get",
// 	url : "/remove_cart_item",
// 		data : {
// 		//   'product_id':product_id,
// 		  csrfmiddlewaretoken: token
// 		},success : function(response){
// 			location.reload();
// 		}
// });