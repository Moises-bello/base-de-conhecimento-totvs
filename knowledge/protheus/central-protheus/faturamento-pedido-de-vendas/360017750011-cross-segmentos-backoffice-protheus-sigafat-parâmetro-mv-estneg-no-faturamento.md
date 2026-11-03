---
article_id: 360017750011
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6ca0ff164fcab5738e2a77719472ad327333bbbecc5e1da8194b4aa5cc9640c5
fetched_at: '2026-06-28T22:38:39.910459+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Parâmetro MV_ESTNEG no Faturamento
type: support-article
updated_at: '2024-11-11T14:33:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017750011-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Par%C3%A2metro-MV-ESTNEG-no-Faturamento
---

**Dúvida**

A utilização do parâmetro MV\_ESTNEG tem efeito no módulo Faturamento?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O parâmetro **MV\_ESTNEG**, **[independentemente da configuração do parâmetro MV\_TPSALDO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013215531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-TPSALDO)**, não tem nenhum efeito no módulo Faturamento. Ele é exclusivo para movimentações realizadas no módulo de Estoque / Custos (registrar uma saída em movimentações internas para produto que não possui saldo).

No módulo Faturamento, para que não seja faturado produto que não possui saldo (causando assim estoque negativo), a forma é realizar a liberação do Pedido somente de forma automática.

Para retirar a permissão para **Liberação Manual de Estoque**, consulte a documentação: **[Retirar Permissões para Liberação Manual do Pedido de Vendas](https://tdn.totvs.com/x/VUBtDQ)**

**Saiba Mais:**

**[Parâmetro MV\_ESTNEG não impede Saldo Negativo na Liberação Manual do Estoque](https://tdn.totvs.com/x/oLx3DQ)**
