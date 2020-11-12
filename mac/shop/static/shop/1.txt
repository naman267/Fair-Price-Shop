

export function track(city)
{
var dict={};
function creategraph(V,E)
{
  let adjlist=[];
  for(let i=0;i<V;i++)
  {
    adjlist.push([]);
  }
  for(let i=0;i<E.length;i++)
  {
  	adjlist[dict[E[i][0]]].push( [dict[E[i][1]],E[i][2]] );

    adjlist[dict[E[i][1]]].push( [ dict[E[i][0]] , E[i][2] ] );
  }
  return adjlist;
}

function djikstra(graph, V, src) {
    let vis = Array(V).fill(0);
    let dist = [];
    for(let i=0;i<V;i++)
        dist.push([10000,-1]);
    dist[src][0] = 0;

    for(let i=0;i<V-1;i++){
        let mn = -1;
        for(let j=0;j<V;j++){
            if(vis[j]===0){
                if(mn===-1 || dist[j][0]<dist[mn][0])
                    mn = j;
            }
        }

        vis[mn] = 1;
        for(let j=0;j<graph[mn].length;j++){
            let edge = graph[mn][j];
            if(vis[edge[0]]===0 && dist[edge[0]][0]>dist[mn][0]+edge[1]){
                dist[edge[0]][0] = dist[mn][0]+edge[1];
                dist[edge[0]][1] = mn;
            }
        }
    }

    return dist;
}

//let cities=['Delhi', 'Mumbai', 'Gujarat', 'Goa',];
let cities = ['Delhi', 'Mumbai', 'Gujarat', 'Goa','Kanpur', 'Jammu', 'Hyderabad', 'Bangalore', 'Gangtok', 'Meghalaya'];
let V=cities.length;

for(let i=0;i<V;i++)
{
	dict[cities[i]]=i
}
console.log(dict);
let E=[];
for(let i=0;i<V;i++)
{
	for(let j=i+1;j<V;j++)
	{
		let weight=Math.floor(Math.random() * 70) + 30;
        if(i===0 && j===7)
        {
            weight=500;
        }
		E.push([cities[i],cities[j],weight]);
	}
}
console.log(E);
var graph=creategraph(V,E);
console.log(graph);
let distances = djikstra(graph,V,7);
console.log(distances);
var dest=dict[city];


let path=[];

let parent=distances[dest][1];

while(dest!=-1)
{
	path.push(dest);
	dest=distances[dest][1];
}
console.log("path",path);
path=path.reverse();

create();

function create()
{

    // create a network
    const container = document.getElementById('graph');
  //  const genNew = document.getElementById('generate-graph');

    // initialise graph options

    const options = {
        edges: {
            labelHighlightBold: true,
            font: {
                size: 20
            }
        },
        nodes: {
            font: '12px arial-red',
            scaling: {
                label: true
            },
            shape: 'icon',
            icon: {
                face: 'FontAwesome',
                code: '\uf015',
                size: 40,
                color: '#991133'
            }
        }
    };

    // initialize your network!
    const network = new vis.Network(container);
    network.setOptions(options);

    function createdata()
    {

        // Initialising number of nodes in graph dynamically
        //const V = Math.floor(Math.random() * cities.length) + 3;
    const V=path.length;
        // Preparing node data for Vis.js
        let vertices = [];
        for (let i = 0; i < path.length; i++) {
            if(path[i]==7)
            {
                cities[path[i]]=cities[path[i]]+"(supply center)";
            }
            if(cities[path[i]]==city)
            {
                cities[path[i]]=cities[path[i]]+"(Destination)";
            }
            vertices.push({ id: i, label: cities[path[i]] });
        }

        // Preparing edges for Vis.js
        let edges = [];
        for (let i = 0; i < path.length-1; i++) {
            // Picking a neighbour from 0 to i-1 to make edge to
    
            //Math.floor(Math.random() * i);

            // Adding the edge between node and neighbour
            edges.push({ from: i, to: i+1, color: 'orange', label: String(20 ) });
            
        }

        //Preparing data object for Vis.js
        const data = {
            nodes: vertices,
            edges: edges
        };
        return data;
    
 }
   
        let data = createdata();
        network.setData(data);
    
    var places=[];
    for(var i=0;i<path.length;i++)
    {
        places.push(cities[path[i]]);
    }
    console.log("places",places);

   var table=` <table style="width:100%">
    <tr>  
    <th>From</th> 
    <th>To</th>
    <th>Distance</th>
    </tr>`;
     for(var i=0;i<places.length-1;i++)
     {
        var temp=`<tr>
          <td>${places[i]}</td>
          <td>${places[i+1]}</td>
          <td>Distance</td>
        </tr>`;
        table=table+temp;
     }
     table=table+"</table>"
     document.getElementById('table').innerHTML=table; 

};
};