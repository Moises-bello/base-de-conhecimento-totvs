---
article_id: 27720825729815
category: Financeiro - Movimentação Bancária
content_hash: 6752c53d47ad715a27c78283c87ec8fdf66a7247c17650f6fe68a9fba6ec9d93
fetched_at: '2026-06-28T22:38:19.515089+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice Protheus - Gesplan x Protheus LP 562 (Contabilizando
  pela E5_DTDIGIT) e não pela data de disponibilidade
type: support-article
updated_at: '2024-11-12T22:13:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27720825729815-Cross-Segmentos-TOTVS-BackOffice-Protheus-Gesplan-x-Protheus-LP-562-Contabilizando-pela-E5-DTDIGIT-e-n%C3%A3o-pela-data-de-disponibilidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27720825680919) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao realizar a **Integração Gesplan x Protheus** de uma movimentação bancária e contabilizar pelo **LP 562,** está contabilizando pela **Data de digitação** (**E5\_DTDIGIT**) e não pela (**E5\_DATA**) = **Data da Movimentação.**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o parâmetro **MV\_DTCNMOV**está igual a 1.  
  
**Solução**Para solucionar o problema deve preencher o parâmetro **MV\_DTCNMOV = 2.**

## **CRIAÇÃO DO PARÂMETRO NA TABELA SX6**

| **Nome da variável** | MV\_DTCNMOV |
| --- | --- |
| **Tipo** | Caractere |
| **Descrição** | Data contabilizacao online Mov. Banc.; 1 - Database (Default); 2 - Data do Movimento |
| **Valor padrão** | 1 |

**Saiba mais**

[Utilização do parâmetro MV\_DTCNMOV](https://tdn.totvs.com/pages/releaseview.action?pageId=661617660)  
[562/564 Inclusao/Cancelamento de Movimento a Pagar (contém 564)](https://tdn.totvs.com/pages/releaseview.action?pageId=555280131#LP562-Inclus%C3%A3odeMovimentoBanc%C3%A1rio-01)
