function minimumWaitingTime(queries) {
    let sorted_q = queries.sort((a, b) => {return a - b})
    console.log(sorted_q);

    let waitingTime = 0;
    queries.forEach((num) =>{
        console.log(num);
    })
    return waitingTime;
}

let queries = [3, 2, 1, 2, 6];
console.log(minimumWaitingTime(queries));