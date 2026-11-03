---
article_id: 360024282271
category: ADVPL - Web Service
content_hash: 0592cce1b012b83a07d9eace0b49147030a0c88312eb4f1eee478b79678a6ed5
fetched_at: '2026-06-28T22:40:10.422556+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Danfe via WebService
type: support-article
updated_at: '2021-12-29T13:20:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024282271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Danfe-via-WebService
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Utilizando o Danfe via WebService não gera pdf e não gera erro.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.17  
  
**Causa**Em binários anteriores, o sistema tentava efetuar a abertura da interface gráfica, contudo caso não conseguisse, ele gera o erro internamente e prosseguia com o processamento das demais tarefas.

Contudo, este processo poderia gerar travamentos nas rotinas e impossibilitar o prosseguimento das demais operações, retendo uma thread e onerando a operação.

**Solução**Com esta proteção, no momento em que ocorrer a tentativa de exibição de um componente gráfico, será gerado o erro fatal ou até não gerando erro via WebService.

Será necessário tratar todas a funcionalidade no Rdmake DanfeII que exibem tela quando executada pelo sistema, funções como RPTStatus, Pergunte e etc...

**Saiba mais**

**[Erro: Job theadrs doesn't suport remote/visual components](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022439332-MP-ADVPL-ERRO-JOB-THREADS-DOESN-T-SUPPORT-REMOTE-VISUAL-COMPONENTS)**
