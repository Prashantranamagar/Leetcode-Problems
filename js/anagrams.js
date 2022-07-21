// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
// typically using all the original letters exactly once.

//Example:
// Input: s = "anagram", t = "nagaram"    Output: true
// Input: s = "rat", t = "car"     Output: false


var buildCharMap = function(string){
    charMap = {}
    for (let char in string){
        // if(charMap[char]){
        //     charMap[char] ++
        // }else{
        //     charMap[char] = 1
        // }
        
        charMap[char] = charMap[char] + 1 || 1
    }
    return charMap
}

var isAnagram = function(s, t) {
    
    const charMapS = buildCharMap(s)
    const charMapT = buildCharMap(t)
    if (Object.keys(charMapS).length !== Object.keys(charMapT).length){
        return false
    }
    for (let char in charMapS){
        if (charMapS[char] === charMapT[char]){
            return true
        }
    }
    return false
    
};