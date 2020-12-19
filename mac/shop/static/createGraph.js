export function track(city)
{
var dict={}
function edges(adjlist,cities)
{
adjlist[dict['srinagar']]=[[dict['jammu'],150]];
adjlist[dict['jammu']]=[[dict['srinagar'],150],[dict['shimla'],75]];
adjlist[dict['shimla']]=[[dict['jammu'],75],[dict['dehradun'],120],[dict['chandigarh'],180]];
adjlist[dict['dehradun']]=[[dict['srinagar'],120],[dict['roorkee'],55],[dict['haridwar'],40]];
adjlist[dict['haridwar']]=[[dict['dehradun'],40],[dict['roorkee'],30]];
adjlist[dict['roorkee']]=[[dict['haridwar'],30],[dict['dehradun'],55],[dict['muzaffarnagar'],80]];
adjlist[dict['chandigarh']]=[[dict['shimla'],180],[dict['jalandhar'],65],[dict['karnal'],60]];
adjlist[dict['jalandhar']]=[[dict['chandigarh'],65],[dict['amritsar'],25],[dict['ludhiana'],30]];
adjlist[dict['amritsar']]=[[dict['jalandhar'],25]];
adjlist[dict['ludhiana']]=[[dict['jalandhar'],30],[dict['karnal'],60]];
adjlist[dict['karnal']]=[[dict['ludhiana'],60],[dict['chandigarh'],40],[dict['delhi'],35]];
adjlist[dict['muzaffarnagar']]=[[dict['roorkee'],80],[dict['meerut'],40],[dict['delhi'],100]];
adjlist[dict['meerut']]=[[dict['muzaffarnagar'],40],[dict['delhi'],80]];
adjlist[dict['delhi']]=[[dict['muzaffarnagar'],100],[dict['meerut'],80],[dict['karnal'],35],[dict['lucknow'],300],[dict['alwar'],175],[dict['jaipur'],120],[dict['kota'],700],[dict['agra'],100]];
adjlist[dict['alwar']]=[[dict['delhi'],175],[dict['jaipur'],90],[dict['bikaner'],115]];
adjlist[dict['bikaner']]=[[dict['alwar'],115]];
adjlist[dict['jaipur']]=[[dict['alwar'],90],[dict['delhi'],120],[dict['gandhinagar'],275],[dict['udaipur'],80],[dict['kota'],300]];
adjlist[dict['gandhinagar']]=[[dict['jaipur'],275],[dict['udaipur'],150]];
adjlist[dict['udaipur']]=[[dict['gandhinagar'],150],[dict['jaipur'],80],[dict['kota'],250],[dict['ahemdabad'],350],[dict['mumbai'],400]];
adjlist[dict['kota']]=[[dict['delhi'],700],[dict['jaipur'],300],[dict['udaipur'],250],[dict['bhopal'],500]];
adjlist[dict['ahemdabad']]=[[dict['udaipur'],350],[dict['mumbai'],200]];
adjlist[dict['mumbai']]=[[dict['udaipur'],400],[dict['ahemdabad'],200],[dict['panaji'],180],[dict['nanded'],500]];
adjlist[dict['panaji']]=[[dict['mumbai'],180],[dict['bengaluru'],560]];
adjlist[dict['bengaluru']]=[[dict['panaji'],560],[dict['kochi'],220],[dict['chennai'],180]];
adjlist[dict['kochi']]=[[dict['bengaluru'],220]];
adjlist[dict['chennai']]=[[dict['bengaluru'],180],[dict['vishakhapatnam'],200]];
adjlist[dict['vishakhapatnam']]=[[dict['chennai'],200],[dict['bhubaneshwar'],575]];
adjlist[dict['bhubaneshwar']]=[[dict['vishakhapatnam'],575],[dict['bhopal'],250],[dict['kolkata'],700]];
adjlist[dict['bhopal']]=[[dict['bhubaneshwar'],250],[dict['nagpur'],375],[dict['kota'],500],[dict['agra'],800]];
adjlist[dict['nagpur']]=[[dict['bhopal'],375],[dict['nanded'],450]];
adjlist[dict['nanded']]=[[dict['nagpur'],450],[dict['mumbai'],500]];
adjlist[dict['kolkata']]=[[dict['bhubaneshwar'],700],[dict['patna'],500]];
adjlist[dict['patna']]=[[dict['kolkata'],500],[dict['lucknow'],400],[dict['agra'],600]];
adjlist[dict['agra']]=[[dict['bhopal'],800],[dict['delhi'],100],[dict['lucknow'],250],[dict['patna'],600]];
adjlist[dict['lucknow']]=[[dict['patna'],400],[dict['delhi'],300],[dict['agra'],250]];

return adjlist
}



function creategraph(cities)
{let adjlist=[];
   for(let i=0;i<cities.length;i++)
   {
    adjlist.push([]);
   }
   adjlist=edges(adjlist,cities);


  return adjlist
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

let cities=['srinagar','jammu','shimla','dehradun','haridwar','roorkee','chandigarh','jalandhar','amritsar','ludhiana','karnal',
'muzaffarnagar','meerut','delhi','alwar','bikaner','jaipur','gandhinagar','udaipur','kota','ahemdabad','mumbai','panaji','bengaluru',
'kochi','chennai','vishakhapatnam','bhubaneshwar','bhopal','nagpur','nanded','kolkata','patna','agra','lucknow'];
let V=cities.length;

for(let i=0;i<V;i++)
{
    dict[cities[i]]=i
}
////console.log(dict);


var graph=creategraph(cities);
console.log(graph);
let distance1 = djikstra(graph,V,13);//delhi
let distance2 = djikstra(graph,V,21);//mumbai
let distance3 = djikstra(graph,V,31);//kolkata
////console.log(distances);
var dest=dict[city];
var complete=false;
console.log(dest)
console.log(city)
if((dest==13) || (dest==21) || (dest==31))
{complete=true;

}

if(!complete)
{
let path=[];
let finalsource="source";
if(distance1[dest][0]<=distance2[dest][0] && distance1[dest][0]<=distance3[dest][0] )
{
    finalsource="delhi";
}
else if(distance2[dest][0]<=distance1[dest][0] && distance2[dest][0]<=distance3[dest][0])
{
    finalsource="mumbai";
}
else
{
    finalsource="kolkata";
}
let parent=distance1[dest][1];
if(finalsource=="delhi")
{
parent=distance1[dest][1];
}
else if(finalsource=="mumbai")
{
    parent=distance2[dest][1];
}
else
{
    parent=distance3[dest][1];
}
let distances=distance1;
if(finalsource=="delhi")
{
    distances=distance1;
}
else if(finalsource=="mumbai")
{
    distances=distance2;
}
else
{
    distances=distance3;
}

while(dest!=-1)
{
    path.push(dest);
    if(finalsource=="delhi")
    {dest=distance1[dest][1];}
    else if(finalsource=="mumbai")
    {
        dest=distance2[dest][1];
    }
    else
    {
        dest=distance3[dest][1];
    }
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
                size: 30
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
 //console.log("create data")
    function createdata()
    {//console.log("create data")

        // Initialising number of nodes in graph dynamically
        //const V = Math.floor(Math.random() * cities.length) + 3;
    const V=path.length;
        // Preparing node data for Vis.js
        let vertices = [];
        for (let i = 0; i < path.length; i++) {
            if(path[i]==dict[finalsource])
            {
                cities[path[i]]=cities[path[i]]+"(supply center)";
            }
            if(cities[path[i]]==city && cities[path[i]]!=finalsource)
            {
                cities[path[i]]=cities[path[i]]+"(Destination)";
            }
            vertices.push({ id: i, label: cities[path[i]] });
        }

        // Preparing edges for Vis.js
        let edges = [];
        //console.log("edges---")
        for (let i = 0; i < path.length-1; i++) {
            // Picking a neighbour from 0 to i-1 to make edge to
    
            //Math.floor(Math.random() * i);

            // Adding the edge between node and neighbour
            let temp=0;
            for(let j=0;j<graph[path[i]].length;j++)
            {
                if(graph[path[i]][j][0]==path[i+1])
                {
                    temp=j;break;
                }
            }
            console.log("temp",temp)
            //console.log("temp--",temp)
            edges.push({ from: i, to: i+1, color: 'orange', label: String(graph[path[i]][temp][1] ) });
            
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

        let tempp=0;
            for(let j=0;j<graph[path[i]].length;j++)
            {
                if(graph[path[i]][j][0]==path[i+1])
                {
                    tempp=j;break;
                }
            }
            console.log("temp",tempp)

        var temp=`<tr>
          <td>${places[i]}</td>
          <td>${places[i+1]}</td>
          <td>${graph[path[i]][tempp][1]}Km</td>
        </tr>`;
        table=table+temp;
     }
     table=table+"</table>"
     document.getElementById('table').innerHTML=table; 

};
}
else
{
    var table=`Your order is already at nearby center `;
    document.getElementById('table').innerHTML=table; 
}

};