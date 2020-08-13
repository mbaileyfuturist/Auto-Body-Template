 
//Hover Effect
function myFunction(y) {
    if (y.matches) { 
        var techContainer = document.getElementById("tech-container");
        var carContainer = document.getElementById("car-container");
        var calendarContainer = document.getElementById("calendar-container");

        //mouse over
        techContainer.onmouseover = function(){
            //Wrench
            var techIcon = document.getElementById("build-icon");
            techIcon.style.transitionDuration = "1s";
            techIcon.style.color = "#7DC8FF"
            techIcon.style.fontSize = "9rem";
        }
        carContainer.onmouseover = function(){
            //Car
            var techIcon = document.getElementById("car-icon");
            techIcon.style.transitionDuration = "1s";
            techIcon.style.color = "#7DC8FF"
            techIcon.style.fontSize = "9rem";
        }
        calendarContainer.onmouseover = function(){
            //Calendar.
            var techIcon = document.getElementById("calendar-icon");
            techIcon.style.transitionDuration = "1s";
            techIcon.style.color = "#7DC8FF"
            techIcon.style.fontSize = "9rem";
        }

        //mouse out.
        techContainer.onmouseout = function(){
            var techIcon = document.getElementById("build-icon");
            techIcon.style.transitionDuration = "1s";
            techIcon.style.color = "#FFFFFF"
            techIcon.style.fontSize = "750%";
        }
        carContainer.onmouseout = function(){
            var techIcon = document.getElementById("car-icon");
            techIcon.style.transitionDuration = "1s";
            techIcon.style.color = "#FFFFFF"
            techIcon.style.fontSize = "750%";
        }
        calendarContainer.onmouseout = function(){
            var techIcon = document.getElementById("calendar-icon");
            techIcon.style.transitionDuration = "1s";
            techIcon.style.color = "#FFFFFF"
            techIcon.style.fontSize = "750%";
        }
    }
};

var y = window.matchMedia("(min-width: 1010px)");
myFunction(y);
y.addListener(myFunction); 