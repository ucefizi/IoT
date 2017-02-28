window.onload = function () {
    var on_mouse_over = function() {
        this.className = this.className + " hovered";
    };
    var on_mouse_out = function() {
        this.className = this.className.replace( /(?:^|\s) hovered(?!\S)/g , '');
    }
    var items = document.getElementsByTagName('a');
    for(var i = 0; i < items.length; i++) {
        items[i].addEventListener('mouseover', on_mouse_over);
        items[i].addEventListener('mouseout', on_mouse_out);
    }
};


function search() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}