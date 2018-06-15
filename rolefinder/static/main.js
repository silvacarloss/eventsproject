function selectItem(el){
    var element =  document.getElementById(el.id);    
    if(element.getAttribute("selectedtag") == "none"){
        element.classList.add("black")
        element.setAttribute("selectedtag", "selected")
    }else{
        element.classList.remove("black")
        element.setAttribute("selectedtag", "none")
    }

    var divTags = document.getElementById("selected_tags").querySelectorAll(".black")
    let ids = ""
    for(i=0; i<divTags.length; i++){
        ids+="," + divTags[i].id
    }
    console.log(ids)
    var hiddenField = document.getElementById("tagsselected").value = ids
}