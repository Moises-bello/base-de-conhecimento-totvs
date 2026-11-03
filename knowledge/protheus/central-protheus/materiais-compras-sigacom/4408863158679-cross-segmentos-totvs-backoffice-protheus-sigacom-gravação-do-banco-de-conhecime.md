---
article_id: 4408863158679
category: Materiais - Compras (SIGACOM)
content_hash: bf98acae2426768124cf422757b0c02c907d6a912c5c3e87eb8586cc5a84a685
fetched_at: '2026-06-28T22:41:18.719220+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Gravação do Banco de
  Conhecimento ( Tabela AC9 ) na Rotina Atualiza Cotação MATA150
type: support-article
updated_at: '2021-09-17T21:51:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408863158679-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Grava%C3%A7%C3%A3o-do-Banco-de-Conhecimento-Tabela-AC9-na-Rotina-Atualiza-Cota%C3%A7%C3%A3o-MATA150
---

**Dúvida**

Como é a gravação do Banco de Conhecimento na rotina de Atualiza Cotações MATA150 ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - A Partir da Versão 23  
  
**Solução**

A opção "Conhecimento" ou "Banco de Conhecimento" através da rotina Atualiza Cotações (MATA150) sofreu alteração na gravação padrão da tabela AC9 da release 23 para a release 27.

Antes na release 23 essa rotina realizava a gravação do conhecimento na tabela AC9 com o índice:   
 **C8\_FILIAL, C8\_NUM, C8\_ITEM, C8\_ITEMGRD, C8\_FORNECE, C8\_LOJA, C8\_FORNOME, C8\_NUMPRO**  
  
Exemplo de visualização:  
**FILIALNUMERO0800010001FOR00101MAGAZINE LUIZA COMERCIO E TESTE99**

Agora, após atualização para a release 27 , o campo está sendo gravado com a informação invertida  
  
**C8\_FILIAL+C8\_NUM+C8\_ITEM+C8\_ITEMGRD+C8\_FORNECE+C8\_LOJA+C8\_NUMPRO+ C8\_FORNOME**   
  
A única alteração foi na ordem dos campo **C8\_FORNOME** e **C8\_NUMPRO**  
  
Exemplo de visualização:  
**FILIALNUMERO0800010001FOR0010199MAGAZINE LUIZA C**  
  
Foi realizada essa mudança para atender uma melhoria que já estava prevista em Roadmap para a release e não uma inconsistência na rotina.  
  
***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
