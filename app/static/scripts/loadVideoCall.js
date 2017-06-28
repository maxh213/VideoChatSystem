$(document).ready(function(){
    var AppearIn = window.AppearIn || require('appearin-sdk');
	var appearin = new AppearIn();

	var isWebRtcCompatible = appearin.isWebRtcCompatible();
	//TODO: IF THIS IS FALSE ADD USER FRIENDLY ERROR MESSAGE
	console.log(isWebRtcCompatible);

	
	//TODO: this is a flag, refactor to remove
	//TODO: ADD THE INVITE A NEW USER TO A CALL TEXT

	//if roomName is defined then this is a user sharing a call
	if (roomName) {
		serveExistingCall(appearin);
	}
	//Otherwise it is the standard homepage
	else {
		createAndServeNewCall(appearin);
		
	}
});

function createAndServeNewCall(appearin) {
	appearin.getRandomRoomName().then(function (roomName) {

	    var iframe = document.getElementById("videoCallFrame");
		appearin.addRoomToIframe(iframe, roomName);

        var request = $.ajax({
			url: "logCall/" + userId + roomName,
			type: "GET",
			data: '{}',
			dataType: "json",
			contentType: "application/json",
		});

		request.done(function(result) {
			var callId = result;
			$("#shareCallMessage").append(" Share this call with the following link: " + $(location).attr('host') + "/call" + roomName + "/" + callId);
		});

		request.fail(function(jqXHR, textStatus) {
		  	console.log( "Request failed: " + textStatus );
		});
	});
}

function serveExistingCall(appearin) {
	var iframe = document.getElementById("videoCallFrame");
	appearin.addRoomToIframe(iframe, roomName);
	var request = $.ajax({
		url: "../../logGuestInActiveCall/" + userId + "/" + callId,
		type: "GET",
		data: '{}',
		dataType: "json",
		contentType: "application/json",
	});

	request.done(function(result) {
		$("#shareCallMessage").append(" Share this call with the following link: " + $(location).attr('host') + "/call" + roomName + "/" + callId);
	});


	request.fail(function(jqXHR, textStatus) {
	  	console.log( "Request failed: " + textStatus );
	});
}