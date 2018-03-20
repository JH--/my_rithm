var users = [
{
  username: "larry",
  email: "larry@foo.com",
  yearsExperience: 22.1,
  favoriteLanguages: ["Perl", "Java", "C++"],
  favoriteEditor: "Vim",
  hobbies: ["Fishing", "Sailing", "Hiking"],
  hometown: {
    city: "San Francisco",
    state: "CA"
  }
},
{
  username: "jane",
  email: "jane@test.com",
  yearsExperience: 33.9,
  favoriteLanguages: ["Haskell", "Clojure", "PHP"],
  favoriteEditor: "Emacs",
  hobbies: ["Swimming", "Biking", "Hiking"],
  hometown: {
    city: "New York",
    state: "NY"
  }
},
{
  username: "sam",
  email: "sam@test.com",
  yearsExperience: 8.2,
  favoriteLanguages: ["JavaScript","Ruby", "Python", "Go"],
  favoriteEditor: "Atom",
  hobbies: ["Golf", "Cooking", "Archery"],
  hometown: {
    city: "Fargo",
    state: "SD"
  }
},
{
  username: "anne",
  email: "anne@test.com",
  yearsExperience: 4,
  favoriteLanguages: ["C#", "C++", "F#"],
  favoriteEditor: "Visual Studio Code",
  hobbies: ["Tennis", "Biking", "Archery"],
  hometown: {
    city: "Albany",
    state: "NY"
  }
},
{
  username: "david",
  email: "david@test.com",
  yearsExperience: 12.5,
  favoriteLanguages: ["JavaScript", "C#", "Swift"],
  favoriteEditor: "Sublime Text",
  hobbies: ["Volunteering", "Biking", "Coding"],
  hometown: {
    city: "Los Angeles",
    state: "CA"
  }
}
]
 
// Write a function called printEmails which console.logs's each email for the users.

function printEmails () {
  users.forEach(obj => console.log(obj.email));
}

// Write a function called printHobbies which console.log's each hobby for each user.

function printHobbies () {
  users.forEach(obj => obj.hobbies.forEach( hobby => console.log(hobby)));
}

/* Write a function called findHometownByState which returns the first user which has a
hometown of the state that is passed in. */

function findHometownByState (state) {
  return users.filter(obj => obj.hometown.state === state)[0];
}

// Write a function called allLanguages which returns an array of all of the unique values

function allLanguages () {
  return Array.from(new Set(users.reduce( (acc, next) => acc.concat(next.favoriteLanguages), [])));
}

/* Write a function called hasFavoriteEditor which returns a boolean if any of the users have 
the editor passed in */

function hasFavoriteEditor (editor) {
  return users.map(obj => obj.favoriteEditor).some(e => e === editor);
}

/* Write a function called findByUsername which takes in a string and returns an object in the
users array that has that username */

function findByUsername (name) {
  return users.filter( obj => obj.username === name)[0];
}

/* Write a function called vowelCount that accepts a string and returns an object with each 
key being the vowel and the value being the number of times the vowel occurs in the string 
(the order of keys in the object does not matter). */

function vowelCount (str) {
    const vowels = str.split('').filter(s => 'a e i o u'.split(' ').includes(s.toLowerCase()));
    return vowels.reduce((acc, next) => {
        if(next in acc){
            acc[next]++;
        } else {
            acc[next] = 1;
        }
        return acc;
    }, {});  
}

/* Write a function called removeVowels that accepts a string and returns an array of each
character that is not a vowel (y should not count as a vowel for this function). */

function removeVowels (str) {
  return str.split('').filter(s => !('a e i o u'.split(' ').includes(s)));
}
