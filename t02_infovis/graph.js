
var width = 800; //700
var height = 600; // 600
//var color = d3.scaleOrdinal(d3.schemeCategory10);
/*var color = d3.scaleSequential()
        .domain([0, 59])
        .interpolator(d3.interpolateOranges);
        .interpolateRgb(a, b)*/
var color = d3.scaleLinear()
        .domain([0, 59])
        .range(['#ffffff', '#fd8d3c'])  // #FD8D3C  #a80e06
        .interpolate(d3.interpolateHsl()); // interpolateHsl interpolateRgb */

/*var color = d3.scaleLinear()
        .domain([0, 59])
        .range(['#ffffff', '#FD8D3C'])  // naranjo #FD8D3C   rojo #a80e06
        .interpolate(d3.interpolateLab); // interpolateHsl interpolateRgb */





d3.json("dataset.json").then(function(graph) {

var label = {
    'nodes': [],
    'links': []
};

graph.nodes.forEach(function(d, i) {
    label.nodes.push({node: d});
    label.nodes.push({node: d});
    label.links.push({
        source: i * 2,
        target: i * 2 + 1
    });
});

var labelLayout = d3.forceSimulation(label.nodes)
    .force("charge", d3.forceManyBody().strength(-50))
    .force("link", d3.forceLink(label.links).distance(0).strength(2));

var graphLayout = d3.forceSimulation(graph.nodes)
    .force("charge", d3.forceManyBody().strength(-2200))
    .force("center", d3.forceCenter((width / 2) + 40, (height / 2) + 30))  // + 40 y -70
    .force("x", d3.forceX(width / 2).strength(1))   // d3.forceX(width / 2).strength(1)
    .force("y", d3.forceY(height / 2).strength(1))  // d3.forceY(height / 2).strength(1)
    .force("link", d3.forceLink(graph.links).id(function(d) {return d.name; }).distance(50).strength(1))
    .on("tick", ticked);

var adjlist = [];


graph.links.forEach(function(d) {
    adjlist[d.source.index + "-" + d.target.index] = true;
    adjlist[d.target.index + "-" + d.source.index] = true;
});



function neigh(a, b) {
    return a == b || adjlist[a + "-" + b];
}

function colorLink(l){
  if(l == false){
    //console.log(l)
    return "#aaa";
  }else{
    return "#305473";
  }
}


var svg = d3.select("#viz").attr("width", width).attr("height", height);
var container = svg.append("g");

container.append("container:defs")
          .append("container:marker")
          .attr("id", "arrow")
          .attr("viewBox", "0 -5 10 10")
          .attr("refX", 20) // 15 mientras menos se acerca al circulo 24
          .attr("refY", 0) //-1.5
          .attr("markerWidth", 3) //6
          .attr("markerHeight", 3) //6
          .attr("orient", "auto-start-reverse")
          .append("path")
          .attr("d", "M0,-5L10,0L0,5") // -5 -> -10 "M0,-5L10,0L0,5" "d", "M 0 -5 10 10" 'M 0,-5 L 10 ,0 L 0,5'
          //.attr("d", "M 0 -5 10 10")
          .style("fill", "#9ECAE1");

/*svg.call(
    d3.zoom()
        .scaleExtent([.1, 4])
        .on("zoom", function() { container.attr("transform", d3.event.transform); })
);*/

var link = container.append("g") //.attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter()
    .append("line")
    .attr("stroke-width", "4px")
    .attr("marker-start", "url(#arrow)")
    .attr("stroke", function(d) { return d.dev == false ? "#9ECAE1" : "#126bbf"; }); // si es false #9ECAE1, true "#305473"


var node = container.append("g")
    .selectAll("g")
    .data(graph.nodes)
    .enter()
    .append("circle") // en el css fill: #FD8D3C;
    .attr("r", 10)  // era 10 function(d) { return Math.log(d.forks) * 4; })
    //.attr("fill", FD8D3C)
    .attr('class', 'node')
    .attr('class', 'inactive ball')  // color activo en css #fill: #de7701;
    .attr("fill", function(d) { return color(Math.log(d.forks) * 10); });  // d3plus.color.lighter(d,mod)  { return color(Math.log(d.forks) * 5); }

const originx = node.x;
const originy = node.y;

node.on("mouseover", focus).on("mouseout", unfocus);



node.call(
    d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended)
);

// cuando se hace click en el nodo
node.on('click', returnPosition);

node.on('dblclick', (d) =>{
        let count = 0;
        var cir = d3.selectAll('.inactive').filter(circle => circle == d);
        var index = d3.select(d3.event.target).datum().index;

        if (cir.size()){
            cir.attr('class', 'active')
            .attr("fill", function(d) { return color(Math.log(d.forks) * 10); })
            actualizarBarchart(d, d.name, d)
            console.log(index)
            link.each(function(o, i) {
              if (o.target.index == index){
                //console.log(o.target.stars, o.target.name)
                //console.log(o.source.stars, o.source.name)
                actualizarBarchart(o.source, o.source.name, d)
              }if(o.source.index == index){
                  actualizarBarchart(o.target, o.target.name, d)
                  //console.log(o.source.stars, o.source.name)
              }
            })
        }

      });

var labelNode = container.append("g") //.attr("class", "labelNodes")
    .selectAll("text")
    .data(label.nodes)
    .enter()
    .append("text")
    .text(function(d, i) { return i % 2 == 0 ? "" : d.node.name + " # " + d.node.forks; })
    .style("fill", "#555")
    .style("font-family", "Arial")
    .style("font-size", 12)
    .style("pointer-events", "none"); // to prevent mouseover/drag capture

labelNode.each(function(d, i) {
        if(i % 2 == 0) {
            const originx = d.node.x;
            const originy = d.node.y;
        }
        });

node.on("mouseover", focus).on("mouseout", unfocus);

// cuando se hace click en el botón
d3.select('#clear').on('click', (_) =>{
        clear();
        d3.selectAll('circle').attr('class', 'inactive ball');
        //d3.selectAll('circle').remove();
    });

function ticked() {

    node.call(updateNode);
    link.call(updateLink);

    labelLayout.alphaTarget(0.3).restart();
    labelNode.each(function(d, i) {
        if(i % 2 == 0) {
            d.x = d.node.x;
            d.y = d.node.y;
        } else {
            //var b = this.getBBox();
            //console.log(b);
            var diffX = d.x - d.node.x;
            var diffY = d.y - d.node.y;

            var dist = Math.sqrt(diffX * diffX + diffY * diffY);

            var shiftX =  30 * (diffX - dist) / (dist * 2); // b.width
            shiftX = Math.max(-30, Math.min(0, shiftX)); // b.width
            var shiftY = 16; // 16
            this.setAttribute("transform", "translate(" + shiftX + "," + shiftY + ")");
        }
    });
    labelNode.call(updateNode);

}

function fixna(x) {
    if (isFinite(x)) return x;
    return 0;
}

function focus(d) {
    var index = d3.select(d3.event.target).datum().index;
    node.style("opacity", function(o) {
        return neigh(index, o.index) ? 1 : 0.1;
    });
    labelNode.attr("display", function(o) {
      return neigh(index, o.node.index) ? "block": "none";
    });
    link.style("opacity", function(o) {
        return o.source.index == index || o.target.index == index ? 1 : 0.1;
    });
}

function unfocus() {
   labelNode.attr("display", "block");
   node.style("opacity", 1);
   link.style("opacity", 1);
}

function returnPosition(d) {
    console.log(d.fx);
    console.log(d.fy);
    d.fx = originx;
    d.fy = originy;
    console.log("hice click");
    
    
}

function updateLink(link) {
    link.attr("x1", function(d) { return fixna(d.source.x); })
        .attr("y1", function(d) { return fixna(d.source.y); })
        .attr("x2", function(d) { return fixna(d.target.x); })
        .attr("y2", function(d) { return fixna(d.target.y); });
}

function updateNode(node) {
    node.attr("transform", function(d) {
        return "translate(" + fixna(d.x) + "," + fixna(d.y) + ")";
    });
}

function dragstarted(d) {
    //d3.select(this).classed("fixed", d.fixed = true);
    d3.event.sourceEvent.stopPropagation();
    if (!d3.event.active) graphLayout.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(d) {
  if(d.fx > 750){
    d.fx = 700;
  }else if (d.fx < 100) {
    d.fx = 100;
  }else{
    d.fx = d3.event.x;
  }
  if(d.fy > 550){
    d.fy = 500;
  }else if (d.fy < 40) {
    d.fy = 40;
  }else{
    d.fy = d3.event.y;
  }
}

function dragended(d) {
    if (!d3.event.active) graphLayout.alphaTarget(0);
    if(d.fx > 750){
        d.fx = 700;
      }else if (d.fx < 100) {
        d.fx = 100;
      }else{
        d.fx = d3.event.x;
      }
      if(d.fy > 550){
        d.fy = 500;
      }else if (d.fy < 40) {
        d.fy = 40;
      }else{
        d.fy = d3.event.y;
      }


    
      // NULL
    //console.log(d.y, d.fy);
}

}); // d3.json
