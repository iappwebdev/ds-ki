class Network {
  constructor() {
    this.nodes = {};
    this.inputs = {};
    this.outputs = [];
  }

  node(nodeID) {
    return this.nodes[nodeID];
  }

  printTruthTable() {
    // TODO
  }

  static objectToNN(o) {
    let nn = new Network();
    for (const { id, bias, x, y } of o.nodes) {
      nn.nodes[id] = new Node(x, y, bias);
    }
    for (const { src, dest, weight } of o.connections) {
      const srcNode = nn.node(src);
      const destNode = nn.node(dest);
      srcNode.connectWith(destNode, weight);
    }
    for (const [id, activation] of Object.entries(o.inputs)) {
      const node = nn.node(id);
      node.setActivation(activation);
    }
    return nn;
  }
}
