d3.tsv('askmefi_category_year.tsv', (r) => ({
    category: r.category,
    n: Number(r.n),
    year: Number(r.year)
  }))
  .then((data) => {
    var nested = d3.nest()
    	.key(k => k.category)
    	.entries(data);
  
  	nested.forEach(g => g.trackball = []);
  	  
    var yExtent = fc.extentLinear()
      .accessors([d => d.n])
    	.pad([0, 0.2])
    	.include([0]);
  
  	var xExtent = fc.extentLinear()
    	.accessors([d => d.year]);

    var area = fc.seriesSvgArea()
      .crossValue(d => d.year)
      .mainValue(d => d.n);
  
  	var line = fc.seriesSvgLine()
      .crossValue(d => d.year)
      .mainValue(d => d.n);
  
  	var gridlines = fc.annotationSvgGridline()
    	.xTicks(0)
    	.yTicks(3);
  
  	var point = fc.seriesSvgPoint()
      .crossValue(d => d.year)
      .mainValue(d => d.value)
    	.size(25)
    	.decorate((selection) => {
        selection.enter()
        	.append('text');        
        selection.select('text')
        	.text(d => d.value)
      })
    
    var line = fc.annotationSvgLine()
    	.orient('vertical')
      .value(d => d.year)
    	.decorate((selection) => {
        selection.enter()
        	.select('.bottom-handle')
        	.append('text');        
        selection.select('.bottom-handle text')
        	.text(d => d.year)
      })
     
  
  	var multi = fc.seriesSvgMulti()
    	.series([area, line, gridlines, line, point])
      .mapping((data, index, series) => {
        switch (series[index]) {
        case point:            
        case line:
          return data.trackball;
        default:
          return data.values;
        }
      });
  
  	var xScale = d3.scaleLinear();
    // create a chart
    var chart = fc.chartSvgCartesian(
        xScale,
        d3.scaleLinear())
      .yDomain(yExtent(data))
    	.xDomain(xExtent(data))
    	.xLabel(d => d.key)
    	.yTicks(3)
    	.xTicks(2)
    	.xTickFormat(d3.format('0'))
      .yOrient('left')
    	.plotArea(multi);
  
    function render() {
      // render
    	var container = d3.select('#small-multiples')
      var update = container.selectAll('div.multiple')
        .data(nested);
      update.enter()
        .append('div')
      	.classed('multiple', true)
      	.merge(update)
        .call(chart)
        .classed('tooltip', d => d.trackball.length);

      // add the pointer component to the plot-area, re-rendering
      // each time the event fires.
      var pointer = fc.pointer()
        .on('point', (event) => {
          // determine the year
          if (event.length) {
            var year = Math.round(xScale.invert(event[0].x));
            // add the point to each series
            nested.forEach((group) => {
              var value = group.values.find(v => v.year === year);
              group.trackball = [{
                year: year,
                value: value.n
              }];
            })
          } else {
            nested.forEach(g => g.trackball = [])
          }
          render();
        });

      d3.selectAll('#small-multiples4 .plot-area')
        .call(pointer);  
    }
  
  	render();
	});
 
