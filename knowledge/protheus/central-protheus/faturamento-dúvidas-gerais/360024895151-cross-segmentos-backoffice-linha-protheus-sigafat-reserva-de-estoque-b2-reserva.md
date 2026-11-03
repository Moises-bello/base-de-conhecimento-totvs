---
article_id: 360024895151
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4d6c3d490a70c386683163889111464b89966f10fb1f7fd70e69e25c7d2d687c
fetched_at: '2026-06-28T22:38:32.993312+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Reserva de Estoque
  B2_RESERVA posterior à liberação do Pedido
type: support-article
updated_at: '2023-07-28T18:46:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024895151-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Reserva-de-Estoque-B2-RESERVA-posterior-%C3%A0-libera%C3%A7%C3%A3o-do-Pedido
---

**Ocorrência**Reserva de Estoque B2\_RESERVA posterior à liberação do Pedido

Quando a empresa precisa realizar a liberação do Pedido de Vendas, porém, a Nota não é emitida no mesmo momento; pode ocorrer de, no momento da emissão da Nota, determinado Pedido que é prioridade para a empresa, não poder ser liberado e Faturado, pois o saldo do Produto está reservado no estoque para outro Pedido emitido / liberado antes, o qual ainda não foi faturado (sendo que este segundo não é a prioridade).

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**Sempre que for realizada a liberação de Estoque para o Pedido, o B2\_RESERVA do produto será alimentado, reservando o saldo para este Pedido.  
  
**Solução**

É possível, Liberar o Pedido pela rotina MATA440 - Liberação de Pedidos, e executar a rotina de forma automática, na qual há opção para não analisar o estoque neste momento. Ou seja, o sistema fará as análises de Regras, de Verbas, até Crédito; mas não realiza a análise de estoque, mantendo o pedido bloqueado por estoque (aguardando análise).  
Desta forma, aguardar para fazer a liberação de estoque (e a respectiva reserva do produto) apenas no momento que for efetivamente faturar a nota.

Então, deve-se realizar a análise de crédito separada da liberação de Estoque; pois é no momento da Liberação de Estoque que o saldo é empenhado / comprometido.

Saiba Mais: **[Reserva de Estoque B2\_RESERVA posterior à liberação do Pedido](http://tdn.totvs.com/pages/releaseview.action?pageId=235575382)**

Veja nosso Webinar: **[Análise e Bloqueio de Estoque no Faturamento (SIGAFAT)](https://youtu.be/6XfctVxULuY)**
