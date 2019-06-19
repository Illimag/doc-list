# Web App Fullscreen API

This is an API to fullscreen a Web App from the browser.

Firstly, because of security reasons fullscreen cannot be done on document load.

Instead there needs to be an user interaction for example an onclick event.

Here is an example:

	onclick="launchFullscreen(document.documentElement);"

So onclick the function launchFullscreen will run with the argument document.documentElement.

	document.documentElement

is the full HTML page.

To only make certain elements full screen:

	document.getElementByID(#element)

Put that in a div.

For example:

	<div class="button" onclick="launchFullscreen(document.documentElement);"></div>

Now here is the function launchFullscreen

	function launchFullscreen(element) {
		if(element.requestFullscreen) {
		  element.requestFullscreen();
		} else if(element.mozRequestFullScreen) {
		  element.mozRequestFullScreen();
		} else if(element.webkitRequestFullscreen) {
		  element.webkitRequestFullscreen();
		} else if(element.msRequestFullscreen) {
		  element.msRequestFullscreen();
		}
	  }

This is the API which is cross-browser functionality.

This is how to exit fullscreen.

	function exitFullscreen () {
	  if (document.exitFullscreen) {
	    document.exitFullscreen();
	  } else if (document.mozCancelFullScreen) {
	    document.mozCancelFullScreen();
	  } else if (document.webkitExitFullscreen) {
	    document.webkitExitFullscreen();
	  } else if (document.msExitFullscreen) {
	    document.msExitFullscreen();
	  }
	}

These are how to config properties and events:

Just run on browser and see console to see what they do.

	  function dumpFullscreen() {
		console.log("document.fullscreenElement is: ", document.fullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement || document.msFullscreenElement);
		console.log("document.fullscreenEnabled is: ", document.fullscreenEnabled || document.mozFullScreenEnabled || document.webkitFullscreenEnabled || document.msFullscreenEnabled);
	  }
  
	  // Events
	  document.addEventListener("fullscreenchange", function(e) {
		console.log("fullscreenchange event! ", e);
	  });
	  document.addEventListener("mozfullscreenchange", function(e) {
		console.log("mozfullscreenchange event! ", e);
	  });
	  document.addEventListener("webkitfullscreenchange", function(e) {
		console.log("webkitfullscreenchange event! ", e);
	  });
	  document.addEventListener("msfullscreenchange", function(e) {
		console.log("msfullscreenchange event! ", e);
	  });

Fullscreen CSS selectors

	:-webkit-full-screen {
	  /* properties */
	}

	:-moz-full-screen {
	  /* properties */
	}

	:-ms-fullscreen {
	  /* properties */
	}

	:full-screen { /*pre-spec */
	  /* properties */
	}

	:fullscreen { /* spec */
	  /* properties */
	}

	/* deeper elements */
	:-webkit-full-screen video {
	  width: 100%;
	  height: 100%;
	}

	/* styling the backdrop*/
	::backdrop {
	  /* properties */
	}
	::-ms-backdrop {
	  /* properties */
	}

6/16/2019
