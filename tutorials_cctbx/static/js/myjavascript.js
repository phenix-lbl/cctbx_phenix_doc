$(document).ready(function () {






//var shown = [false, false, false]
  var shown = false

  $('.code').each(function(index, elem){

      CodeMirror.fromTextArea(elem, {
        mode: {name: "python",
           version: 3,
           singleLineStringErrors: false},
        lineNumbers: true,
        indentUnit: 4,
        matchBrackets: true});
  });
  $('.output').each(function(index, elem){
    CodeMirror.fromTextArea(elem, {
      lineNumbers: false
    })
  })

  var shown=true

  $('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {

    ind = $(e.target).parent().index()
    //window.alert(shown)
    if (ind==0 && shown==true) {
      return;
    }
    shown=false
    $('.CodeMirror').each(function(i, el){
        el.CodeMirror.toTextArea();
    });

    //CM = document.getElementById('CMEditor');
    //CM.CodeMirror.toTextArea();
    //$('.CodeMirror').each(function(i, el){
    //    el.CodeMirror.refresh();
    //});

    $('.code').each(function(index, elem){

        CodeMirror.fromTextArea(elem, {
          mode: {name: "python",
             version: 3,
             singleLineStringErrors: false},
          lineNumbers: true,
          indentUnit: 4,
          matchBrackets: true});
    });
    $('.output').each(function(index, elem){
      CodeMirror.fromTextArea(elem, {
        lineNumbers: false
      })
    })
})

var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("myactive");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

});
