var eventFire = (MyElement, ElementType) => { 
	var MyEvent = document.createEvent("MouseEvents"); 
	MyEvent.initMouseEvent 
	(ElementType, true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null); 
	MyElement.dispatchEvent(MyEvent); 
};



function simulateMouseEvents(element, eventName) 
{ 
	var mouseEvent = document.createEvent('MouseEvents'); 
	mouseEvent.initEvent(eventName, true, true); 
    element.dispatchEvent(mouseEvent); 
    myFunc()
    
} 

var mname = JSON.parse('["veMiyAmzDkbHtrUhsI"]');

var donebynow = false;
var refreshIntervalId = null;
mname.forEach(element => {
    simulateMouseEvents(document.querySelector('[title="' + element + '"]'), 'mousedown'); 
    
});




function myFunc() 
{ 

	messageBox = document.querySelectorAll("[contenteditable='true']")[1]; 
	var x = new Date();
	message = document.getElementsByClassName("_3Id9P _1VzZY selectable-text copyable-text")[0].innerText + " "+ x.toString(); // Replace My Message with your message use  to add spaces to your message

	counter = 1; // Replace 1 with the number of times you want to send your message

	for (i = 0; i < counter; i++) { 
		event = document.createEvent("UIEvents"); 

		messageBox.innerHTML = message.replace(/ /gm, ' '); // test it
		event.initUIEvent("input", true, true, window, 1); 
		messageBox.dispatchEvent(event); 
        
        eventFire(document.querySelector('span[data-icon="send"]'), 'click'); 
	} 
}


	 

 

