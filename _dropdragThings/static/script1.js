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
	return dict
}

function saveBtn(){

	var n=document.getElementById('frame-1').children.length
	var datalist=counting('frame-1','div')


	var finallist=[]

	ele=document.getElementById('frame-1');
	console.log(ele.parentNode)

	for( var i=0; i<datalist.length ;i++){
		dict={}
		console.log(datalist[i].id)
		ele=document.getElementById(datalist[i].id);
		console.log(ele)
		dict=getElemnts(ele)
		finallist.push(dict)
	}	
	console.log(finallist)

	data = JSON.stringify(finallist)
	var request = new XMLHttpRequest();
	request.open('POST', '', true);
	request.setRequestHeader('Content-Type', 'application/json','charset=UTF-8');
	request.send(data);

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
	var datalist=counting('frame-1','div')

	for (var i=0;i<jsonData.length;i++){
		ele=document.getElementById(datalist[i].id)
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

function counting(id,cmd){
	var mainf=document.getElementById(id)
	var inMainf=mainf.getElementsByTagName(cmd)
	idarray=[]
	for (var i=0;i<inMainf.length;i++){
			idarray.push(inMainf[i])
	}
	return idarray
}




$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});

