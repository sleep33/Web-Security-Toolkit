const zxcvbn = require('zxcvbn');

const password = process.argv[2];
const result = zxcvbn(password);

console.log(`Password strength score: ${result.score}`);
console.log(`Feedback: ${result.feedback.suggestions.join(' ')}`);
