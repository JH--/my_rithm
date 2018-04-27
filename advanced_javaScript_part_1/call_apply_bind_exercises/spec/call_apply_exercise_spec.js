describe("#sumEvenArguments", function(){
  it("takes all of the arguments passed to a function and returns the sum of the even ones", function(){
    expect(sumEvenArguments(1,2,3,4)).toBe(6); // 6
    expect(sumEvenArguments(1,2,6)).toBe(8); // 8
    expect(sumEvenArguments(1,2)).toBe(2); // 2
  });
});

describe("#arrayFrom", function(){
  function convert(){
      var arr = arrayFrom(arguments);
      return arr;
  }
  it("takes an array like object and converts it into an array", function(){
    var argsArr = convert();
    expect(argsArr.reduce).toEqual(jasmine.any(Function));
  });
});


describe("#invokeMax", function(){
  function add(a,b){
      return a+b
  }
  it("returns a function that calls another function a certain amount of times", function(){

   var addOnlyThreeTimes = invokeMax(add,3);
   expect(addOnlyThreeTimes(1,2)).toEqual(3); // 3
   expect(addOnlyThreeTimes(2,2)).toEqual(4); // 4
   expect(addOnlyThreeTimes(1,2)).toEqual(3); // 3
   expect(addOnlyThreeTimes(1,2)).toEqual("Maxed Out!");
   expect(addOnlyThreeTimes(1,2)).toEqual("Maxed Out!");
  });
});
  