

function load_strategies(){
         document.getElementById("preference").value = localStorage.getItem('pref');
         document.getElementById("preference").style.visibility = "hidden";
changebarstatus();

}

//PROGRESS BAR
var progressbar_value = "35%";


function changebarstatus(){
         document.getElementById("myBar").style.width = progressbar_value;
         document.getElementById("label").innerHTML = progressbar_value;
}




function strategy1(){
        //Only perform tasks if this condition is fulfilled
        if (progressbar_value == "100%"){

        }
        else{
        alert("Please wait. The system is setting up the initial temperature");
        }
}

function strategy2(){
        //Only perform tasks if this condition is fulfilled
        if (progressbar_value == "100%"){

        }
        else{
        alert("Please wait. The system is setting up the initial temperature");
        }
}


function strategy3(){
       //Only perform tasks if this condition is fulfilled
        if (progressbar_value == "100%"){

        }
        else{
        alert("Please wait. The system is setting up the initial temperature");
        }
}

function strategy4(){

        //Only perform tasks if this condition is fulfilled
        if (progressbar_value == "100%"){

        }
        else{
        alert("Please wait. The system is setting up the initial temperature");
        }



}