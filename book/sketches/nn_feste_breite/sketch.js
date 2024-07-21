const WINDOWSIZE = -1; // verwenden, wenn Canvas auf Fenstergröße skaliert werden soll

let nn;
let buttonAnimate;
let exampleSelector;

let scaling = 0.9;
let originalHeight = 400;
let scaleFactor;

//let SIZE = WINDOWSIZE;   // Canvas auf Fenstergröße skalieren
let SIZE = 400; // Test mit fester Breite

function setup() {
  if (SIZE < 0) SIZE = windowWidth;
  createCanvas(SIZE, SIZE);

  buttonAnimate = createButton("Animation an/aus");
  buttonAnimate.on = true;
  buttonAnimate.mousePressed((_) => (buttonAnimate.on = !buttonAnimate.on));

  exampleSelector = createSelect();
  for (let ex of NN_EXAMPLES) {
    exampleSelector.option(ex.name);
  }
  exampleSelector.changed(selectionChanged);
  selectionChanged();

  changeNN("Beispiel 4"); // setzt ein bestimmtes Bsp als Start
}

function selectionChanged() {
  let item = exampleSelector.value();
  changeNN(item);
}

function changeNN(item) {
  nnDefinition = NN_EXAMPLES.find((net) => net.name === item);
  if (nnDefinition === undefined) selectionChanged();
  nn = Network.objectToNN(nnDefinition);
}

function draw() {
  scaleWindow();
  background(255);

  text(
    "Klicke die Input-Neuronen auf der linken Seite an! Was passiert?",
    20,
    50
  );
  for (const id in nn.nodes) {
    const node = nn.nodes[id];
    for (const con of node.successorCons) {
      con.show();
    }
    node.show();
  }
  text("Welche logische Schaltung simuliert dieses neuronale Netz?", 20, 350);
}

function mousePressed() {
  for (const node of Object.values(nn.nodes)) {
    if (node.isUnderMouse()) {
      node.toggleActivation();
    }
  }
}

function scaleWindow() {
  resizeCanvas(scaling * SIZE, scaling * SIZE);
  scaleFactor = (scaling * SIZE) / originalHeight;
  scale(scaleFactor, scaleFactor);
}
