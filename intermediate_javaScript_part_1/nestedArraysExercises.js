/*Write a function called rotate, which takes an array and a number and moves each element
however many spaces the number is to the right. */

const nums = [1,2,3];

rotate = (numsArr, moves) => {
    return numsArr.map((val, i) => numsArr.slice((i - moves) % numsArr.length)[0]);
}

rotate(nums, 1); //[3,1,2]
rotate(nums, 2); //[2,3,1]
rotate(nums, 3); //[1,2,3]
rotate(nums, 5); //[2,3,1]
rotate(nums, 6); //[1,2,3]

/*Write a function called makeXOGrid which takes in two parameters, rows and columns,
and returns an array of arrays with the number of values in each subarray equal to
the columns parameter and the number of subarrays equal to the rows parameter. The
values in the subarray should switch between "X" and "O". */

makeXOGrid = (rows, columns) => {
    const xRow = [...Array(columns).keys()].map(c => c%2==0 ? 'X' : 'O');
    const oRow = [...Array(columns).keys()].map(c => c%2==0 ? 'O' : 'X');
    return [...Array(rows).keys()].map(r => columns%2 === 1 && r%2 === 1 ? oRow : xRow);
}

makeXOGrid(1,3); //[['X', 'O', 'X']]
makeXOGrid(3,5); //[['X', 'O', 'X', 'O', 'X'], ['O', 'X', 'O', 'X', 'O'], ['X', 'O', 'X', 'O', 'X']]