$(document).ready(function () {

  var url = document.location.href;
  var templ_name = url.split('/').slice(-2)[0]
  //window.alert(templ_name)
  if (templ_name!="phenix") {
    $('a[href="/docs/phenix/"]').removeClass("active");
    $("a[href*="+templ_name+"]").addClass("active");
  };

  if (templ_name=='doc_overview' || templ_name=='template' || templ_name=='examples' || templ_name.startsWith("doc_")) {
    $("#submenu-doc").addClass("show");
  };

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
    if (ind==0 && shown==true) {
      return;
    }
    shown=false
    $('.CodeMirror').each(function(i, el){
        el.CodeMirror.toTextArea();
    });

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
  });

});
