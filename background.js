chrome.omnibox.onInputChanged.addListener(
  function(text, suggest) 
  {
    console.log('inputChanged: ' + text);
    suggest([
      {content: text + " ", description: "Save it already!"},
    ]);
  });

chrome.omnibox.onInputEntered.addListener(
	function (text) 
	{
    	document.body.innerHTML += '<form id="dynForm" action="http://save-to-evernote.appspot.com/sign" method="post"><input type="hidden" name="note" value='+text+'></form>';
		document.getElementById("dynForm").submit();

	}
);

