---
article_id: 35015081693719
category: Financeiro - Contas a Pagar - PIX
content_hash: 561327c1c10ea8dcd6796e8659f3552842e88f90bcb2ed7909ffc5f14d875a86
fetched_at: '2026-06-28T22:38:11.329073+00:00'
product: protheus
section_id: 1500001550462
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA885 - Como utilizar
  o Ponto de entrada em MVC para a rotina FINA885 (Chave PIX)
type: support-article
updated_at: '2025-09-17T20:09:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35015081693719-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA885-Como-utilizar-o-Ponto-de-entrada-em-MVC-para-a-rotina-FINA885-Chave-PIX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35015081670423) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como utilizar o ponto de entrada em MVC para a rotina FINA885 (Chave PIX)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para chamada desta fonte, é necessário colocar um M na frente do nome desta fonte em particular; desta forma, será acionado na rotina.  
  
**Modelo** -> FINA885M  
**Grid campos** -> FORDETAIL  
**Cabeçalho** -> FORMCAB

Este ponto de entrada é o único que deve ser uma **User Function**e ter como nome o ID do Modelo de Dados **(Model) FINA885M**.

**Saiba mais**

[Ponto de Entrada Padrão do MVC](https://tdn.totvs.com/pages/viewpage.action?pageId=208345968)

[Execução automática - Vincular a chave PIX no cadastro de fornecedores](https://tdn.totvs.com/pages/releaseview.action?pageId=852326999)
