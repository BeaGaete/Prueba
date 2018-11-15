const width = 1000, height = 1000;
const groupSpacing = 5; 
const cellSpacing = 2;
const offsetTop = height / 5;
const cellSize = Math.floor((width - 11 * groupSpacing) / 100) - cellSpacing;

/*var canvas = d3.select('canvas'),
    context = canvas.node().getContext("2d"),
    width = canvas.property("width"),
    height = canvas.property("height"),
    radius = 1.5;

var hiddencanvas = d3.select('canvas'),
    context = canvas.node().getContext("2d"),
    width = canvas.property("width"),
    height = canvas.property("height"),
    radius = 1.5;*/

/*const canvas = d3.select('#container')
                 .append('canvas')
                    .attr('width', width)
                    .classed('mainCanvas', true) 
                    .attr('height', height);

const hiddenCanvas = d3.select('#container')
                        .append('canvas')
                        .classed('hiddenCanvas', true)
                        .attr('width', width) 
                        .attr('height', height)
                        .style('display', 'none');*/

/*context = canvas.node().getContext("2d");
contexthiddenCanvas = hiddenCanvas.node().getContext("2d");*/

let colorG = d3.scaleOrdinal([d3.rgb("#ee057a"), d3.rgb('#ffd203'), d3.rgb('#6dc9c8'), d3.rgb('#43b77a'),
        d3.rgb('#fB7022'), d3.rgb('#7d3f1a'), d3.rgb('#cc769d'), d3.rgb('#276d77'),
        d3.rgb('#b91e46'), d3.rgb('#0aafe7')]);

const genreColor = {'Action': "#ee057a", 'Adventure': '#ffd203', 'Animation': '#6dc9c8', 'Horror': '#43b77a', 'Music': '#fB7022', 'Romance': '#7d3f1a', 
'Thriller': '#cc769d', 'War': '#276d77', 'Western': '#b91e46'}

const genreColorRGB = {'Action': [238, 5, 7], 'Adventure': [255, 210, 3], 'Animation': [109, 201, 200], 'Horror': [67, 183, 122], 'Music': [251,112, 34], 'Romance': [125,63, 26], 
'Thriller': [204, 118, 157], 'War': [39, 109, 119], 'Western': [185, 30, 70]}

const genreColorInt = {'Action': 1, 'Adventure': 2, 'Animation': 3, 'Horror': 4, 'Music': 5, 'Romance': 6, 
'Thriller': 7, 'War': 8, 'Western': 9}

const allGenres = ['Action', 'Adventure', 'Animation', 'Horror', 'Music', 'Romance', 
'Thriller', 'War', 'Western']

let count = -1;

let nextCol = 1;



