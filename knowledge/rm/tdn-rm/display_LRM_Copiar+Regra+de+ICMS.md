---
content_hash: 77a7d99d7de29e097ca2957a80155e5d4a976c55d499c9046b4248137ef200af
fetched_at: '2026-06-29T00:09:21.418523+00:00'
page_id: '422545882'
product: rm
source: tdn-rm
title: Copiar Regra de ICMS
type: documentation
url: https://tdn.totvs.com/display/LRM/Copiar+Regra+de+ICMS
version: 7
---

Este processo possibilita os seguintes tipos de cópia:

* Entre coligadas (globais)
* Entre filiais de coligadas diferentes (não globais)
* Entre filiais de uma mesma coligada (não globais)

 O processo de cópia irá consistir os parâmetros de inclusão de regras:

**Regras de Interface da Cópia**

* Quando as coligadas de origem e destino utilizar naturezas globais não será possível a seleção de uma filial de origem e destino
* As regras poderão ser copiadas individualmente ou por faixa
* O parâmetro "Copiar regras globais", só necessitará ser habilitado quando a filial de origem não utilizar naturezas globais.

O parâmetro "Copiar regra como global",  só deverá ser habilitado caso o usuário necessite criar na coligada de destino as regras de origem como global. Se a coligada de destino utilizar naturezas globais as regras já serão duplicadas automaticamente como globais.  
Aconselha- se quando da duplicação de faixas que seja criado um filtro que retorne somente regras globais ou não globais na coligada origem, pois todas as regras de faixa serão criadas como globais ou não globais dependendo da marcação do parâmetro.  
O parâmetro "Substituir registros no destino se eles já existirem", só irá executar esta ação caso as regras a serem copiadas não estejam associadas a naturezas de operação. Caso contrário a regra já existente será sobreposta.   
Se o parâmetro não for marcado o processo irá apresentar uma mensagem de erro informando a existência do registro que está sendo copiado.
