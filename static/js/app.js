function loadDoc() {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    document.getElementById("demo").innerHTML = xhttp.responseText;
    }
  xhttp.open("GET", "http://localhost:8080/logs, true);
  xhttp.send();
}