$(document).ready(function () {


//    $(document).on('click', '.nav-item a', function (e) {
//        $(this).parent().addClass('active').siblings().removeClass('active');
//    });
  var url = document.location.href;
  window.alert(url)
  window.alert(url.split('/').slice(-2)[0])
  var templ_name = url.split('/').slice(-2)[0]
  //var templ_name = document.location.pathname.split('/').slice(-1)[0]
  window.alert(templ_name)
  //sdkjghdkgjh
  if (templ_name!="") {
    $("a[href='/cctbx/']").removeClass("active");
    $("a[href$="+templ_name+"]").addClass("active");


  };

  if (templ_name=='documentation_overview' || templ_name=='newsletter_artcls' || templ_name.startsWith("doc_")) {
    //$('#body-row .collapse').collapse('show');
    //$(".submenu-head").attr("aria-expanded":"true");
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
