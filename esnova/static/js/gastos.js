
function showContent() {
  element = document.getElementById("content");
  check = document.getElementById("check");
  if (check.checked) {
      element.style.display='block';
  }
  else {
      element.style.display='none';
  }
}
function showContent2() {
element = document.getElementById("content");
check = document.getElementById("check");
if (check.checked) {
    element.style.display='none';
}
else {
    element.style.display='none';
}
document.getElementById("texto1").value='';
document.getElementById("texto2").value='';
}

function showContent3() {
  element = document.getElementById("content2");
  check = document.getElementById("check2");
  if (check.checked) {
      element.style.display='block';
  }
  else {
      element.style.display='none';
  }
}
function showContent4() {
  element = document.getElementById("content2");
  check = document.getElementById("check2");
  if (check.checked) {
      element.style.display='block';
  }
  else {
      element.style.display='none';
  }
  document.getElementById("texto3").value='';
}

function showContent5() {
  element = document.getElementById("content3");
  element2 = document.getElementById("content10");
  check = document.getElementById("inputState").value;
  if (check=='Motocicleta') {
      element.style.display='block';
      element2.style.display='none';
      document.getElementById("texto10").value='';

  } else   if (check=='Automóvil') {
        element.style.display='block';
        element2.style.display='none';
        document.getElementById("texto10").value='';
    }else   if (check=='otro') {
          element2.style.display='block';
          element.style.display='none';
          document.getElementById("texto4").value='';
      }else {
      element.style.display='none';
      element2.style.display='none';
      document.getElementById("texto10").value='';
      document.getElementById("texto4").value='';
  }


}


function showContent6() {
  element = document.getElementById("content4");
  check = document.getElementById("check4");
  if (check.checked) {
      element.style.display='block';
  }
  else {
      element.style.display='none';
  }
   $('#texto5').prop("required", true);
   $('#texto6').prop("required", true);
   $('#texto7').prop("required", true);
}
function showContent7() {
element = document.getElementById("content4");
check = document.getElementById("check4");
if (check.checked) {
    element.style.display='none';
}
else {
    element.style.display='none';
}
document.getElementById("texto5").value='';
document.getElementById("texto6").value='';
document.getElementById("texto7").value='';
$('#texto5').removeAttr("required");
$('#texto6').removeAttr("required");
$('#texto7').removeAttr("required");
}

function showContent8() {
  element = document.getElementById("content5");
  check = document.getElementById("check5");
  if (check.checked) {
      element.style.display='block';
  }
  else {
      element.style.display='none';
  }
}
function showContent9() {
element = document.getElementById("content5");
check = document.getElementById("check5");
if (check.checked) {
    element.style.display='none';
}
else {
    element.style.display='none';
}
document.getElementById("texto8").value='';
document.getElementById("texto9").value='';

}
