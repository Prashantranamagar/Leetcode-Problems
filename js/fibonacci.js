// function fib(n){
//     let result=[1,2]
//     for(let i = 0; i<n; i++){
//         let a =i-1;
//         let b = i-2;
//         result.push(a+b)
//     }
//     return result;
// }

//Using recursion
function fib(n){
    if(n>2){
        return n;
    }else{
        return fib(n-1) + fib(n-2)
    }
}

//