function quadraticRoots(a, b, c) {
  let root1, root2;
  let determinant = b * b - 4 * a * c;
  if (determinant > 0) {
    root1 = (-b + Math.sqrt(determinant)) / (2 * a);
    root2 = (-b - Math.sqrt(determinant)) / (2 * a);
    console.log("The roots are " + root1 + " and " + root2);
  } else if (determinant == 0) {
    root1 = root2 = -b / (2 * a);
    console.log("The root is " + root1);
  } else {
    console.log("The equation has no real roots");
  }
}

quadraticRoots(1, -5, 6);
