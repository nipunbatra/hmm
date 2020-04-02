 function create_node(id, x, y,){

    return {id: 'n' + id,
    label: 'Node ' + id,
    x: x,
    y: y,
    size: 50,
    color: '#666'}
 }


function create_edge(edge_id, node_1, node_2, curvetype='curvedArrow'){

    return {
    id: 'e'+edge_id,
    source: 'n'+node_1 ,
    target: 'n'+node_2 ,
    size: 5,
    type: curvetype,
    color: '#ccc'
  }
 }
 

// cubic helper formula at percent distance
function CubicN(pct, a,b,c,d) {
    var t2 = pct * pct;
    var t3 = t2 * pct;
    return a + (-a * 3 + pct * (3 * a - a * pct)) * pct
    + (3 * b + pct * (-6 * b + b * 3 * pct)) * pct
    + (c * 3 - c * 3 * pct) * t2
    + d * t3;
}


 function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}



function getQuadraticBezierXYatPercent(startPt, controlPt, endPt, percent) {
    var x = Math.pow(1 - percent, 2) * startPt.x + 2 * (1 - percent) * percent * controlPt.x + Math.pow(percent, 2) * endPt.x;
    var y = Math.pow(1 - percent, 2) * startPt.y + 2 * (1 - percent) * percent * controlPt.y + Math.pow(percent, 2) * endPt.y;
    return ({
        x: x,
        y: y
    });
}

// cubic bezier percent is 0-1
function getCubicBezierXYatPercent(startPt, controlPt1, controlPt2, endPt, percent) {
    var x = CubicN(percent, startPt.x, controlPt1.x, controlPt2.x, endPt.x);
    var y = CubicN(percent, startPt.y, controlPt1.y, controlPt2.y, endPt.y);
    return ({
        x: x,
        y: y
    });
}