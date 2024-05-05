<script>
  $(document).keydown(function(e) {
    if (e.ctrlKey) {
      // Check for Ctrl key shortcuts
      switch (e.altKey) {
        
      }
    } else if (e.altKey) {
      // Check for Alt key shortcuts
      switch (e.keyCode) {
        case 65:
          // Redirect to "add_city" when Alt + A is pressed
          window.location.href = "/masters/main_masters/city_master/add_city";
          break;
          case 71:
          // Redirect to "view_city_grid" when Ctrl + G is pressed
          window.location.href = "/masters/main_masters/city_master/view_city_grid";
          break;
        case 77:
          // Redirect to "view_city" when Ctrl + M is pressed
          window.location.href = "/masters/main_masters/city_master/view_city";
          break;
        case 88:
          // Redirect to "export-cities-to-excel" when Ctrl + X is pressed
          window.location.href = "/masters/main_masters/city_master/export-cities-to-excel";
          break;
        case 80:
          // Redirect to "export_city_pdf" when Ctrl + P is pressed
          window.location.href = "/masters/main_masters/city_master/export_city_pdf";
          break;
        // Add more Alt key shortcuts here as needed
      }
    }
  });
</script>