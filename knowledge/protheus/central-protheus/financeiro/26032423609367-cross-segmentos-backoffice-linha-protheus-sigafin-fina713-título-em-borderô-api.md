---
article_id: 26032423609367
category: Financeiro
content_hash: 29ddae62603e2917f140a136d166445975d3d3823a9d078693b409318359492b
fetched_at: '2026-06-28T22:38:03.165205+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Título em
  borderô API não é apresentando no monitor de pendências com status "À registrar"
  ficando zeros registros
type: support-article
updated_at: '2024-08-30T20:21:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26032423609367-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-T%C3%ADtulo-em-border%C3%B4-API-n%C3%A3o-%C3%A9-apresentando-no-monitor-de-pend%C3%AAncias-com-status-%C3%80-registrar-ficando-zeros-registros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26032423576087) Tempo aproximado para leitura: **00:05:00min****Dúvida**FINA713 - Título em borderô API não é apresentando no monitor de pendências com status "À Registrar" ficando zeros registros  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - A partir da P22.1.10  
  
**Causa:**FINA060/FINA240 - Ao colocar o título em borderô para fazer a comunicação via API

Exemplo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26032423583127)

FINA710 Ao acessar o monitor de pendência, ficando zero registros "À Registrar"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26032440224663)

**Solução:**

Esse problema geralmente ocorre, pois o monitor de pendência somente está posicionado em 1 filiais, e o borderô foi feito em outra filial.

Clicando no símbolo da Totvs, irá apresentar as filiais para que sejam selecionadas (Selecione Filiais)

Ao marcar todas as filiais, o registro irá voltar a ser apresentar com status "À Registrar"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26032423584919)
