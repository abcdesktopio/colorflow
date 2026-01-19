build: binding.gyp 
	npm run build

install:
	npm install

audit:
	npm audit fix

test: colorflow.test.js
	npm test
