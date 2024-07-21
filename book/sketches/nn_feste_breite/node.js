class Node {
  constructor(x, y, bias = 0.1) {
    this.location = createVector(x, y);
    this.radius = 15;
    this.bias = bias;
    this.inputCons = [];
    this.successorCons = [];
    this.activation = 0;
  }

  show() {
    push();
    fill(0);
    noStroke();
    let { x, y } = this.location;
    if (this.activationFunction() > 0) {
      fill("darkgreen");
    } else {
      fill(0);
    }
    ellipseMode(RADIUS);
    circle(x, y, this.radius);

    textAlign(CENTER, CENTER);
    fill(255);
    //text(round(this.activationFunction(), 3), x, y);
    text(round(this.activation, 3), x, y);

    if (!this.isInputNode()) {
      fill(0);
      strokeWeight(0.5);
      textSize(8);
      text(round(this.bias, 1), x, y - 20);
    }

    pop();
  }

  isInputNode() {
    return this.inputCons.length == 0;
  }

  connectWith(other, weight) {
    let con = new Connection(this, other, weight);
    this.successorCons.push(con);
    other.inputCons.push(con);
  }

  setActivation(newAct) {
    this.activation = newAct;
    this.recomputeActivation();
  }

  toggleActivation() {
    this.setActivation(this.activation == 1 ? 0 : 1);
  }

  recomputeActivation() {
    if (!this.isInputNode()) {
      const weightedInputs = this.inputCons.map((c) => c.weightedActivation());
      let sum = 0;
      for (const wi of weightedInputs) sum += wi;
      // this.activation = this.activationFunction(sum)
      this.activation = sum;
    }
    for (const con of this.successorCons) {
      con.dest.recomputeActivation();
    }
    return this.activation;
  }

  activationFunction() {
    // Achtung HACK!!!
    if (this.isInputNode()) return this.activation;

    if (this.activation >= this.bias) return 1;
    else return 0;
  }

  isFiring() {
    return this.activationFunction() > 0;
  }

  isUnderMouse() {
    let { x, y } = this.location;
    let [mx, my] = [mouseX / scaleFactor, mouseY / scaleFactor];
    return dist(x, y, mx, my) < this.radius;
  }
}
