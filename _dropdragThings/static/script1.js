list=[]

window.onload=load;

delOperation=false
selectingId=''

function load(){
	console.log('system is loaded..')
}

function ondragstart_handler(ev){	
	console.log('start to drag..')
}

function ondrag_handler(ev,id) {
	// console.log('drapping...')
	var ele=document.getElementById(ev.target.id);
	ele.style.display='none';
	ele.style.top=ev.y+'px';
	ele.style.left=ev.x+'px';
	ele.style.position='absolute';
}


function ondragend_handler(ev,id){
	// console.log('drapping end..')
	var ele=document.getElementById(ev.target.id);
	ele.style.top=ev.y+'px';
	ele.style.left=ev.x+'px';
	ele.style.display='Block';
	
}

function addElement(){
	var ne=document.createElement('div')
	var nc=document.createTextNode('newtag_'+getElementLength())
	ne.id='p'+getElementLength()
	ne.appendChild(nc)

	var currentDiv=document.getElementById('frame-1')
	// document.body.appendChild(ne,currentDiv)
	currentDiv.appendChild(ne)
	console.log(getElementLength())
}

function getElementLength(){
	return document.getElementById('frame-1').children.length
}

function getElemnts(ele){
	dict={}
	dict['y']=ele.getBoundingClientRect().top;
	dict['x']=ele.getBoundingClientRect().left;
	list.push(dict)
}

function getAllElements(){

	var n=document.getElementById('frame-1').children.length
	for( var i=0; i<n ;i++){
		ele=document.getElementById('p'+i);
		getElemnts(ele);
	}	

	data = JSON.stringify(list)
	var request = new XMLHttpRequest();
	request.open('POST', '', true);
	request.setRequestHeader('Content-Type', 'application/json','charset=UTF-8');
	request.send(data);
	list=[]

  	request.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      callback(this.responseText);
    }  
  };
  
  request.onerror = function(error) {
    console.error('error')
    rewritelabel(null,false)
};
  

  function callback(result){
    r=JSON.parse(result);
    layoutReflash(r)
}
}

function layoutReflash(jsonData){
	console.log(jsonData[1].y)
	console.log(jsonData.length)
	for (var i=0;i<jsonData.length;i++){
		ele=document.getElementById('p'+i)
		ele.style.top=jsonData[i].y
		ele.style.lef=jsonData[i].x
	}

}

function selElement(id){
	console.log(id.id)
	if (delOperation){
		ele=document.getElementById(id.id)
		ele.parentNode.removeChild(ele)
	}

}

function delBtn(){
	if (delOperation === false){
		delOperation=true
	}
	else{
		delOperation=false
	}
	console.log(delOperation)
}


$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});

