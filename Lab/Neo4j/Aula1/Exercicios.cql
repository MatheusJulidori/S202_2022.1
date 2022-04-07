Querys:

1 - MATCH (n) return n
2 - MATCH(n:Game) WHERE n.ano > 2012 RETURN n;
3 - MATCH (n:Game) WHERE n.genero =~ 'Terror' RETURN n;
4 - MATCH n=()-[j:JOGOU]->() WHERE j.nota > 7 return n;

CREATE(g:Game{titulo:'League of Legends',genero:'MOBA',ano:2009});
CREATE(g:Game{titulo:'World of Warcraft',genero:'MMORPG',ano:2004});
CREATE(g:Game{titulo:'Elden Ring',genero:'RPG',ano:2022});
CREATE(g:Game{titulo:'Valheim',genero:'RPG',ano:2021});

CREATE(j:Jurado{nome:'Julidori'});
CREATE(j:Jurado{nome:'Phyll'});
CREATE(j:Jurado{nome:'Arthur'});


MATCH(j:Jurado{nome:'Julidori'}),(g:Game{titulo:'League of Legends'})
CREATE(j)-[:JOGOU{nota:8, horas:3512}]->(g);

MATCH(j:Jurado{nome:'Julidori'}),(g:Game{titulo:'World of Warcraft'})
CREATE(j)-[:JOGOU{nota:10, horas: 4326}]->(g);

MATCH(j:Jurado{nome:'Julidori'}),(g:Game{titulo:'Valheim'})
CREATE(j)-[:JOGOU{nota:9, horas: 324}]->(g);

MATCH(j:Jurado{nome:'Phyll'}),(g:Game{titulo:'World of Warcraft'})
CREATE(j)-[:JOGOU{nota:7, horas: 2142}]->(g);

MATCH(j:Jurado{nome:'Phyll'}),(g:Game{titulo:'Elden Ring'})
CREATE(j)-[:JOGOU{nota:10, horas: 312}]->(g);

MATCH(j:Jurado{nome:'Arthur'}),(g:Game{titulo:'Valheim'})
CREATE(j)-[:JOGOU{nota:10, horas: 314}]->(g);

MATCH(j:Jurado{nome:'Arthur'}),(g:Game{titulo:'League of Legends'})
CREATE(j)-[:JOGOU{nota:0, horas: 2}]->(g);
