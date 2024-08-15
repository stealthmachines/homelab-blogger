chrome.runtime.onInstalled.addListener(() => {
  console.log("Homelab Network Search Extension Installed");
});

chrome.action.onClicked.addListener(async () => {
  let url = "http://localhost:6000/nodes";
  let response = await fetch(url);
  let data = await response.json();
  
  chrome.storage.local.set({nodes: data.nodes}, () => {
    console.log("Nodes stored in local storage");
  });
});
