
// WRITE YOUR TESTS HERE!

var person;

beforeEach(function(){
  person = new Person("Elie", "Schoppik", "purple", 34);
});

describe("Person", function(){
  it("has a firstName", function(){
    expect(person.hasOwnProperty("firstName")).toEqual(true);
  });
  it("has a lastName", function(){
    expect(person.hasOwnProperty("lastName")).toEqual(true);
  });
  it("has a favoriteColor", function(){
    expect(person.hasOwnProperty("favoriteColor")).toEqual(true);
  });
  it("has a favoriteNumber", function(){
    expect(person.hasOwnProperty("favoriteNumber")).toEqual(true);
  });
  it("has a favoriteFoods", function(){
    expect(person.hasOwnProperty("favoriteFoods")).toEqual(true);
    expect(person.favoriteFoods).toEqual([]);
  });
});

describe("#fullName", function(){
  it("returns the firstName concatenated with the lastName", function(){
    expect(person.fullName()).toEqual("Elie Schoppik");
  });
});

describe("family", function(){
  var p1, p2;
  beforeEach(function(){
    p1 = new Person();
    p2 = new Person();
  });
  it("is initialized as an empty array on the Person object", function(){
    expect(p1.family).toExist;
    expect(Array.isArray(p1.family)).toEqual(true);
    expect(p1.family.length).toEqual(0);
  });
});

describe("#addToFamily", function(){
  var p1, p2;
  beforeEach(function(){
    p1 = new Person();
    p2 = new Person();
  });
  it("is not shared amongst all objects created from the Person constructor", function(){
    p1.addToFamily(p1);
    expect(p2.family.length).toEqual(0)
  });
  it("adds a new person to the family array ONCE", function(){
    person.addToFamily(p1);
    person.addToFamily(p1);
    person.addToFamily(p1);
    expect(person.family.length).toEqual(1)
  });
  it("only adds objects created from the Person constructor to the array", function(){
    person.addToFamily(p1);
    person.addToFamily("test");
    person.addToFamily({});
    person.addToFamily([]);
    person.addToFamily(false);
    expect(person.family.length).toEqual(1)
  });
});


describe("#toString", function() {
  var p1 = new Person("Tim", "Garcia", "Blue", 7);
  it("is shared amongst all objects created from the Person constructor", function(){
    expect(p1.hasOwnProperty('toString')).to.equal(false);
    expect(Person.prototype.toString).toExist;
  });

  it("returns all the info about the Person", function() {
    expect(p1.toString()).toEqual("Tim Garcia, Favorite Color: Blue, Favorite Number: 7");
  });

});


// PART II

describe("Array.prototype.map", function(){
  var arr = [1,2,3,4];
  it("returns a new array of values with a callback run on each value", function(){
    expect(arr.map(v => v*2)).toEqual([2,4,6,8]);
  });
  it("allows access to the index as a second parameter", function(){
    expect(arr.map((v,i) => i*2)).toEqual([0,2,4,6]);
  });
  it("allows access to the array as the third parameter", function(){
    expect(arr.map((v,i,a) => a.length)).toEqual([4,4,4,4]);
  });
});

describe("Array.prototype.reduce", function(){
  var arr = [1,2,3,4];
  it("adds numbers without an initial value", function(){
    expect(arr.reduce((acc,v) => acc+v)).toEqual(10);
  });
  it("adds numbers with an initial value", function() {
    expect(arr.reduce((acc,v) => acc+v, 10)).toEqual(20);
  })
  it("has an index as the 3rd parameter", function() {
    expect(arr.reduce((acc,v, i) => i === 3 ? "blah": null, 10)).toEqual("blah");
  })
  it("has an index array as the 4th parameter", function() {
    expect(arr.reduce((acc,v, i, arr) => arr.length, 10)).toEqual(4);
  })
  it("can return any type of data", function() {
    var init = {name: "Tim", age: "33", numbers: []};
    var res = arr.reduce((acc,v, i, arr) => {
      acc.numbers.push(v);
      return acc;
    }, init);
    expect(res).toEqual(init);
    expect(res.numbers).toBe("array");
    expect(res.numbers).toEqual(init.numbers);
    expect(res.numbers.length).toEqual(4);
    expect(res.numbers).toEqual(arr);
  });

});

describe("String.prototype.reverse", function(){
  it("returns a new reversed string", function(){
    expect("test".reverse()).to.equal("tset");
    expect("tacocat".reverse()).to.equal("tacocat");
  });
});

describe("Function.prototype.bind", function(){
  function add(a,b){
    return a+b;
  };
  it("returns a function with the context set", function(){
    expect(add.bind(this)).toEqual(jasmine.any(Function));
  });
  it("returns a function with the context set", function(){
    expect(add.bind(this,3)(4)).toEqual(7);
    expect(add.bind(this)(3,4)).toEqual(7);
  });
});