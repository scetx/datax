// create an array with nodes
// changes color when node is clicked, indicating infection
var nodes = new vis.DataSet([
    { id: 1, label: "Router/Firewall", shape: "database", color:{highlight:{background:"pink"}}},
    { id: 2, label: "Hub 1", shape: "box", color:{highlight:{background:"pink"}}},
    { id: 3, label: "Hub 2", shape: "box", color:{highlight:{background:"pink"}} },
    { id: 4, label: "Hub 3", shape: "box", color:{highlight:{background:"pink"}} },
    { id: 5, label: "Computer 1", color:{highlight:{background:"pink"}} },
    { id: 6, label: "Computer 2", color:{highlight:{background:"pink"}} },
    { id: 7, label: "Computer 3", color:{highlight:{background:"pink"}} },
    { id: 9, label: "Computer 4", color:{highlight:{background:"pink"}} },
    { id: 10, label: "Computer 5", color:{highlight:{background:"pink"}} },
    { id: 11, label: "Computer 6", color:{highlight:{background:"pink"}} },
    { id: 12, label: "Computer 7", color:{highlight:{background:"pink"}} },
    ]);

// create an array with edges
var edges = new vis.DataSet([
    { from: 2, to: 1 },
    { from: 3, to: 1 },
    { from: 4, to: 1 },
    { from: 5, to: 2 },
    { from: 6, to: 2 },
    { from: 7, to: 3 },
    { from: 8, to: 3 },
    { from: 10, to: 4 },
    { from: 11, to: 4 },
    { from: 12, to: 4 },
    { from: 9, to: 3 },
    ]);

          
// create a network
var container = document.getElementById("mynetwork");
var data = {
    nodes: nodes,
    edges: edges,
};

var options = {};

var network = new vis.Network(container, data, options);
