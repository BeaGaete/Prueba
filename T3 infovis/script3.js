
//var parseDate = d3.timeParse("%b %Y");

//var x = d3.scaleTime()
    //.range([0, width]);

var margin = {top: 8, right: 10, bottom: 2, left: 10},
    width = 960 - margin.left - margin.right,
    height = 69 - margin.top - margin.bottom;

var x = d3.scaleBand().rangeRound([0, width]);

d3.dsv(",", "TheLordOfTheRing.csv", function(d) {
  return {
  	film: d.Film,
    chapter: d.Chapter,
    character: d.Character,
    race: d.Race,
    words: parseInt(d.Words),
    numfilm: d.story.split("-")[0],
    cap: d.story.split("-")[1]
};
}).then(function(data) {


	var symbols = d3.nest()
	      .key(function(d) { return d.character; })
	      .entries(data);

	console.log(symbol.values[0].cap);

	  x.domain([
	    d3.min(symbols, function(symbol) { return symbol.values[0].cap; }),
	    d3.max(symbols, function(symbol) { return symbol.values[symbol.values.length - 1].cap; })
	  ]);

	  var svg = d3.select("body").selectAll("svg")
	      .data(symbols)
	    .enter().append("svg")
	      .attr("width", width + margin.left + margin.right)
	      .attr("height", height + margin.top + margin.bottom)
	    .append("g")
	      .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
	      .each(multiple);

	  // aparecn los nokbres de los personajes a cada lado del small
	  svg.append("text")
	      .attr("x", width - 120)
	      .attr("y", height - 6)
	      .text(function(d) { return d.key; });

	function multiple(symbol) {
		  var svg = d3.select(this);

		  var y = d3.scaleLinear()
		      .domain([0, d3.max(symbol.values, function(d) { return d.words; })])
		      .range([height, 0]);

		  var area = d3.area()
		      .x(function(d) { return x(d.cap); })
		      .y0(height)
		      .y1(function(d) { return y(d.words); });

		  var line = d3.line()
		      .x(function(d) { return x(d.cap); })
		      .y(function(d) { return y(d.words); });

		  svg.append("path")
		      .attr("class", "area")
		      .attr("d", area(symbol.values));

		  svg.append("path")
		      .attr("class", "line")
		      .attr("d", line(symbol.values));
	}

});