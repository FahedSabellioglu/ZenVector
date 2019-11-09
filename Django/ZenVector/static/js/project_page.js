 function changeDetails() {

        var assignedTo = document.getElementById("assignedToD").value;
        console.log(assignedTo);

        var deadline = document.getElementById("deadlineD").value;
        console.log(deadline);

        var detail = document.getElementById("taskDetailsD").value;
        console.log(detail);

        var status =document.getElementById("statusD").value;
        console.log(status);

      // It sould get the task ID and check if the card status has changed, if it has been changed, add the task to the new state.
        document.getElementById(status).innerHTML+=
              "<div class='card'><div class='card-header card-header-danger2'>" + "Card Title !!!" +
              "<button type='button' style='position: absolute; right: 1rem;' class='btn btn-just-icon btn-sm' data-toggle='modal' data-target='#detailModal'>"+
              "<i class='material-icons'>menu</i></button></div> <class='card-body card-text'>" + detail+ "</div></div>";
      // If it is not, it should change the card content.
      // document.getElementById(task ID).innerHTML=
      //         "<div class='card'><div class='card-header card-header-danger2'>" + "Card Title !!!" +
      //         "<button type='button' style='position: absolute; right: 1rem;' class='btn btn-just-icon btn-sm' data-toggle='modal' data-target='#detailModal'>"+
      //         "<i class='material-icons'>menu</i></button></div> <class='card-body card-text'>" + detail+ "</div></div>";

}
 function deleteTask(){

    var x = confirm("Are you sure you want to delete?");
    if (x){
      //  code to delete task
        // document.getElementById("***").innerHTML = "";
      console.log(x);
      return true;
    }
    else{
      console.log(x);
      return false;
    }
}

function addTask() {

      var title = document.getElementById("taskTitle").value;
      console.log(title);

      var assignedTo = document.getElementById("assignedTo").value;
      console.log(assignedTo);

      var deadline = document.getElementById("deadline").value;
      console.log(deadline);

      var detail = document.getElementById("taskDetails").value;
      console.log(detail);

      var status = document.getElementById("status").value;
      console.log(status);

      document.getElementById(status).innerHTML +=
          "<div class='card'><div class='card-header card-header-danger2'>" + title +
          "<button type='button' style='position: absolute; right: 1rem;' class='btn btn-just-icon btn-sm' data-toggle='modal' data-target='#detailModal'>"+
          "<i class='material-icons'>menu</i></button></div> <class='card-body card-text'>" + detail+ "</div></div>";

      // $('#addTaskModal').modal('hide');
  }

function addList() {

  var title = document.getElementById("listTitle").value;
  console.log(title);

  var color = document.getElementById("headerColor").value;
  console.log(color);

  document.getElementById("board").innerHTML +=
      "<div class='col-xs-6 col-md-3'><div class='card-list'><div class='card-header'><h4 class='card-list-title'>"
      +title+"</h4></div><div class='card-list-body text-center' id="+title+"><div class='card'><div class='card-header "+
      " card-header-danger2'>Task Title <button type='button' style='position: absolute; right: 1rem;'class='btn btn-just-icon"+
      " btn-sm' data-toggle='modal' data-target='#detailModal'><i class='material-icons'>menu</i></button></div> "+
      "<class='card-body card-text'>Please click to detail button to change task details</div></div></div></div>"
}

$("#addTask").click(function(){
$("#addTaskModal").modal({backdrop: "static"});
});

$("#addList").click(function(){
$("#addListModal").modal({backdrop: "static"});
});

$("#detailModal").click(function(){
$("#detailModal").modal({backdrop: "static"});
});


 /* Custom Dragula JS */
dragula([
document.getElementById("to-do"),
document.getElementById("doing"),
document.getElementById("done"),
]);

removeOnSpill: false
.on("drag", function(el) {
  el.className.replace("ex-moved", "");
  console.log(el.className)
})
.on("drop", function(el) {
  el.className += "ex-moved";
  console.log(el.className)
})
.on("over", function(el, container) {
  container.className += "ex-over";
  console.log(el.className)
})
.on("out", function(el, container) {
  container.className.replace("ex-over", "");
  console.log(el.className)
});