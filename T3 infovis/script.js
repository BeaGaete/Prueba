d3.dsv(",", "TheLordOfTheRing.csv", function(d) {
  return {
    film: d.Film,
    chapter: d.Chapter,
    character: d.Character,
    race: d.Race,
    words: parseInt(d.Words),
    numfilm: d.story.split("-")[0],
    cap: +d.story.split("-")[1]
  };
}).then((data) => {
    var nested = d3.nest()
      .key(k => k.character)
      .entries(data);

    console.log(nested);
    console.log(nested[0].key);
    console.log(nested[0].values[0].words);

    //onchange();
    

    var margin = {top: 8, right: 10, bottom: 2, left: 10},
    width = 125 - margin.left - margin.right,
    height = 100 - margin.top - margin.bottom;

    /*var opciones = ["film 1", "film 2", "film 3"];

    var select = d3.select('body')
      .append('select')
        .attr('class','select')
        .on('change',onchange)

    var options = select
      .selectAll('option')
      .data(opciones).enter()
      .append('option')
        .text(function (d) { return d; });*/
    


      /*x.domain([
    d3.min(nested, function(symbol) { return symbol.values[0].cap; }),
    d3.max(nested, function(symbol) { return symbol.values[symbol.values.length - 1].cap; })
  ]);*/

    var svg = d3.select("body").selectAll("svg")
        .data(nested)
      .enter().append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      //.append("g")
        //.attr("transform", "translate(" + margin.left + "," + margin.top + ")")
        .each(multiple);

    
  

    function multiple(symbol) {
      var svg = d3.select(this);

      var x = d3.scaleLinear() //d3.scaleBand()
          .range([0, width])
          //.rangeRound([0, width])
          //.domain(nested.map(function(d) { return d.values[0].cap; }));
          .domain([0, d3.max(symbol.values, function(d) { return d.cap; })])

      var y = d3.scaleLinear()
          .domain([0, d3.max(symbol.values, function(d) { return d.words; })])
          .range([height, 0]);

      /*var area = d3.area()
          .x(function(d) { return x(d.cap); })
          .y0(height)
          .y1(function(d) { return y(d.words); });*/

      var line = d3.line()
          .x(function(d) { return x(d.cap); })
          .y(function(d) { return y(d.words); });

      /*svg.append("path")
          .call(d3.axisBottom(x))
          .attr("class", "area")
          .attr("d", area(symbol.values));*/

      /*svg.append("path")
          .attr("class", "line")
          .attr("fill", "none")
          .attr("d", line(symbol.values));*/

      svg.append("text")
          .attr("x", width + 12)
          .attr("y", height + 8)
          .attr("fill", "#F26144")
          .text(function(d) { return d.key; });

      const g = svg.append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")")


      g.append("g")
          .attr("transform", "translate(0," + height + ")")
          //.call(d3.axisBottom(x))
          .append("text")
          .attr("fill", "#F26144") // .attr("fill", "#F26144")
          .attr("transform", "rotate(0)")
          .attr("y", height)
          .attr("dx", "0.71em")
          .attr("text-anchor", "start");

      g.append("path")
          .datum(symbol.values)
          .attr("fill", "none")
          .attr("stroke", "#15959F")
          .attr("stroke-linejoin", "round")
          .attr("stroke-linecap", "round")
          .attr("stroke-width", 1.5)
          .attr("d", line);

      let lineAndDots = g.append("g")
          .attr("transform", "translate(" + ((margin.left + margin.right) / 2) - 10 + "," + 0 + ")")

      // Data line
      lineAndDots.append("path")
          .datum(symbol.values)
          .attr("d", line)
          .attr("fill", "none")
          //.attr("d", areaPa)
          //.attr("fill", "#15959F")
          .style("opacity", 0.4);

      // Data dots
      lineAndDots.selectAll("circle")
          .data(symbol.values)
        .enter().append("circle") // con append se ingresa el elemento html propiamente tal
          .attr("r", 2)
          .attr("cx", function(d) { return x(d.cap); })
          .attr("cy", function(d) { return y(d.words); })
          .attr("fill", "#15959F");

      
      /*g.append('g')  // gris '#D9D9D9'
          //.attr('class', 'grid')
          .attr('transform', `translate(0, ${height})`)
          .call(d3.axisBottom()
              .scale(x)
              .tickSize(-height, 0, 0)
              //.attr("fill", "white")
              .tickFormat(''));*/
      /*g.append('g')
        .attr('class', 'grid')
        .call(d3.axisLeft()
            .scale(y)
            .tickSize(-width, 0, 0)
            .tickFormat(''));*/
    }

});

