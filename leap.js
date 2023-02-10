let year;

const isLeapYear = (year) => {
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    return true;
  } else {
    return false;
  }
};

year = window.prompt("Enter a year: ");

if (isLeapYear(year)) {
  console.log(year + " is a leap year.");
} else {
  console.log(year + " is not a leap year.");
}
