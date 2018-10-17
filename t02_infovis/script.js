// Para más referencia respecto a los métodos utilizados:
// https://github.com/d3/d3-force#simulation_alpha

const WIDTH = 800; //1500
const HEIGHT = 600; //700
const MARGIN = { TOP: 20, BOTTOM: 20, LEFT: 20, RIGHT: 20 }; // 40 40 50 50

const width = WIDTH - MARGIN.RIGHT - MARGIN.LEFT;
const height = HEIGHT - MARGIN.TOP - MARGIN.BOTTOM;

const FILEPATH = 'dataset.json';

const container = d3.select('#container')
  .append('svg')
    .attr('width', WIDTH)
    .attr('height', HEIGHT)
  .append('g')
    .attr('transform',
        `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);



const ticked = () => {
// Cada tick aumenta el alpha en (alphaTarget - alpha) × alphaDecay
// alpha = alpha + (alphaTarget - alpha) × alphaDecay
// alphaTarget parte como 0, alpha como 1 y alphaDecay como 0.0228
// Los ticks acaban cuando alpha es menor a una cota. Por defecto esa cota es  0.001



container.selectAll('.node')
    .attr('transform', node => `translate(${node.x}, ${node.y})`);

    container.selectAll('line')
             .attr('x1', link => link.source.x)
             .attr('y1', link => link.source.y)
             .attr('x2', link => link.target.x)
             .attr('y2', link => link.target.y);
};

const simulation = d3.forceSimulation()
                     .force('center', d3.forceCenter(width/3, height/2)) // partido por 2
                     .force('collision', d3.forceCollide(20))
                     .force('charge', d3.forceManyBody().strength(-350)) //-500, -350 para que no se esparramen
                     .force('link', d3.forceLink().id(node => node.name));


d3.json(FILEPATH).then(dataset => {
    simulation.nodes(dataset.nodes)
              .on('tick', ticked)
              .force('link')
              .links(dataset.links)
              .distance(50); //80

    container.append("container:defs")
              .append("container:marker")
              .attr("id", "arrow")
              .attr("viewBox", "0 -5 10 10")
              .attr("refX", 24) // 15 mientras menos se acerca al circulo 24
              .attr("refY", -1.5) //-1.5  -1.5
              .attr("markerWidth", 3) //6
              .attr("markerHeight", 3) //6
              .attr("orient", "auto")
              .append("path")
              .attr("d", "M0,-5L10,0L0,5") // -5 -> -10 "M0,-5L10,0L0,5" "d", "M 0 -5 10 10" 'M 0,-5 L 10 ,0 L 0,5'
              //.attr("d", "M 0 -5 10 10")
              .style("stroke", "black");

    container.selectAll('line')
             .data(dataset.links)
             .enter()
             .append('line')
             .attr('x1', link => link.target.x)
             .attr('y1', link => link.target.y)
             .attr('x2', link => link.source.x)
             .attr('y2', link => link.source.y)
             .attr("marker-start", "url(#arrow)");




    const nodes = container.selectAll('.node')
                           .data(dataset.nodes)
                           .enter()
                           .append('g')
                           .attr('class', 'node')
                           .call(d3.drag()
                            .on("start", dragstarted)
                            .on("drag", dragged)
                            .on("end", dragended));

    nodes.append('circle').attr('r', 15);

    nodes.append('text').text(node => node.name).attr('dy', 5);



    /*function mouseOver(opacity) {
        return function(d) {
            // check all other nodes to see if they're connected
            // to this one. if so, keep the opacity at 1, otherwise
            // fade
            node.style("stroke-opacity", function(o) {
                thisOpacity = isConnected(d, o) ? 1 : opacity;
                return thisOpacity;
            });
            node.style("fill-opacity", function(o) {
                thisOpacity = isConnected(d, o) ? 1 : opacity;
                return thisOpacity;
            });
            // also style link accordingly
            link.style("stroke-opacity", function(o) {
                return o.source === d || o.target === d ? 1 : opacity;
            });
            link.style("stroke", function(o){
                return o.source === d || o.target === d ? o.source.colour : "#ddd";
            });
        };
    }*/
    nodes.on("mouseover", focus).on("mouseout", unfocus);

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

    /*nodes.on('mouseover', (d, i , all) =>{
        // Buscamos todos los circulos que no son el donde está el mouse
        console.log(d)
        console.log(d.x, d.y)
        console.log(d3.selectAll('line')._groups[0]) // ._groups[0][0].x1
        d3.selectAll('circle').filter(circle => circle != d).style("opacity", 0.3)
        d3.selectAll('text').filter(text => text != d).style("opacity", 0.3)
        d3.selectAll('line')._groups[0].filter(line => line.x1 != d.x && line.y1 != d.y).style("opacity", 0.3)

        // Seleccionamos nuestro circulo y le cambiamos el radio.
        d3.select(all[i]).transition().attr('r', 20);
    });

    nodes.on('mouseout', (_, i, all) =>{
        d3.select(all[i]).transition().attr('r', 10);
        d3.selectAll('circle').style("opacity", 1)
        d3.selectAll('text').style("opacity", 1)
        d3.selectAll('line').style("opacity", 1)
    });*/
});

const dragstarted = (node) => {
  // d3.event.active es usado para detectar el primer evento y el último;
  // Esto es cero cuando el primer drag empieza y cero cuando el último drag termina.
  if (!d3.event.active) {
    // Cambiar el alphaTarget hace que el alpha aumente y la simulación vuelva a tomar accción
    // .restart para que se vuelvan a ejecutar los ticks.
    simulation.alphaTarget(0.3).restart();
  };
  node.fx = node.x;
  node.fy = node.y;
  // fx y fy se pueden considerar como las posiciones absolutas. Cuando no son nulas
  // obliga a que la posicion X, Y sea igual a fx, fy y la velocidad para moverse
  // en la simulación sea 0
}

const dragged = (node) => {
  node.fx = d3.event.x;
  node.fy = d3.event.y;
}

const dragended = (node) => {
  if (!d3.event.active) {
    // Cambiar el alphaTarget a 0 hace que el alpha comience a disminuir y así la simulación puede acabar
    simulation.alphaTarget(0.0);
  }
  node.fx = null;
  node.fy = null;
  // Indicamos que las posiciones absolutas sean nulas para que la simulación pueda alterar las velocidades
  // y posiciones X, Y
}
