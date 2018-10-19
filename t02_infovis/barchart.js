const margin = {top: 30, right: 20, bottom: 0, left: 20}; // 30 20 0 20

const WIDTH = 350;
const HEIGHT = 700;

const widthb =  WIDTH - margin.left - margin.right;
const heightb = HEIGHT - margin.top - margin.bottom;

const containerBarchart = d3.select('#bar')
    .append('svg')
        .attr('width', WIDTH)
        .attr('height', HEIGHT)
    .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`)


const scale = d3.scaleLinear()
                .range([margin.right, widthb])
                .domain([0, 80000]);

const xAxis = d3.axisBottom(scale).ticks(7);
const axis = containerBarchart.append('g')
        .attr('class', 'axis axis--x')

axis.call(xAxis)

containerBarchart.append("text")
        .attr("x", (widthb / 2))             
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")  
        .style("font-size", "16px")
        .style("fill", "#555")
        .style("text-decoration", "underline")
        .text("Stars en módulos de d3.js");

const lista_final = [];

const actualizarBarchart = (nodo, label, nodoclick) => {
    //clear();
    //containerBarchart.selectAll('.rect').data(lista_final).remove();
    //containerBarchart.selectAll('.text').data(lista_final).remove();
    //lista_final.length = 0;
    lista_final.push({label, nodo, nodoclick});
    //console.log(cantidad)
    // Actualizamos el dominio de la escala
    scale.domain([0, d3.max(lista_final, d=> d.nodo.stars)])  // d3.max(lista_final, d=> parseInt(d.stars))
    // Volvemos a aplicar el método call para que el eje se actualice a la 
    // nueva escala
    axis.call(xAxis)

    const data = containerBarchart.selectAll('.rect').data(lista_final);

    const enteringBar = data.enter()
        .append('rect')
        .attr('class', 'rect')
        .attr('x', margin.right)
        .attr('y', (_, i, nodoclick) => i*30 + 15)
        .attr('height', 20)
        /*if(nodo == nodoclick){
            //enteringBar.attr('class', 'rectclick')
            enteringBar.attr('stroke', 'black')
            enteringBar.attr('fill', '#FD8D3C')
            enteringBar.attr('stroke_width', '5px')
        }else{
            enteringBar.attr('class', 'rect')
            //enteringBar.attr('stroke', '#a80e06')
            //enteringBar.attr('stroke_width', '3px')
        };*/

        

    const enteringtext = data.enter()
        .append('text')
        .attr('class', 'text')
        .attr('text-anchor', 'start')
        .attr('x', margin.right + 40)
        .attr('y', (_, i, nodoclick) => i*30 + 30);


           
        
    // Agregamos el .merge para identificar las barras que ya estaban dentro
    // del dataset antes de agregar nuevos datos.
    data.merge(enteringBar).transition()
        .duration(400)
        .attr('width', d => scale(d.nodo.stars) - margin.right) // d => scale(parseInt(d.stars) ) - margin.right
        //console.log(d.stars)
        /*if(nodo == nodoclick){
            enteringBar.attr('border', 4px)
        };*/
        /*if(nodo == nodoclick){
            enteringBar.attr('class', 'rectclick')
            enteringBar.attr('stroke', '#a80e06')
            enteringBar.attr('stroke_width', '3px')
        };
        if(nodo != nodoclick){
            enteringBar.attr('class', 'rect')
            enteringBar.attr('stroke', '#a80e06')
            enteringBar.attr('stroke_width', '3px')
        };*/


    enteringBar.transition()
        .duration(400)
        .attr('width', d => scale(d.nodo.stars) - margin.right)  // d => scale(parseInt(d.stars) ) - margin.right
        .style('stroke', function(d){
        if(d.nodo == d.nodoclick){
          return 'black' // #a80e06
        } else {
          return '#FD8D3C'
        }
    })
        .attr('fill', function(d){
        if(d.nodo == d.nodoclick){
          return 'black'
        } else {
          return '#FD8D3C'
        }

         
         // or maybe also this.setAttribute('moved', 'no');
     })
        .style('stroke-width', function(d){
        if(d.nodo == d.nodoclick){
          return 6
        } else {
          return 2
        }

         
         // or maybe also this.setAttribute('moved', 'no');
     })/*if(nodo == nodoclick){
                enteringBar.attr('class', 'rectclick')
                //enteringBar.attr('stroke', '#a80e06')
                //enteringBar.attr('stroke_width', '3px')
            };
            if(nodo != nodoclick){
                enteringBar.attr('class', 'rect')
                //enteringBar.attr('stroke', '#a80e06')
                //enteringBar.attr('stroke_width', '3px')
            };*/
        
        

    enteringtext.transition()
        .delay(400)
        .text(d => d.label); // d => d.name

    axis.attr('transform', `translate(0,${lista_final.length*30 + 15})`)

    


}

const clear = () => {
    lista_final.length = 0;
    const dataRect = containerBarchart.selectAll('.rect').data(lista_final);
    const dataText = containerBarchart.selectAll('.text').data(lista_final);

    dataRect.exit()
        .transition()
        .duration(500)
        .attr('width', 0)
        .remove();
    
    dataText.exit()
        .transition()
        .delay(500)
        .text('')
        .remove();
    
    axis.transition().delay(500).attr('transform', `translate(0,${lista_final.length*30 + 15})`)
}


            
