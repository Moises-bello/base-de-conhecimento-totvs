---
article_id: 11337644535575
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7444faf3777303ade9576cd9f85e84297b7e8d2b1d632d708dee359e1b7fbba3
fetched_at: '2026-06-28T22:38:42.635553+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Zerar saldo remanescente do controle de reservas
type: support-article
updated_at: '2022-12-30T20:18:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11337644535575-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Zerar-saldo-remanescente-do-controle-de-reservas
---

**Dúvida**Qual o comportamento e configuração da funcionalidade de zerar saldo remanescente das reservas no Faturamento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.  
  
**Solução**

Essa opção é exibida na alteração do Controle de Reservas e permite estornar o saldo remanescente de reservas parcialmente utilizadas, que não podem ter o valor alterado pelo botão “alterar” convencional, e não podem mais ser depuradas.

Ao clicar no botão e confirmar, a quantidade remanescente é liberada nas tabelas de controles de saldo / reserva do sistema, e o saldo baixado é gravado no campo ***C0\_QTDELIM***.

**Caminho:** Atualizações > Pedidos > Controle Reservas > Alterar > Outras ações > **Zerar Saldo Remanescente**

**Exemplo:**

Inclua um pedido de venda mencionando a quantidade 2, vinculando uma reserva com quantidade 3. Como será utilizado apenas 2 unidades, execute a função “Zera Saldo Remanescente” para que seja estornado a quantidade que não será utilizada.

A reserva fica com a legenda em azul e acrescenta a quantidade zerada no campo ***C0\_QTDELIM*** (quantidade eliminada).

**Saiba mais:**

[FAT0131 Rotina Controle de Reservas (MATA430)](https://tdn.totvs.com/x/P5AjDw)
