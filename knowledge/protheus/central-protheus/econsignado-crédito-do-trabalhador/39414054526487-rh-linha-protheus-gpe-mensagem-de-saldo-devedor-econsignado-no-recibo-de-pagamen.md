---
article_id: 39414054526487
category: eConsignado (Crédito do Trabalhador)
content_hash: d9ccfb62e909b4045540773b8d82e3906a8a4479e1b9383226cb0de73ba78d8c
fetched_at: '2026-06-28T22:43:07.324573+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Mensagem de Saldo Devedor eConsignado no Recibo
  de Pagamento
type: support-article
updated_at: '2026-03-31T17:06:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39414054526487-RH-Linha-Protheus-GPE-Mensagem-de-Saldo-Devedor-eConsignado-no-Recibo-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39414054516119) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Mensagem de Saldo Devedor eConsignado no Recibo de Pagamento (GPER030)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Foi implementada a exibição da mensagem referente ao resíduo de empréstimo do eConsignado no recibo de pagamento.

A mensagem será exibida quando houver empréstimo eConsignado e o valor descontado for parcial ou não houver desconto:

      ATENÇÃO TRABALHADOR: Não foi possível realizar o desconto total ou parcial do seu empréstimo consignado, por exceder o percentual de 35% da remuneração disponível, conforme disposto na Lei nº 10.820/2003 e na Portaria MTE nº 435/2025. Procure sua instituição financeira para regularizar o pagamento desse empréstimo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39414054516759)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39414054516887)

**Importante:** A impressão do recibo em período aberto é validada diretamente na Rotina de Valores Futuros SRK. Quando a impressão for referente a um período fechado, a validação passa a considerar o campo RCK\_NPAG (Valor Não Pago), que registra o valor não quitado do empréstimo no momento do fechamento da folha na rotina de Conta Corrente valores Futuros.

**Devido a falta de espaço no leiaute, a mensagem não será exibida se o tipo de impressão selecionado for "Pré-impresso". Eventuais mudanças podem ser customizadas no rdmake da rotina.** [RH - Linha Protheus - GPE - Como customizar o fonte do recibo de pagamento RDMAKE para a rotina GPER030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016654371-RH-Linha-Protheus-GPE-Como-customizar-o-fonte-do-recibo-de-pagamento-RDMAKE-para-a-rotina-GPER030)

**Saiba mais:**

[Mensagem Recibo de Pagamento (GPER030)](https://tdn.totvs.com/pages/releaseview.action?pageId=1018575847)

[RH - Recibos e Cheques](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909573-RH-Recibos-e-Cheques)