// las peliculas tiene que estar ordenadas de mayor a menor popularidad
// agregar más atributos
d3.dsv(",", "new_movies_metadata.csv", function(d) {
	
  return {
  	index: count+=1,
  	adult: d.adult,
  	//belongs_to: d.belongs_to,
  	budget: +d.budget,
  	genres: d.genres,
  	//onegenre: d.genres.split(" ")[0],
  	homepage: d.homepage,
  	id: d.id,
  	name: d.name,
  	year: d.year,
  	poster_path: d.poster_path,
  	overview: d.overview

  	/*imdb_id: d.imdb_id,
  	original_language: d.original_language,
  	original_title: d.original_title,
  	overview: d.overview,
  	popularity: +d.popularity,
  	poster_path: d.poster_path,
  	production_companies: d.production_companies,
  	production_countries: d.production_countries,
  	release_date: d.release_date,
  	revenue: +d.revenue,
  	runtime: +d.runtime,
  	spoken_languages: d.spoken_languages,
  	status: d.status,
  	tagline: d.tagline,
  	title: d.title,
  	video: d.video,
  	vote_average: d.average,
  	vote_count: d.vote_count*/
  };
}).then(function(dataMovies) {
	console.log(dataMovies);

	var data = [];
	var count = 0;
	const radius = 2.5;
	const theta = Math.PI * (3 - Math.sqrt(5));
	d3.range(6859).forEach(function(el){
		count+= 1;
		var r = 10 * Math.sqrt(count), a = theta * count;
		data.push({ x: width / 2 + r * Math.cos(a), y: height / 2 + r * Math.sin(a) - 100, r: radius, index: count -1 });
	});
	console.log(data);

	// main canvas
	var mainCanvas = d3.select('#container')
		.append('canvas')
		.classed('mainCanvas', true)
		.attr('width', width)
		.attr('height', height);



	// hidden canvas
	var hiddenCanvas = d3.select('#container')
		.append('canvas')
		.classed('hiddenCanvas', true)
		.attr('width', width)
		.attr('height', height);

	context = mainCanvas.node().getContext("2d");
	contextHidden = hiddenCanvas.node().getContext("2d");

	var customBase = document.createElement('custom');
	var custom = d3.select(customBase); // replacement of SVG

		// map to track color the nodes.
	var colorToNode = {};
	// function to create new colors for picking
	var nextCol = 1;
	function genColor(){
		var ret = [];
		if (nextCol < 16777215){
			ret.push(nextCol & 0xff); //R
			ret.push((nextCol & 0xff00) >> 8); //G
			ret.push((nextCol & 0xff0000) >> 16); //B

			nextCol += 1;
		}
		var col = "rgb(" + ret.join(',') + ")";
		return col;
	}



	/*var x = d3.scaleLinear()
		.domain([2, 8])
		.range([0, width]);

	var y = d3.scaleLinear()
		.domain([2,8])
		.range([height, 0]);*/

	databind(data);
		var t = d3.timer(function(elapsed){
			draw(mainCanvas, false);
			if (elapsed > 300) t.stop();
			// timer running the draw function repeatedly for 300ms.
		});


	function databind(data){
		var join = custom.selectAll('custom.circle')
			.data(data);


		var enterSel = join.enter()
			.append('custom')
			.attr('class', 'circle')
			.attr('x', function(d,i){
				return d.x;
			})
			.attr('y', function(d,i){
				return d.y;
			})
			.attr('r', function(d,i){
				return Math.abs(d.r);
			});

		join
			.merge(enterSel)
			.transition()
			.attr('fillStyleHidden', function(d){
				if (!d.hiddenCol){
					d.hiddenCol = genColor();
					colorToNode[d.hiddenCol] = d;
				}
				return d.hiddenCol;
			});

	}

	function draw(canvas, hidden){
		var context = canvas.node().getContext('2d');

		context.clearRect(0, 0, width, height);

		var elements = custom.selectAll('custom.circle');
		elements.each(function(d,i){
			var node = d3.select(this);
			context.fillStyle = hidden ? node.attr('fillStyleHidden') : 'steelblue';
			context.beginPath();
			context.arc(node.attr('x'), node.attr('y'), node.attr('r'), 0, 2*Math.PI);
			context.fill();
		})
	}

	mainCanvas.call(d3.zoom()
	    .scaleExtent([1 / 2, 4])
	    .on("zoom", zoomed));

	function zoomed() {
	  context.save();
	  context.clearRect(0, 0, width, height);
	  context.translate(d3.event.transform.x, d3.event.transform.y);
	  context.scale(d3.event.transform.k, d3.event.transform.k);
	  draw(mainCanvas, false);
	  context.restore();
	}

	hiddenCanvas.call(d3.zoom()
	    .scaleExtent([1 / 2, 4])
	    .on("zoom", zoomedHidden));

	function zoomedHidden() {
	  contextHidden.save();
	  contextHidden.clearRect(0, 0, width, height);
	  contextHidden.translate(d3.event.transform.x, d3.event.transform.y);
	  contextHidden.scale(d3.event.transform.k, d3.event.transform.k);
	  draw(hiddenCanvas, true);
	  contextHidden.restore();
	}

	function getTitle(index, dataMovies) {
		return dataMovies[index].name;
	}

	d3.select('.mainCanvas').on('mousemove', function(){
		draw(hiddenCanvas, true);
		var mouseX = d3.event.layerX || d3.event.offsetX;
		var mouseY = d3.event.layerY || d3.event.offsety;

		var hiddenCtx = hiddenCanvas.node().getContext('2d');
		var col = hiddenCtx.getImageData(mouseX, mouseY, 1, 1).data;

		var colKey = 'rgb(' + col[0] + ',' + col[1] + ',' + col[2] + ')';
		var nodeData = colorToNode[colKey];

		if (nodeData){
			console.log(nodeData);
			d3.select('#tooltip')
				.style('opacity', 0.8)
				.style('top', d3.event.pageY + 5 + 'px')
				.style('left', d3.event.pageX + 5 + 'px')
				.html('x: ' + nodeData.x + '<br>' + 'y: ' + nodeData.y + '<br>' + 'radius: ' + nodeData.r + '<br>' + 'index: ' + nodeData.index + '<br>' + 'color: ' + nodeData.hiddenCol + '<br>' + 'title: ' + getTitle(nodeData.index, dataMovies));
		} else {
			d3.select('#tooltip')
				.style('opacity', 0);
		}

	})
});




