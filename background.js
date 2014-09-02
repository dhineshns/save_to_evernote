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
		alert("You enterd : " + text)
	}
);