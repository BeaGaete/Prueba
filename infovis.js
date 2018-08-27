d3.dsv(",", "output.csv", function(d) {
  return {
    prompa: +d.prompa,
    sdpa: +d.sdpa,
    promac: +d.promac,
    sdac: +d.sdac,
    semestreano: d.ano + "-" + d.semestre
  };
}).then(function(data) {
  console.log(data);
  drawChart(data);
});

/**
 * Creates a chart using D3
 * @param {object} data Object containing data
 */
function drawChart(data) {
var svgWidth = 1000, svgHeight = 500; //400 y 600 originalmente
var margin = { top: 20, right: 20, bottom: 30, left: 50 };
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3.select('svg')
    .attr("width", svgWidth)
    .attr("height", svgHeight)
    .attr("class", "svg-container");

var g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var x = d3.scaleBand().rangeRound([0, width]).padding(1)
    //.rangeRoundBands([0,width]);
    //.domain(function(d) { return x(d.semestreano)}) // input
    .domain(data.map(function(d) { return d.semestreano; }))
    //.range([0, width]); // output
    //.rangeRound([0, width]);

var y = d3.scaleLinear()
    .domain([0, 7])
    .rangeRound([height, 0]);

var linePa = d3.line()
    .x(function(d) { return x(d.semestreano)})
    //.y(function(d) { return y(d.prompa)})
    .y(function(d) { return y(d.prompa); })

var lineAc = d3.line()
    .x(function(d) { return x(d.semestreano)})
    //.y(function(d) { return y(d.prompa)})
    .y(function(d) { return y(d.promac); })
    //.curve(d3.curveMonotoneX)
    /*x.domain(d3.extent([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], function(d) { return d.semestreano }));
    y.domain(d3.extent([0, 1, 2, 3, 4, 5, 6, 7], function(d) { return  }));*/
    //x.domain(d3.extent(data, function(d) { return d.semestreano }));
    //y.domain(d3.extent(data, function(d) { return d.prompa }));


g.append("g")
    .attr("transform", "translate(0," + height + ")")
    //.attr("transform", "translate(-16," + height + ")")
    .call(d3.axisBottom(x))
    .append("text")
    .attr("fill", "#000")
    .attr("transform", "rotate(-90)")
    //.select(".domain")
    .attr("y", 900)
    .attr("dy", "0.71em")
    .attr("text-anchor", "start")
    .text("Semestre");
    //.remove();

g.append("g")
    .call(d3.axisLeft(y))
    .append("text")
    .attr("fill", "#000")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", "0.71em")
    .attr("text-anchor", "end")
    .text("Nota");

g.append("path")
    .datum(data)
    .attr("fill", "none")
    .attr("stroke", "#15959F")
    .attr("stroke-linejoin", "round")
    .attr("stroke-linecap", "round")
    .attr("stroke-width", 1.5)
    .attr("d", linePa);

g.append("path")
    .datum(data)
    .attr("fill", "none")
    .attr("stroke", "#F26144")
    .attr("stroke-linejoin", "round")
    .attr("stroke-linecap", "round")
    .attr("stroke-width", 1.5)
    .attr("d", lineAc);

}
