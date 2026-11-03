---
article_id: 39780738922391
category: SIGAACD - Automação e Coleta de Dados
content_hash: 5cd23e8baa6d10b9ebcadb1e3743708864ab3a66390d389609f506c165b55ae1
fetched_at: '2026-06-28T22:39:11.083236+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  ACDA100 - Ao fazer
  a separação por OP grava somente a última linha do empenho na SD4 do lote
type: support-article
updated_at: '2026-04-16T11:38:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39780738922391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100-Ao-fazer-a-separa%C3%A7%C3%A3o-por-OP-grava-somente-a-%C3%BAltima-linha-do-empenho-na-SD4-do-lote
---

O sistema TOTVS Protheus apresentava problema ao atualizar o empenho da ordem de produção com controle de rastreabilidade, considerando apenas a última separação de materiais fracionados por lote. Foi implementada uma correção para garantir a atualização correta e completa dos empenhos após separações múltiplas. A solução está disponível nas versões 12.1.2310, 12.1.2410 e 12.1.2510, vinculada à issue DMANMAT01-47600, recomendando backup e aplicação em ambiente de homologação.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39780750877335) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao realizar a separação de materiais empenhados em uma ordem de produção com controle de rastreabilidade, o sistema atualiza o empenho da ordem de produção considerando apenas a última separação realizada, desconsiderando os demais lotes separados anteriormente quando a quantidade do produto é fracionada?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Para corrigir este comportamento, foi implementado um ajuste no sistema. Com a aplicação da correção, o sistema garante que, após a separação de materiais com fracionamento por lote, os empenhos da ordem de produção sejam atualizados de forma correta e completa. Para obter a correção, é necessário aplicar a atualização referente à issue DMANMAT01-47600

**12.1.2310**:<https://r.totvs.io/p/1244368>

**12.1.2410**:<https://r.totvs.io/p/1244369>

**12.1.2510**:<https://r.totvs.io/p/1244370>

Realizar o backup das informações, aplicar o pacote de atualização em sua base de homologação.

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)  
[26424994 DMANMAT01-47600 DT 15/04 ACDA100 - Ao fazer a separação por OP grava somente a última linha do empenho na SD4 do lote](https://tdn.totvs.com/pages/releaseview.action?pageId=1053192262)
