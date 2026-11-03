---
article_id: 7012167234199
category: SIGAEST - PROCESSAMENTOS
content_hash: dc9139a1001f642693115af1d74af059f338e9cd9c71978255e9c1773dbcc563
fetched_at: '2026-06-28T22:39:04.870523+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  MATA300 - Pontos
  de Entrada da rotina Refaz Saldos
type: support-article
updated_at: '2022-06-24T19:10:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7012167234199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Pontos-de-Entrada-da-rotina-Refaz-Saldos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

Quais os Pontos de Entrada do Refaz Saldos Atuais - MATA300? Quais as suas funções no Protheus?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada:** | **Título:** | **Descrição:** |
| **[M300SBF](https://tdn.totvs.com/pages/releaseview.action?pageId=651919580)** | Função utilizada para recalcular o saldo atual dos movimentos. | **Localização**: Function MA300Process - Função utilizada para recalcular o saldo atual dos movimentos.  **Em que ponto**: Executada após a deleção logica dos registros do SBF e antes da reconstrução da tabela SBF com os saldos atualizados. |
| **[M300SB8](https://tdn.totvs.com/pages/releaseview.action?pageId=236603423)** | Grava campos específicos no arquivo SB8. | **Localização**: Function MA300Process - Função utilizada para recalcular o saldo atual dos movimentos.  **Em que ponto**: Executada após a gravação dos campos da tabela SB8, este Ponto de Entrada é utilizado para gravar campos específicos no arquivo SB8. |
| [**MA300OK**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087628) | Valida execução da rotina | Função utilizada para recalcular o saldo atual dos movimentos.  EM QUE PONTO : Executada antes da confirmação de execução da rotina, ponto utilizado para validar se sera permitida a execução da rotina. |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7012167234199)
