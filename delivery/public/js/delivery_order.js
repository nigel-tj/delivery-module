frappe.ui.form.on('Delivery Order', {
  refresh: function(frm) {
      // Add the map view to the delivery order form
      frm.add_custom_button(__('View Map'), function() {
          // Create the map view
          var map = L.map('map').setView([51.505, -0.09], 13);

          // Add a tile layer to the map view
          L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
              attribution: 'Map data &copy; OpenStreetMap contributors'
          }).addTo(map);

          // Add the driver marker to the map view
          var driverMarker = L.marker([51.5, -0.09]).addTo(map);

          // Add the delivery destination marker to the map view
          var destinationMarker = L.marker([51.51, -0.1]).addTo(map);

          // Update the driver marker in real-time
          setInterval(function() {
              // Get the driver's location from your Frappe app
              frappe.call({
                  method: "delivery.delivery.doctype.delivery_order.delivery_order.get_driver_location",
                  args: {
                      driver: frm.doc.delivery_driver
                  },
                  callback: function(response) {
                      var driverLocation = response.message;
                      if (driverLocation) {
                          // Update the driver marker on the map view
                          driverMarker.setLatLng(driverLocation);
                      }
                  }
              });
          }, 1000);
      }).appendTo(frm.dashboard.wrapper);
  }
});
