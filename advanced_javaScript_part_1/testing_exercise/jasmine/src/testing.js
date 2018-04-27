function replaceWith(str, target, replacement) {
	return str.split('').map(s => s === target ? replacement : s).join('');
};

function expand(arr, N) {
	return [].concat.apply([], Array(N).fill(arr));
};

function acceptNumbersOnly() {
	return [].slice.call(arguments).filter(
		i => typeof i === 'number' && !(isNaN(i))).length === arguments.length;
};

function mergeArrays(arr1, arr2) {
	return arr1.concat(arr2).sort((a,b) => a-b);
};

function mergeObjects(obj1, obj2) {
	//the instructions said not to use Object.assign
	let result = {}
	for(let key in obj1){
		result[key] = obj1[key];
	};
	for(let key in obj2){
		result[key] = obj2[key];
	};
	return result;
};