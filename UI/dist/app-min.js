const SPA=(e=>{"use strict";let a,o,l;a=(a=>{o=e(a),e("#game-toggle").on("click",()=>{s()})});let s=()=>{let e=SPA.ResponseModule.getPlayerToken;SPA.ResponseModule.joinGame;e().then(e=>(l=e.playerToken,console.log(l),l)).catch(e=>console.error(new Error(e)))};return{init:a}})($);SPA.GameModule=(e=>{"use strict";let a,o,l,s,t,i,n,d,r=[];a=((a,o,c)=>{d=o,s=c,l=a;for(let e=0;e<s.length;e++)r.push([]);i=e('<div id="row-info">'),n=e('<div id="col-info">'),t=e('<div id="reversi-board">'),s.forEach((a,o)=>{const l=o+1;e(i).append('<div class="row-info-cell"> <span>'+l+"</span> </div>"),a.forEach((a,i)=>{const n=d[i],c=s[o][i],f=e('<div data-row="'+l+'" data-col="'+n+'" data-played='+c+' class="reversi-field"></div>');0!=c&&f.append(p()),r[o].push(f),e(t).append(f)})}),d.forEach(a=>{e(n).append('<div class="col-info-cell">'+a+"</div>")}),e(l).append(i),e(l).append(t),e(l).append(n)}),o=(e=>{let a=0;e.forEach(e=>{let o=0;e.forEach(e=>{const l=e,t=s[a][o];l!=t&&(0==t&&r[a][o].append(p()),r[a][o].attr("data-played",l)),o++}),a++}),s=e});let p=()=>e('<div class="fiche"></div>');return{init:a,updateGrid:o,test:()=>{console.log("test")}}})($),SPA.ResponseModule=(e=>{"use strict";let a,o,l,s,t,i="http://localhost:5001";return{move:a=((a,o,l,s)=>new Promise((t,n)=>e.ajax({url:i+"/api/Spel/Zet",method:"PUT",data:JSON.stringify({moveType:a,col:o,row:l,playerToken:s}),success:e=>{t(e)},failed:e=>{n("failed")}}))),getGameInfo:o=((a=0)=>new Promise((o,l)=>e.ajax(i+"/api/Spel/"+a,{success:e=>{o(e)},failed:e=>{l("failed")}}))),getPlayerToken:l=(()=>new Promise((a,o)=>e.ajax(i+"/api/Spel/GetPlayerToken",{method:"GET",success:e=>{a(e)},failed:e=>{o("failed")}}))),joinGame:s=(a=>new Promise((o,l)=>e.ajax(i+"/api/Spel/JoinGame/"+a,{method:"GET",success:e=>{o(e)},failed:e=>{l("failed")}}))),subscribe:t=((e,a)=>{new EventSource(i+"/api/Spel/Event/"+e).onmessage=(e=>{if("1"!=e.data){let o=e.data.split("'")[1],l=JSON.parse(o);a(l)}})})}})($);