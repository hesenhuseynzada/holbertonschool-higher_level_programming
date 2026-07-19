const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  // Convert all arguments to numbers
  const numbers = args.map(Number);
  
  // Filter out duplicates and sort descending
  const uniqueSorted = [...new Set(numbers)].sort((a, b) => b - a);

  if (uniqueSorted.length < 2) {
    console.log(0);
  } else {
    console.log(uniqueSorted[1]);
  }
}