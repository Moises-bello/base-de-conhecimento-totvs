---
content_hash: a629276c6cfe3b65b8be0040edfe86b4ae3c38810614067fb5d4413704b09664
fetched_at: '2026-06-29T00:09:21.386577+00:00'
page_id: '422545877'
product: rm
source: tdn-rm
title: Copiar Regras de IPI
type: documentation
url: https://tdn.totvs.com/display/LRM/Copiar+Regras+de+IPI
version: 3
---

Este processo possibilita os seguintes tipos de cópia:

* Entre coligadas (globais)
* Entre filiais de coligadas diferentes (não globais)
* Entre filiais de uma mesma coligada (não globais)

 O processo de cópia irá consistir os parâmetros de inclusão de regras  
   
**Regras de Interface de Cópia**

* Quando as coligadas de origem e destino utilizar naturezas globais não será possível a seleção de uma filial de origem e destino
* As regras poderão ser copiadas individualmente ou por faixa
* O parâmetro COPIAR REGRAS GLOBAIS só necessitará ser habilitado quando a filial de origem não utilizar naturezas globais.

O parâmetro COPIAR COMO GLOBAL  só deverá ser habilitado caso o usuário necessite criar na coligada de destino as regras de origem como global. Se a coligada de destino utilizar naturezas globais as regras já serão duplicadas automaticamente como globais.  
Aconselha- se quando da duplicação de faixas que seja criado um filtro que retorne somente regras globais ou não globais na coligada origem, pois todas as regras de faixa serão criadas como globais ou não globais dependendo da marcação do parâmetro.  
   
O parâmetro SUBSTITUIR REGISTROS NO DESTINO só irá executar esta ação caso as regras a serem copiadas não estejam associadas a naturezas de operação. Caso contrário a regra já existente será sobreposta.   
Se o parâmetro não for marcado o processo irá apresentar uma mensagem de erro informando a existência do registro que está sendo copiado.
