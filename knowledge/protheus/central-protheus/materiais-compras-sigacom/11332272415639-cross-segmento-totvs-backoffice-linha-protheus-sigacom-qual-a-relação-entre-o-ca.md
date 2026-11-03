---
article_id: 11332272415639
category: Materiais - Compras (SIGACOM)
content_hash: b30e2a7f36be43b69a2bb1ad8d3cf72108971fe3534efe08904d0e0e559da9c4
fetched_at: '2026-06-28T22:41:11.740561+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Qual a relação
  entre o campo C8_VALIDA e a rotina de Cotação ?
type: support-article
updated_at: '2022-12-30T18:44:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11332272415639-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Qual-a-rela%C3%A7%C3%A3o-entre-o-campo-C8-VALIDA-e-a-rotina-de-Cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual a relação do campo C8\_VALIDA e a rotina de Cotação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**O campo C8\_VALIDA serve para informar ao Comprador sobre a data de validade de uma proposta enviada pelo Fornecedor, porém, atualmente nenhuma rotina do processo de Cotação utiliza esse campo como forma restritiva do processo, pois mesmo uma proposta vencida pode sofrer alterações quando houver alguma informação que esteja incorreta, dessa forma a data informada não é impeditivo para o processo de Cotação.

A maior influência desse campo é no processo de Análise de Cotação pois, quando uma proposta está vencida não há mais garantia de que será mantida caso o Fornecedor vença com a melhor condição oferecida.

Em soluções futuras como o Portal Gestão de Compras haverá a possibilidade de bloquear propostas vencidas na Análise de Cotação, porém não há previsão desse bloqueio ocorrer na Atualização da Cotação, caso seja necessário efetuar esse processo pode-se utilizar como sugestão o Ponto de Entrada MT150ENV para garantir o bloqueio.

Documentação sobre o Ponto de Entrada:

[Ponto de Entrada MT150ENV](https://tdn.totvs.com/x/ldtc)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
