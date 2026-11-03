---
article_id: 7268051134743
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: 2343daea5267a9079001b476e7c3344490630bf7af33d6c79047549a67c0e016
fetched_at: '2026-06-28T22:36:57.354995+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Fixação de preço
  aviso bolsa não cadastrada
type: support-article
updated_at: '2024-05-15T18:53:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7268051134743-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Fixa%C3%A7%C3%A3o-de-pre%C3%A7o-aviso-bolsa-n%C3%A3o-cadastrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao tentar fixar o preço na rotina de Pedido de Exportação (**EECAP100**) ao informar o mês de fixação o sistema esta exibindo uma mensagem "**Aviso - Bolsa não cadastrada**".  Mesmo cadastrando uma cotação de bolsa na rotina Cotação Bolsa (**EECAT150**)  a mensagem persiste. Como proceder para que esta mensagem não seja exibida?

![bolsa_n_o_cadastrada.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7265864085783/bolsa_n_o_cadastrada.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Foi liberado uma solução **DTRADE-7122** que ao efetuar uma fixação de preço no ambiente da 12.1.33 para um pedido de exportação ocorria um erro. Além da solução homologada foi efetuado o ajuste dos tamanhos dos campos de Código da Bolsa que estavam com tamanho 3, para o tamanho 6, pois estes campos são relacionados à tabela **YP** do dicionário **SX5** (**Tabelas Genéricas**). Também foi efetuada as adequações necessárias nos fontes em que estes campos são utilizados para que não ocorra erro nas leituras dos campos com os novos tamanhos.  
Para que a mensagem de aviso não seja mais exibida durante a fixação do preço, o campo **EE7\_CODBOL**, da tabela **EE7** - **Processo de Exportação**, o tamanho do campo deve ser ajustado de forma manual via configurador (**SIGACFG**), desta forma, caso o campo já esteja criado com o tamanho 3 , mesmo com a aplicação do **UPDDISTR**, este tamanho não será alterado. Só que o tamanho correto do campo deve ser 6 com isso será necessário efetuar a alteração de forma manual para o correto funcionamento da rotina.  
  
**Saiba mais**[DTRADE-7122 DT Erro na Fixação de Preço para a Exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=651665675)  
[Adequação ao Exportador de Café](https://tdn.totvs.com/pages/releaseview.action?pageId=235314306)
