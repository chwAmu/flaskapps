list=[]

window.onload=load;

function reloadPage() {
    location.reload();
}

delOperation=false
selectingId=''
var offX=0
var offY=0
var offXY=[]

function load(){
	console.log('system is loaded..')
}

function ondragstart_handler(event){	
	var style = window.getComputedStyle(event.target, null);
    var str = (parseInt(style.getPropertyValue("left")) - event.clientX) + ',' + (parseInt(style.getPropertyValue("top")) - event.clientY);
    offXY.push(parseInt(style.getPropertyValue("left")) - event.clientX)
    offXY.push(parseInt(style.getPropertyValue("top")) - event.clientY)
}


function ondrag_handler(ev,id) {
	// console.log('drapping...')
	var ele=document.getElementById(ev.target.id);
	ele.style.display='none';
	ele.style.top=ev.y+'px';
	ele.style.left=ev.x+'px';
	ele.style.position='absolute';
}


function ondragend_handler(event,id){
	var offset = event.dataTransfer.getData("text").split(',');
    var dm = document.getElementById(id);
    dm.style.left = (event.clientX + offXY[0] )+ 'px';
    dm.style.top = (event.clientY + offXY[1]) + 'px';
 	dm.style.display='Block'

    event.preventDefault();
    return false;
	
}

function addElement(){
	var ne=document.createElement('div')
	// var nc=document.createTextNode('newtag_'+getElementLength())
	ne.id='p'+getElementLength()
	// ne.appendChild(nc)
	var currentDiv=document.getElementById('frame-1')
	currentDiv.appendChild(ne)
	ne.className='tagElements'
	saveBtn()	
	reloadPage()
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

// save
function saveBtn(){

	var n=document.getElementById('frame-1').children.length
	var datalist=countingclass('tagElements')

	var finallist=[]

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
	var datalist=countingclass('tagElements')

	for (var i=0;i<jsonData.length;i++){
		ele=document.getElementById(datalist[i].id)
		ele.style.top=jsonData[i].y
		ele.style.lef=jsonData[i].x
	}

}

function selElement(id){

	ele=document.getElementById(id.id)
	ele.parentNode.removeChild(ele)
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

function countingclass(className){
	var ele=document.getElementsByClassName(className)
	return ele
}

function popupDelOper(eleId){
	ele=document.getElementById(eleId.id)
	selElement(selectingId)
}

function popEditOper(eleId){
	// selElement(selectingId)
}

function popupTrigger(eleId){
	selectingId=eleId
}

// Bootstrap’s js

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});

$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('Operation of Object ' + recipient)
  // modal.find('.modal-body input').val(recipient)
})

