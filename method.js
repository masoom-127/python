// function greet(f,coua)
// {
//     for(let i=0;i<coua;i++)
//         freet()
// }





// // let freet= function() {
// //     console.log("hello")

// // }

// console.log(freet())
// greet(freet,5)
// function factory( request){
//     if(request=="add"){
//     return function(a,b){
//         console.log(a+b);
// };
// }
//     else if(request=="sub"){
//     return function(a,b){
//         console.log(a-b)
//     };
// }

// }

// let request = "add";
// let operation = factory(request);  // factory returns a function
// operation(10, 5);

// arrpw  method map 
// arr = [
//     {
//         name: "ali",
//         roll: 22
//     },
//     {
//         name: "khan",
//         roll: 33
//     },
//     {
//         name: "dj",
//         roll:49
//     }]

// arr.forEach(   (stu) => {
//     console.log(stu.roll)
// });  

// let arr=[22,33,44,5,6,7]
// let p=arr.filter( (n)=>{
// //     return n%2==0

// // });
// // console.log(p)
// saveToDb("apna college", () => { console.log("success: your data was saved"); 
//     saveToDb("hello world", () => { console.log("success2: data2 saved");
//          saveToDb("shradha", () => { console.log("success3: data3 saved"); },
//           () => { console.log("failure3 : weak connection"); }); },
//            () => { console.log("failure2 : weak connection"); 

// //            }); 
// //         });` 


// function f1()
// {
//     console.log("hello f1"); // call back hell it working
// }
// f2( f1())

// function f2()
// {
//     console.log("hello f2");
    

// }


f1( 2, function() { console.log("nor mal")});

function f1(a,fun)
{
    console.log(a,"hello");
    fun();
}