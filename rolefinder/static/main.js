function selectItem(el){
    var element =  document.getElementById(el.id);    
    if(element.getAttribute("selectedtag") == "none"){
        element.classList.add("black")
        element.setAttribute("selectedtag", "selected")
    }else{
        element.classList.remove("black")
        element.setAttribute("selectedtag", "none")
    }
}