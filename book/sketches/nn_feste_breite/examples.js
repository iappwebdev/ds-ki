NN_EXAMPLES = [
  
  {
    // OR
    name: "Beispiel 0",
    nodes: [
      { id: "in1", bias: 0.5, x: 100, y: 100 },
      { id: "in2", bias: 0.5, x: 100, y: 300 },
      { id: "out", bias: 0.1, x: 300, y: 200 },
    ],
    connections: [
      { src: "in1", dest: "out", weight: 0.2 },
      { src: "in2", dest: "out", weight: 0.4 },
    ],
    inputs: { in1: 0, in2: 0 },
  },

  {
    // AND
    name: "Beispiel 1",
    nodes: [
      { id: "in1", bias: 0.5, x: 100, y: 100 },
      { id: "in2", bias: 0.5, x: 100, y: 300 },
      { id: "out", bias: 0.75 , x: 300, y: 200 },
    ],
    connections: [
      { src: "in1", dest: "out", weight: 0.5 },
      { src: "in2", dest: "out", weight: 0.5 },
    ],
    inputs: { in1: 0, in2: 1 },
  },

  {
    // Bsp aus Jupyter-Notebook Perzeptron
    name: "Beispiel 2",
    nodes: [
      { id: "in1", bias: 0, x: 100, y: 100 },
      { id: "in2", bias: 0, x: 100, y: 300 },
      { id: "out", bias: 0, x: 300, y: 200 },
    ],
    connections: [
      { src: "in1", dest: "out", weight: 0.2 },
      { src: "in2", dest: "out", weight: -0.8 },
    ],
    inputs: { in1: 0.1, in2: 0.2 },
  },

  {
    // XOR
    name: "Beispiel 3",
    nodes: [
      { id: "in1", bias: 0.5, x: 100, y: 100 },
      { id: "in2", bias: 0.5, x: 100, y: 300 },
      { id: "h1", bias: 1, x: 200, y: 100 },
      { id: "h2", bias: -1, x: 200, y: 300 },
      { id: "out", bias: 2, x: 300, y: 200 },
    ],
    connections: [
      { src: "in1", dest: "h1", weight: 1 },
      { src: "in2", dest: "h1", weight: 1 },
      { src: "in1", dest: "h2", weight: -1 },
      { src: "in2", dest: "h2", weight: -1 },
      { src: "h1", dest: "out", weight: 1 },
      { src: "h2", dest: "out", weight: 1 },
    ],
    inputs: { in1: 0, in2: 1 },
  },

  {
    // XOR again... but different
    name: "Beispiel 4",
    nodes: [
      { id: "in1", bias: 1, x: 100, y: 150 },
      { id: "in2", bias: 1, x: 100, y: 250 },
      { id: "h1", bias: 1, x: 200, y: 100 },
      { id: "h2", bias: 2, x: 200, y: 200 },
      { id: "h3", bias: 1, x: 200, y: 300 },
      { id: "out", bias: 0.8, x: 300, y: 200 },
    ],
    connections: [
      { src: "in1", dest: "h1", weight: 1 },
      { src: "in1", dest: "h2", weight: 1 },
      { src: "in2", dest: "h2", weight: 1 },
      { src: "in2", dest: "h3", weight: 1 },
      { src: "h1", dest: "out", weight: 1 },
      { src: "h2", dest: "out", weight: -2 },
      { src: "h3", dest: "out", weight: 1 },
    ],
    inputs: { in1: 1, in2: 1 },
  },
  
  {
    // NAND
    name: "Beispiel 5",
    nodes: [
      { id: "in1", bias: 0.5, x: 100, y: 100 },
      { id: "in2", bias: 0.5, x: 100, y: 300 },
      { id: "out", bias: -1.5, x: 300, y: 200 },
    ],
    connections: [
      { src: "in1", dest: "out", weight: -1 },
      { src: "in2", dest: "out", weight: -1 },
    ],
    inputs: { in1: 0, in2: 0 },
  },



];
