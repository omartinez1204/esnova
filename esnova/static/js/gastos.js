
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
      document.getElementById("texto10").value=check;

  } else   if (check=='Automóvil') {
        element.style.display='block';
        element2.style.display='none';
        document.getElementById("texto10").value=check;
    }else   if (check=='otro') {
          element2.style.display='block';
          element.style.display='none';
          document.getElementById("texto10").value='';
          document.getElementById("texto4").value='';
      }else {
      element.style.display='none';
      document.getElementById("texto10").value=check;
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
}



function filterFloat(evt,input){
    // Backspace = 8, Enter = 13, ‘0′ = 48, ‘9′ = 57, ‘.’ = 46, ‘-’ = 43
    var key = window.Event ? evt.which : evt.keyCode;
    var chark = String.fromCharCode(key);
    var tempValue = input.value+chark;
    if(key >= 48 && key <= 57){
        if(filter(tempValue)=== false){
            return false;
        }else{
            return true;
        }
    }else{
          if(key == 8 || key == 13 || key == 0) {
              return true;
          }else if(key == 46){
                if(filter(tempValue)=== false){
                    return false;
                }else{
                    return true;
                }
          }else{
              return false;
          }
    }
}
function filter(__val__){
    var preg = /^([0-9]+\.?[0-9]{0,2})$/;
    if(preg.test(__val__) === true){
        return true;
    }else{
       return false;
    }

}
