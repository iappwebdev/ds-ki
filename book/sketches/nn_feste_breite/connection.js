"use strict";

class Connection {
  constructor(node1, node2, weight) {
    this.src = node1;
    this.dest = node2;
    this.weight = weight;
    this.animationPct = 0;
  }

  weightedActivation() {
    return this.weight * this.src.activationFunction();
  }

  color() {
    return this.weight > 0 ? "darkseagreen" : "indianred";
  }

  show() {
    const { x: x1, y: y1 } = this.src.location;
    const { x: x2, y: y2 } = this.dest.location;

    push();

    stroke(this.color());
    strokeWeight(abs(this.weight) * 4);
    line(x1, y1, x2, y2);

    textAlign(CENTER, CENTER);
    noStroke();
    fill(0);
    let pt = this.pointAt(0.6);
    text(this.weight, pt.x, pt.y - 10);

    if (this.src.isFiring()) {
      this.animate(this.src.activationFunction());
    }
    pop();
  }

  animate(activation) {
    let pt = this.pointAt(this.animationPct);
    push();
    noStroke();
    fill(this.color());
    circle(pt.x, pt.y, 12);
    fill(0);
    textAlign(CENTER, CENTER);
    text(round(this.weightedActivation(), 2), pt.x, pt.y);
    pop();
    if (buttonAnimate.on) {
      this.animationPct = (this.animationPct + 0.01) % 1;
    }
  }

  pointAt(pct) {
    let dir = p5.Vector.sub(this.dest.location, this.src.location);
    dir.mult(pct);
    return p5.Vector.add(this.src.location, dir);
  }
}
