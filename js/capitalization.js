// function that accepts a string. The function should capatilize the first letter of each word in the 
// string and return the capatilized string.

//Example
// 'Lazy fox'  => 'Lazy Fox'        'i am a man'  => 'I Am A Man'

// function capatalize(str){
//     let capitalString = []
//     let abc = str.split(' ')
//     for (let i of abc){
//         capitalString.push(i[0].toUpperCase() + i.slice(1))
//     }
//     return capitalString.join(' ')
// }


function capatalize(str){
    let result = str[0].toUpperCase()
    for( i=1; i<str.length; i++){
        if(str[i-1] === ' '){
           result+=str[i].toUpperCase()
        }else{
            result+=str[i]
        }
    }
    return result
} 
capatalize('a im')





