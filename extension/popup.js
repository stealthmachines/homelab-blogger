document.addEventListener('DOMContentLoaded', () => {
  chrome.storage.local.get(['nodes'], function(result) {
    let nodesList = result.nodes || [];
    let listElement = document.getElementById('nodes-list');

    nodesList.forEach(node => {
      let li = document.createElement('li');
      li.textContent = node;
      listElement.appendChild(li);
    });
  });
});
