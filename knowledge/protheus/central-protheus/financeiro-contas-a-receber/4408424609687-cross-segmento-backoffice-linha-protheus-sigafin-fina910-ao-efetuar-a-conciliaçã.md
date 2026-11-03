---
article_id: 4408424609687
category: Financeiro - Contas a Receber
content_hash: 5f71f16280c568c5915fe7e6eb4caafedb623dab2bd8e9ebb472e9d2d7d57150
fetched_at: '2026-06-28T22:38:13.856713+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmento BackOffice Linha Protheus - SIGAFIN - FINA910 Ao efetuar a
  Conciliação Tef esta apresentando a mensagem de Help: A910NOINFO'
type: support-article
updated_at: '2021-09-13T17:36:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408424609687-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-FINA910-Ao-efetuar-a-Concilia%C3%A7%C3%A3o-Tef-esta-apresentando-a-mensagem-de-Help-A910NOINFO
---

**Ocorrência**Ao efetuar a Conciliação **TEF** esta apresentando a mensagem de Help: **A910NOINFO**  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408404468759/mceclip0.png)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro- Versão 12  
  
**Causa**Nos parâmetros abaixo da rotina:

MV\_PAR05 = BRANCO  
MV\_PAR06 = ZZZZZZZZZZZZ  
MV\_PAR06 esta com apenas 12 "ZZZ" preenchido, deixando assim o tamanho de campo incorreto causando o erro  
  
**Solução** Verificar o tamanho do parâmetro **MV\_PAR06** do grupo de perguntas **FINA910A**, pois o mesmo deverá ter o mesmo tamanho do campo **E1\_NSUTEF**, sendo que correto seria o tamanho 20.   
  
Será necessário realizar a alteração do parâmetro **MV\_PAR06** para 20.  
  
Efetuar o teste colocando os parâmetros:  
MV\_PAR05 = BRANCO  
MV\_PAR06 = ZZZZZZZZZZZZZZZZZZZZ 20 posições  
  
O preenchimento do conteúdo ZZZ deverá ser preenchido até completar todas as posições do campo.

**Importante**: Se deixar os parâmetro conforme abaixo, também irá funcionar.

MV\_PAR05 = BRANCO  
MV\_PAR06 = BRANCO
