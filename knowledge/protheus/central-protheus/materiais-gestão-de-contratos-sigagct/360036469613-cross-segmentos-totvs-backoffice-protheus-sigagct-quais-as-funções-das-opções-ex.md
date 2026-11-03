---
article_id: 360036469613
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: cc4ce6d1af4332efcd34df911d410f55fce1cdb85f0f281d9b0b3848e6851d29
fetched_at: '2026-06-28T22:37:24.057500+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais as funções das
  opções existentes na Aba Parâmetros/Revisão na realização de uma Revisão de Contratos
  ?
type: support-article
updated_at: '2026-06-16T11:58:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036469613-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-as-fun%C3%A7%C3%B5es-das-op%C3%A7%C3%B5es-existentes-na-Aba-Par%C3%A2metros-Revis%C3%A3o-na-realiza%C3%A7%C3%A3o-de-uma-Revis%C3%A3o-de-Contratos
---

**Dúvida**  
Quais as funcionalidades das opções existentes na Aba "Parâmetros/Revisão" na realização de uma Revisão de Contratos ?

**Ambiente**  
Protheus - Gestão de Contratos - A partir da versão 12.1.17

**Solução**  
Explicação sobre os parâmetros de Fin./Fisico e Redistribuição de Saldos na Aba Parâmetros/Revisão:

* ***Arrasto -->*** A opção Arrasto permite transferir os saldos de parcelas já medidas para a primeira parcela em aberto do Cronograma.
* ***Redistribuir Saldos -->*** A opção Redistribuir Saldos permite a redistribuição dos saldos de parcelas já medidas **para as demais parcelas em aberto** do cronograma (não somente à primeira), para que os saldos não medidos em períodos anteriores sejam futuramente medidos. Trata-se de redistribuir algo já distribuído anteriormente, no caso o saldo de parcelas anteriores.  
  A opção Redistribuir Saldos é habilitada somente se a opção Arrasto for marcada, pois antes de realizar a redistribuição saldos é necessário realizar o arrasto.
* ***Tipo (Acréscimo ou Decréscimo) -->*** Define se deseja acrescentar ou retirar alguma alguma parcela do Cronograma.
* ***Quantidade -->*** Define o numero de Parcelas a Acrescentar ou retirar conforme o definido no parâmetro anterior.
* ***Parcelas Ant(CN9\_CPARCA):*** Define se as parcelas anteriores serão inclusas na redistribuição do valores.
* ***Parcelas Rea(CN9\_CPARCV):*** Define se as parcelas com valor realizado também serão utilizadas na distribuição. Depende de CN9\_PARCA estar ativado.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
