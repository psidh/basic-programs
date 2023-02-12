const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout
});

const calculateMarks = () => {
  readline.question("Enter marks in Maths: ", maths => {
    readline.question("Enter marks in Science: ", science => {
      readline.question("Enter marks in English: ", english => {
        const total = parseFloat(maths) + parseFloat(science) + parseFloat(english);
        const average = total / 3;
        const percentage = (total / 300) * 100;

        console.log(`Total marks: ${total}`);
        console.log(`Average marks: ${average}`);
        console.log(`Percentage: ${percentage}`);

        readline.close();
      });
    });
  });
};

calculateMarks();
