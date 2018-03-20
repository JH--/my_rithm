const nestedArr = ['Elie', ['Mat', ['Tim']],['Colt',['Whisky', ['Janey'],'Tom']],'Lorien']; 

countVowels = arr => {
    const vowels = new Set('aeiouAEIOU');
    return arr.join('').split('').filter(i => vowels.has(i)).length;
}

countVowels(nestedArr);



