---
article_id: 25199619300631
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2942de4574376b2ece8cfb70761f911f05de8c2c1f6b9bfd6257969eb7740d68
fetched_at: '2026-06-28T22:38:55.767248+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA175 - HELP A175MOVLOT
  ao Estornar Baixa do CQ
type: support-article
updated_at: '2024-07-26T19:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25199619300631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA175-HELP-A175MOVLOT-ao-Estornar-Baixa-do-CQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25199619277591) Tempo aproximado para leitura: **00:04:30 min** **Dúvida**

Ao Estornar a Baixa do CQ (MATA175) de determinada movimentação apresenta o **HELP A175MOVLOT**. Como identificar o que esta apresentado o HELP?

![A175MOVLOT2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25200310622103)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

O **HELP A175MOVLOT** é apresentado quando para produtos que controlam LOTE/SUBLOTE (B1\_RASTRO) após efetuar a Baixa do CQ o Saldo do Lote encontrar-se em uma das seguintes situações:

**- 1 -** O Lote ser consumido em **Pedido de Venda Liberado**, ou seja Saldo Reservado **(B2\_RESERVA)**;

**- 2 -** O Lote ser consumido por algum **Empenhos a partir de OP (MATA381)**, **Lote vencido (SDD)** ou também quando existe **Solicitação de Transferência entre Filiais (via MATA311) ainda não efetivada. (B2\_QEMP);**

**- 3 -** O Lote ser consumido em uma Pré-Requisição de **Solicitação ao Armazém, (B2\_QEMPSA)**

![A175MOVLOT f4.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25200247498263)

Nesse caso, deve-se avaliar os consumos dos Lotes nas rotinas envolvidas, estornar cada um dos processos que consumiram o Saldo do Lote e ao refazer o Estorno da Baixa não vai apresentar mais o **HELP A175MOVLOT**.

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

*[SIGAEST - Como descobrir a origem dos saldos na consulta com comando [F4] no Produto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto)*
