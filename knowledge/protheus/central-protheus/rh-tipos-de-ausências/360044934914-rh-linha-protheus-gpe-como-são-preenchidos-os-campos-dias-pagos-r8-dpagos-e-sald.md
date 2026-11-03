---
article_id: 360044934914
category: RH - Tipos de Ausências
content_hash: 6dc95dacd4ab278037bdcf049ba236df3f7c679259b1645993b8e73bf1d71adf
fetched_at: '2026-06-28T22:43:20.994536+00:00'
product: protheus
section_id: 360011967353
source: central-protheus
title: RH - Linha Protheus - GPE - Como são preenchidos os campos Dias Pagos (R8_DPAGOS)
  e Saldo Dias (R8_SDPAGAR) na rotina de Ausências
type: support-article
updated_at: '2025-08-13T17:01:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044934914-RH-Linha-Protheus-GPE-Como-s%C3%A3o-preenchidos-os-campos-Dias-Pagos-R8-DPAGOS-e-Saldo-Dias-R8-SDPAGAR-na-rotina-de-Aus%C3%AAncias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34156543268375)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como o sistema preenche os campo **Dias Pagos (R8\_DPAGOS)** e **Saldo Dias (R8\_SDPAGAR)** na rotina de Ausências?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O campo **Dias Pagos (R8\_DPAGOS)**, representa o número de dias pagos conforme ausência.  
Por exemplo, na ocasião de pagamento por **Férias**, este valor representa a quantidade de dias pagos associadas a este cálculo, quantos dias o funcionário tirou de férias. Agora, por exemplo, na ocasião de um afastamento por **Acidente de Trabalho ou Doença**, representa a quantidade de dias que a empresa efetuará o pagamento/desconto do salário referente a essa ausência cujo valor são 15 dias.  
  
O campo de **Saldo Dias (R8\_SDPAGAR)**, acumula a quantidade pendente ainda a ser paga referente a ausência.  
Por exemplo, na ocasião de afastamento por **Licença Maternidade** onde são pagos 120 dias, a cada mês esse campo é atualizado com a quantidade restante após pagamento desses dias, ou seja, digamos que no primeiro mês sejam pagos 30 dias, o saldo de dias será 90 dias e assim por diante.  
Quando o pagamento é quitado, o campo **Dias Pagos (R8\_PAGOS)** possui conteúdo equivalente ao campo **Dias a Pagar (R8\_DPAGAR)**.  
  
Esses campos em conjunto ao campo **Status (R8\_STATUS)** são atualizados apenas através do fechamento do período do cálculo cujo propósito é o cumprimento do pagamento devido do período e acompanhamento do mesmo.

**Saiba Mais**  
[Artigos Gestão de Pessoal](%C2%A0https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
