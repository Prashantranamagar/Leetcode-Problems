//function that accepts a positive number N.The function should console.log
//a step shape with N level using the character. Make sure the step has spaxes on the right side.
// Example:
// step(3)  =>  '#  '
//              '## '
//              '###'   


function step(n){
    for(let row =0; row<n; row++){
        let result = ''
        for (let col=0; col<n; col++) {
            if (col<=row){
                result += '#'
            }
            result += ' '
        }
        console.log(result)
    }
}