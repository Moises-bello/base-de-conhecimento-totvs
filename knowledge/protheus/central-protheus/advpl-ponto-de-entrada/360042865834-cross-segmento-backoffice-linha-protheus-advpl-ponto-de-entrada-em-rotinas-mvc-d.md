---
article_id: 360042865834
category: ADVPL - Ponto de Entrada
content_hash: 948b014a24822e2f9765b7b668f8fa3fa6660acbbd4d5ccaf95de7405266905a
fetched_at: '2026-06-28T22:40:11.561531+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Ponto de entrada em rotinas
  MVC do módulo DPR
type: support-article
updated_at: '2021-12-21T19:52:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042865834-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-em-rotinas-MVC-do-m%C3%B3dulo-DPR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min****Dúvida**Pontos de entrada em rotinas MVC do módulo DPR, em que momentos os pontos são executados nas rotinas DPRA340,DPRA341, DPRA342?

**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Solução**Nas três rotinas identificamos que a chamada do ponto de entrada padrão do *MVC* ocorre nas seguintes funções:

|  |  |
| --- | --- |
| **DPRA340** | Gerar Ordem |
| Ordens Relacionadas ->(Visualizar,Excluir,Regerar) |
| **DPRA341** | Aprovar Estrutura |
| Aprov. Operação |
| Reabrir Estrutura |
| Reabrir Operação |
| Suspender |
| Reabrir suspensão |
| **DPRA342** | Liberar |

**Saiba Mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Pontos de entrada MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025996033)[Cross Segmento - Backoffice Linha Protheus - ADVPL - Tratamento help ponto de validação MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013994911)
