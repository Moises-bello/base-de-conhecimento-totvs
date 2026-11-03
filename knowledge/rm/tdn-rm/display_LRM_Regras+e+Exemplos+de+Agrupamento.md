---
content_hash: 9e649ebd37d08b92bb4869475210e3940186e9809bafff3c6e28647021f7c317
fetched_at: '2026-06-29T00:09:27.504260+00:00'
page_id: '423938528'
product: rm
source: tdn-rm
title: Regras e Exemplos de Agrupamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Regras+e+Exemplos+de+Agrupamento
version: 6
---

Internamente o sistema identifica as partidas da seguinte forma:

Tipo de Agrupamento = 0 – Para partidas sem nenhum tipo de Agrupamento  
Tipo de Agrupamento = 1 – Para partidas resultantes do Agrupamento de Débitos  
Tipo de Agrupamento = 2 – Para partidas resultantes do Agrupamento de Créditos  
Tipo de Agrupamento = 3 – Para partidas resultantes do Agrupamento de Débitos com Créditos em uma única partida (quando partidas originais forem cadastradas com o débito em uma partida e o crédito em outra).  
Tipo de Agrupamento = 4 – Para partidas resultantes do Agrupamento de Débitos com Créditos em uma única partida (quando partidas originais já forem cadastradas com o débito e o crédito em uma única partida).

**Atenção:**

1 - Uma partida resultante de um tipo de agrupamento não poderá ser agrupada novamente utilizando-se outro tipo de agrupamento:

* Uma partida que teve seus débitos agrupados (Tipo = 1), não poderá ser agrupada novamente utilizando-se a opção "Agrupar Débitos com Créditos em uma única partida" (Tipo = 3 ou 4);
* Uma partida que teve seus créditos agrupados (Tipo = 2), não poderá ser agrupada novamente utilizando-se a opção "Agrupar Débitos com Créditos em uma única partida" (Tipo = 3 ou 4);
* Uma partida que tenha originalmente o débito e o crédito preenchidos somente poderá ser agrupada com partidas que também originalmente tenham o débito e o crédito preenchidos (neste caso irão gerar partidas com o Tipo = 4);
* Uma partida resultante do agrupamento do débito e do crédito na mesma partida (Tipo = 3) não poderá ser agrupada a outra partida resultante do Tipo = 4.

2 - Uma partida resultante de um tipo de agrupamento pode ser agrupada a outra partida resultante do mesmo tipo de agrupamento ou a outra partida ainda não agrupada (Tipo = 0).

**Forma de Agrupamento: Agrupar partidas e Agrupar Partidas a Crédito**   
**Forma de agrupamento: Agrupar Débitos com Créditos em uma única partida.**  
  
**Forma de agrupamento: Agrupar Débitos com Créditos em uma única partida.**