/*d3.select('#clear').on('click', (_) =>{
        updateData();
        d3.selectAll('circle').attr('class', 'inactive ball');
        //d3.selectAll('circle').remove();
    });*/
// <button class="clear_btn" value="Clear" id="clear">Clear</button>

function onchange() {
    selectValue = d3.select('select').property('value')
    d3.dsv(",", "TheLordOfTheRing.csv", function(d) {
      return {
        film: d.Film,
        chapter: d.Chapter,
        character: d.Character,
        race: d.Race,
        words: parseInt(d.Words),
        numfilm: d.story.split("-")[0],
        cap: +d.story.split("-")[1]
      };
    }).then((data) => {
          var filtered = data.filter(function(d) {
             return d.numfilm == "1"; 
          });
          var nested = d3.nest()
          .key(k => k.character)
          .entries(filtered);
        
      console.log("se hizo onchange");
      console.log(nested);
      console.log(nested[0].key);
      console.log(nested[0].values[0].words);
      // Scale the range of the data again 
      x.domain(d3.extent(data, function(d) { return d.cap; }));
      y.domain([0, d3.max(data, function(d) { return d.words; })]);
    });
}

/*function multiple(nested) {
  
  width = 150;
  height = 120;
  margin = {
    top: 15,
    right: 10,
    bottom: 40,
    left: 35
  };*/

  /*var div = d3.select("#vis")
  .selectAll(".chart")
  .data(nested);
    
  div.enter()
    .append("div")
    .attr("class", "chart")
    .append("svg").append("g");*/

  /*var svg = div.select("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom);

  var g = svg
    .select("g")
    .attr("transform", "translate(" + margin.left + 
          "," + margin.top + ")");

  g.append("rect")
  .attr("class", "background")
  //.style("pointer-events", "all")
  .attr("width", width + margin.right)
  .attr("height", height);


//d3.scaleBand().rangeRound([0, width])
  var xScale = d3.scaleBand().rangeRound([0, width]);
  var yScale = d3.scalelinear().range([height, 0]);

  var extentX, maxY;
  maxY = d3.max(nested, function(c) {
    return d3.max(c.values, function(d) {
      return yValue(d);
    });
  });
  maxY = maxY + (maxY * 1 / 4);
  yScale.domain([0, maxY]);
  /*extentX = d3.extent(nested[0].values, function(d) {
    return xValue(d);
  });
  xScale.domain(data.map(function(d) { return d.cap; }));
    


  var line = d3.svg.line()
    .x(function(d) { return xScale(d.cap); })
    .y(function(d) { return yScale(d.words); });

  var area = d3.svg.area()
    .x(function(d) { return xScale(d.cap); })
    .y0(height).y1(function(d) { return yScale(d.words); });

  lines = g.append("g");

  lines.append("path")
    .attr("class", "area")
    .attr("d", function(c) {
      return area(c.values);
    });

  lines.append("path")
    .attr("class", "line")
    .attr("d", function(c) {
      return line(c.values);
    });*/


  /*let area = d3.svg.area()
    .x(function(d) { return xScale(d.cap); })
    .y0(height).y1(function(d) { return yScale(d.words); });

  lines = g.append("g");

  lines.append("path")
    .attr("class", "area")
    .attr("d", function(c) {
      console.log(c.values);
      return area(c.values);
    });

  lines.append("path")
    .attr("class", "line")
    .attr("d", function(c) {
      return line(c.values);
    });*/


      /*var nest;
      nest = d3.nest().key(function(d) {
        return d.character;
      }).sortValues(function(a, b) {
        return d3.ascending(a.cap, b.cap);
      }).entries(rawData);
      console.log(nest);
      //return nest;

        SmallMultiples = function() {
          var area, bisect, caption, chart, circle, curYear, data, height, line, margin, mousemove, mouseout, mouseover, setupScales, width, xScale, xValue, yAxis, yScale, yValue;
          width = 150;
          height = 120;
          margin = {
            top: 15,
            right: 10,
            bottom: 40,
            left: 35
          };
          data = [];
          circle = null;
          caption = null;
          curYear = null;
          bisect = d3.bisector(function(d) {
            return d.cap;
          }).left;
          //format = d3.time.format("%Y");
          xScale = d3.scale.linear().range([0, width]);
          yScale = d3.scale.linear().range([height, 0]);
          xValue = function(d) {
            return d.cap;
          };
          yValue = function(d) {
            return d.words;
          };
          yAxis = d3.svg.axis().scale(yScale).orient("left").ticks(4).outerTickSize(0).tickSubdivide(1).tickSize(-width);
          area = d3.svg.area().x(function(d) {
            return xScale(xValue(d));
          }).y0(height).y1(function(d) {
            return yScale(yValue(d));
          });
          line = d3.svg.line().x(function(d) {
            return xScale(xValue(d));
          }).y(function(d) {
            return yScale(yValue(d));
          });
        }

        setupIsoytpe = function() {
          $("#vis").isotope({
            itemSelector: '.chart',
            layoutMode: 'fitRows',
            getSortData: {
              descending: function(e) {
                var d, sum;
                d = d3.select(e).datum();
                sum = d3.sum(d.values, function(d) {
                  return d.words;
                });
                return sum * -1;
              },
              alphabetical: function(e) {
                var d;
                d = d3.select(e).datum();
                return d.key;
              }
            }
          });
          return $("#vis").isotope({
            sortBy: 'descending'
          });
        };

        plotData = function(selector, data, plot) {
          return d3.select(selector).datum(data).call(plot);
        };

        $(function() {
          var display, plot;
          plot = SmallMultiples();
          var data;
          if (error) {
            console.log(error);
          }
          data = nest;
          plotData("#vis", data, plot);
          setupIsoytpe();
        });
        /*display = function(error, rawData) {
          
          //return setupIsoytpe();
        };*/
        /*queue().defer(d3.dsv, "TheLordOfTheRing.csv").await(display);
        return d3.select("#button-wrap").selectAll("div").on("click", function() {
          var id;
          id = d3.select(this).attr("id");
          d3.select("#button-wrap").selectAll("div").classed("active", false);
          d3.select("#" + id).classed("active", true);
          return $("#vis").isotope({
            sortBy: id
          });
        });*/
  



    /*SmallMultiples = function() {
          var area, bisect, caption, chart, circle, curYear, data, height, line, margin, mousemove, mouseout, mouseover, setupScales, width, xScale, xValue, yAxis, yScale, yValue;
          width = 150;
          height = 120;
          margin = {
            top: 15,
            right: 10,
            bottom: 40,
            left: 35
          };
          data = [];
          circle = null;
          caption = null;
          curYear = null;
          bisect = d3.bisector(function(d) {
            return d.cap;
          }).left;
          //format = d3.time.format("%Y");
          xScale = d3.scale.linear().range([0, width]);
          yScale = d3.scale.linear().range([height, 0]);
          xValue = function(d) {
            return d.cap;
          };
          yValue = function(d) {
            return d.words;
          };
          yAxis = d3.svg.axis().scale(yScale).orient("left").ticks(4).outerTickSize(0).tickSubdivide(1).tickSize(-width);
          area = d3.svg.area().x(function(d) {
            return xScale(xValue(d));
          }).y0(height).y1(function(d) {
            return yScale(yValue(d));
          });
          line = d3.svg.line().x(function(d) {
            return xScale(xValue(d));
          }).y(function(d) {
            return yScale(yValue(d));
          });
        }


        setupScales = function(data) {
          var extentX, maxY;
          maxY = d3.max(data, function(c) {
            return d3.max(c.values, function(d) {
              return yValue(d);
            });
          });
          maxY = maxY + (maxY * 1 / 4);
          yScale.domain([0, maxY]);
          extentX = d3.extent(data[0].values, function(d) {
            return xValue(d);
          });
          return xScale.domain(extentX);
        };

        chart = function(selection) {
          return selection.each(function(rawData) {
              var div, g, lines, svg;
              data = rawData;
              setupScales(data);
              div = d3.select(this).selectAll(".chart").data(data);
              div.enter().append("div").attr("class", "chart").append("svg").append("g");
              svg = div.select("svg").attr("width", width + margin.left + margin.right).attr("height", height + margin.top + margin.bottom);
              g = svg.select("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
              g.append("rect").attr("class", "background").style("pointer-events", "all").attr("width", width + margin.right).attr("height", height).on("mouseover", mouseover).on("mousemove", mousemove).on("mouseout", mouseout);
              lines = g.append("g");
              lines.append("path").attr("class", "area").style("pointer-events", "none").attr("d", function(c) {
                return area(c.values);
              });
              lines.append("path").attr("class", "line").style("pointer-events", "none").attr("d", function(c) {
                return line(c.values);
              });
              lines.append("text").attr("class", "title").attr("text-anchor", "middle").attr("y", height).attr("dy", margin.bottom / 2 + 5).attr("x", width / 2).text(function(c) {
                return c.key;
              });
              lines.append("text").attr("class", "static_year").attr("text-anchor", "start").style("pointer-events", "none").attr("dy", 13).attr("y", height).attr("x", 0).text(function(c) {
                return xValue(c.values[0]).getFullYear();
              });
              lines.append("text").attr("class", "static_year").attr("text-anchor", "end").style("pointer-events", "none").attr("dy", 13).attr("y", height).attr("x", width).text(function(c) {
                return xValue(c.values[c.values.length - 1]).getFullYear();
              });
              circle = lines.append("circle").attr("r", 2.2).attr("opacity", 0).style("pointer-events", "none")
              caption = lines.append("text").attr("class", "caption").attr("text-anchor", "middle").style("pointer-events", "none").attr("dy", -8)
              curYear = lines.append("text").attr("class", "year").attr("text-anchor", "middle").style("pointer-events", "none").attr("dy", 13).attr("y", height);
              return g.append("g").attr("class", "y axis").call(yAxis);
            });
        };
    

        mouseover = function() {
          circle.attr("opacity", 1.0);
          d3.selectAll(".static_year").classed("hidden", true);
          return mousemove.call(this);
        };
        mousemove = function() {
          var date, index, year;
          year = xScale.invert(d3.mouse(this)[0]).getFullYear();
          date = format.parse('' + year);
          index = 0;
          circle.attr("cx", xScale(date)).attr("cy", function(c) {
            index = bisect(c.values, date, 0, c.values.length - 1);
            return yScale(yValue(c.values[index]));
          });
          caption.attr("x", xScale(date)).attr("y", function(c) {
            return yScale(yValue(c.values[index]));
          }).text(function(c) {
            return yValue(c.values[index]);
          });
          return curYear.attr("x", xScale(date)).text(year);
        };
        mouseout = function() {
          d3.selectAll(".static_year").classed("hidden", false);
          circle.attr("opacity", 0);
          caption.text("");
          return curYear.text("");
        };

        chart.x = function(_) {
          if (!arguments.length) {
            return xValue;
          }
          xValue = _;
          return chart;
        };
        chart.y = function(_) {
          if (!arguments.length) {
            return yValue;
          }
          yValue = _;
          return chart;
        };

        transformData = function(rawData) {
          var nest;
          //format = d3.time.format("%Y");
          rawData.forEach(function(d) {
            d.cap = d.story.split("-")[1];
            return d.Words = +d.Words;
          });
          nest = d3.nest().key(function(d) {
            return d.Character;
          }).sortValues(function(a, b) {
            return d3.ascending(a.cap, b.cap);
          }).entries(rawData);
          return nest;
          };

        plotData = function(selector, data, plot) {
          return d3.select(selector).datum(data).call(plot);
        };

        setupIsoytpe = function() {
        $("#vis").isotope({
          itemSelector: '.chart',
          layoutMode: 'fitRows',
          getSortData: {
            count: function(e) {
              var d, sum;
              d = d3.select(e).datum();
              sum = d3.sum(d.values, function(d) {
                return d.words;
              });
              return sum * -1;
            },
            name: function(e) {
              var d;
              d = d3.select(e).datum();
              return d.key;
              }
            }
          });
          return $("#vis").isotope({
            sortBy: 'count'
          });
        };

        $(allfunctions() {
            var display, plot;
            plot = SmallMultiples();
            display = function(error, rawData) {
              var data;
              if (error) {
                console.log(error);
              }
              data = transformData(rawData);
              plotData("#vis", data, plot);
              return setupIsoytpe();
            };
            queue().defer(d3.dsv, "TheLordOfTheRing.csv").await(display);
            return d3.select("#button-wrap").selectAll("div").on("click", function() {
              var id;
              id = d3.select(this).attr("id");
              d3.select("#button-wrap").selectAll("div").classed("active", false);
              d3.select("#" + id).classed("active", true);
              return $("#vis").isotope({
                sortBy: id
              });
            });
        });*/
    



  