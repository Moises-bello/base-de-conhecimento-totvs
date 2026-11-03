---
article_id: 360044398353
category: Contabilidade Gerencial - Balancetes
content_hash: 2f20796d75040ef0bfdfa41494df77b81c1e4feda8fdd5c4d1c46f4f325f778c
fetched_at: '2026-06-28T22:41:04.181119+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus -  SIGACTB - CTBR040 Saldos Zerados
  = Não
type: support-article
updated_at: '2022-06-06T19:22:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044398353-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR040-Saldos-Zerados-N%C3%A3o
---

**Dúvida**  
Como gerar emissão do relatório CTBR040 (balancete) com parâmetro: Saldos Zerados = Não  
  
**Ambiente**  
Protheus – Contabilidade Gerencial – A partir da versão 12  
  
**Solução**  
Houve uma padronização nos relatórios contábeis no parâmetro   
Saldos Zerados = Não.

A seguir algumas situações que podem ocorrer nos relatórios do sistema:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Conta** | **Saldo Período Anterior** | **Débito** | **Crédito** | **Movimento** | **Saldo Período Atual** | **Saldos Zerados = Não** | **Saldos Zerados = Sim** |
| 000001 | 1000 D | 0 | 0 | 0 | 1000 D | Imprime | Imprime |
| 000002 | 0 | 1000 | 1000 | 0 | 0 | Imprime | Imprime |
| 000003 | 1000 D | 0 | 1000 | 1000 C | 0 | Imprime | Imprime |
| 000004 | 0 | 0 | 1000 | 1000 C | 1000 C | Imprime | Imprime |
| 000005 | 0 | 0 | 0 | 0 | 0 | Não Imprime | Imprime |

Mais detalhes:

<https://tdn.totvs.com/pages/releaseview.action?pageId=519720103>
