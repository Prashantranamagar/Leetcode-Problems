//two step pyramid
// n = 3  =>  '  #  '
//            ' ### '
//            '#####' 

//mid = n-1
//row = 3
//col = 2*n-1
//conditin if (mid-row<=col && mid+row>=col){ level = level+'#' || level+' '}



function pyramid(n){
    let mid = n-1
    for(let row = 0; row<n; row++){
        let result = ''
        for(let col = 0; col<2*n-1; col++){
            if(mid-row<=col && mid+row>=col){
                result+='#'
            }else{
                result += ' '
            }
        }
        console.log(result)
    }
}


pyramid(3)