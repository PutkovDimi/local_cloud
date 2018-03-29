function a() {
    $('.alert').remove();
    var newElement = document.createElement("div");
    var formValue = document.forms["downloadFile"]["putFile"].value;
    if (formValue == ""){
         newElement.textContent = "Упссс.Ошибочка...";
        newElement.className = "alert alert-danger";
    }
    else {
        newElement.textContent = "Молодец ты в деле!!!";
        newElement.className = "alert alert-success";
    }
    newElement.id="alert";
    newElement.style.cssText="padding: .5em 2em;margin:0.7em;font-size:20px;";
    var list = document.getElementById("alert-parent");
    list.appendChild(newElement);

    var newBut = document.createElement("button");
    newBut.className ="close";
    newBut.textContent="close";
    newBut.id="closeAlert";
    newBut.style.cssText="padding-top:5px;font-size:20px;";
    var listic = document.getElementById("alert");
    listic.appendChild(newBut);
    $(document).ready(function(){
                      $('#closeAlert').click(function(){
                                             $('.alert').remove();
                                             })
                      });

}