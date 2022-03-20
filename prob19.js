// https://projecteuler.net/problem=19
// Completed 3/20/2022

let numOfSundays = 0;

let daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
// First day of 1901 was a Tuesday
let daysOfWeekIndex = 1;


for(let year = 1901; year <= 2000; year++){
    for(let month = 1; month <= 12; month++){

        if(month === 2){
            if(daysOfWeek[daysOfWeekIndex] === 'Sunday'){
                numOfSundays++;
            }
            // Checks if it is a leap year
            if(year % 4 === 0){
                // Adds rest of days of the month since only first is looked at (applied to rest of months)
                daysOfWeekIndex += 29
                daysOfWeekIndex %= 7;
                }else{
                daysOfWeekIndex += 28
                daysOfWeekIndex %= 7;
                }
        } else if(month === 1 || month === 3 || month === 5 || month === 7 || month === 8 || month === 10 || month === 12){
            if(daysOfWeek[daysOfWeekIndex] === 'Sunday'){
                numOfSundays++;
            }
            daysOfWeekIndex += 31
            daysOfWeekIndex %= 7;
        } else {
            if(daysOfWeek[daysOfWeekIndex] === 'Sunday'){
                numOfSundays++;
            }
            daysOfWeekIndex += 30
            daysOfWeekIndex %= 7;
        }
    }
}

console.log(numOfSundays)