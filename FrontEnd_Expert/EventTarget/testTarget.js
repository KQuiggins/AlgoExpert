const { EventTarget } = require('./eventTarget'); // Replace path/to/file with the actual path to the file.

// Test the addEventListener() method.
const eventTarget = new EventTarget();
const callback1 = () => console.log('Callback 1');
const callback2 = () => console.log('Callback 2');
eventTarget.addEventListener('click', callback1);
eventTarget.addEventListener('click', callback2);
console.log(eventTarget.listeners); // Expected output: { click: Set { [Function: callback1], [Function: callback2] } }

// Test the removeEventListener() method.
eventTarget.removeEventListener('click', callback1);
console.log(eventTarget.listeners); // Expected output: { click: Set { [Function: callback2] } }

// Test the dispatchEvent() method.
eventTarget.dispatchEvent('click'); // Expected output: "Callback 2"
