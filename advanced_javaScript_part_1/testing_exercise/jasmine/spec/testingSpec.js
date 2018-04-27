
// WRITE YOUR TESTS HERE!

describe("replaceWith", function () {
	it("should take replace a target within a string", function() {
		expect(replaceWith("xyx", "y", "Q")).toBe("xQx");
	});
	it("should be case sensitive", function () {
		expect(replaceWith("abcAzaZA", "A", "Q")).toBe("abcQzaZQ");
	});
});

describe("expand", function () {
	it("should take in an array and a number and a copy of the array * N", function () {
		expect(expand([4,2,0], 3)).toEqual([4,2,0,4,2,0,4,2,0]);
	});
	it("should take in an array and a number and a copy of the array * N", function () {
		expect(expand(["foo", "bar"], 1)).toEqual(["foo", "bar"]);
	});
});

describe("acceptNumbersOnly", function () {
	it("should take in any number of args and return true if all of them are numbers", function () {
		expect(acceptNumbersOnly(1, "foo")).toBe(false);
	});
	it("should take in any number of args and return true if all of them are numbers", function () {
		expect(acceptNumbersOnly(1,2,3,4,5,6,7)).toBe(true);
	});
	it("should take in any number of args and return true if all of them are numbers", function () {
		expect(acceptNumbersOnly(1,2,3,4,5,6,NaN)).toBe(false);
	});
});

describe("mergeArrays", function () {
	it("should take in two arrays and return one array of the values sorted", function () {
		expect(mergeArrays([23,420], [69,87,5])).toEqual([5,23,69,87,420]);
	});
});

describe("mergeObjects", function () {
	let obj1 = {
		  name: "foo",
		  num: 23
	};
	let obj2 = {
		  test: "thing",
		  num: 55
	};
	let obj3 = {
		  underground: "forever",
		  move: "to the beat"
	}
	it("should take in two objects and return an object with keys and values combined", function () {
		expect(mergeObjects(obj1, obj3)).toEqual({
			name: "foo",
			num: 23,
			underground: "forever",
			move: "to the beat"
		});
	});
	it("should override the first objects key:value with the second objects if they have the same key", function () {
		expect(mergeObjects(obj1, obj2)).toEqual({
			name: "foo",
			num: 55,
			test: "thing"
		});
	});
});
