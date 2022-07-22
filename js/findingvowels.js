// function that return the no of vowels use in the string


function vowels(str){
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for(let i of str){
        if (vowels.includes(i)){
            count ++;
        }
        
    }
    return count;
}