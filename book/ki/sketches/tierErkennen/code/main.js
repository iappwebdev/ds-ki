let knn;
let zeigeKlassifizierung;
let datenpunktA;

function preload() {
  GUI.ladeSprites();
}

function setup() {
  textAlign(LEFT);
  knn = new KNN(datenpunkte);
  GUI.erzeugeGUI();
  GUI.zeichneDatenpunkte(knn.datenpunkte);
  zeigeKlassifizierung = false;
}

function draw() {
  background(220);
  GUI.zeichneDatenpunkte(knn.datenpunkte);

  if (zeigeKlassifizierung) {
    const k = GUI.kWaehler.value();
    const nachbarn = knn.nachbarn(datenpunktA, k);
    knn.klassifiziere(datenpunktA, k);
    GUI.zeichneNachbarschaft(datenpunktA, nachbarn);
    GUI.zeichneDatenpunkte(knn.datenpunkte);
  } else {
    let datenpunkt = GUI.mausPositionZuDatenpunkt();
    let x = mouseX;
    let y = mouseY;
    push();
    fill(0);
    noStroke(0);
    textAlign(LEFT);
    textSize(12);
    strokeWeight(1);
    text("niedlichkeit:  " + nf(datenpunkt.niedlichkeit, 1, 2), x + 30, y - 10);
    text(
      "flauschigkeit: " + nf(datenpunkt.flauschigkeit, 1, 2),
      x + 30,
      y + 10
    );
    pop();
    circle(x, y, 10);
  }
}

function mousePressed() {
  if (GUI.mausIstImSpielfeld()) {
    zeigeKlassifizierung = !zeigeKlassifizierung;
    if (zeigeKlassifizierung) {
      datenpunktA = GUI.mausPositionZuDatenpunkt();
    }
  }
}
