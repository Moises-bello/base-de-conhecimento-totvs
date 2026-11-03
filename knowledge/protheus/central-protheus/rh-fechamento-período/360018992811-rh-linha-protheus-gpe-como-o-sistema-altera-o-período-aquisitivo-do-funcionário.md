---
article_id: 360018992811
category: RH - Fechamento Período
content_hash: 3c7d5ec7ee884e843905014e922d6e31e6c884c199aacd8a4331dec751070a5e
fetched_at: '2026-06-28T22:43:24.426881+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema altera o Período Aquisitivo do Funcionário
  após cálculo de Férias Coletivas
type: support-article
updated_at: '2025-04-16T11:51:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018992811-RH-Linha-Protheus-GPE-Como-o-sistema-altera-o-Per%C3%ADodo-Aquisitivo-do-Funcion%C3%A1rio-ap%C3%B3s-c%C3%A1lculo-de-F%C3%A9rias-Coletivas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16023005520791) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como o sistema altera o Período Aquisitivo do Funcionário após cálculo de Férias Coletivas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando o Funcionário é admitido e cadastrado no sistema, automaticamente a rotina de **Controle de Dias de Direito** é preenchida com os dados de seu **Período Aquisitivo:**  
![](https://totvssuporte.zendesk.com/attachments/token/FdbAhHxmtvlGrcP6ItbwvR678/?name=inline-1215508408.png)  
​

Quando são calculadas **Férias Coletivas** para um Funcionário que possui **menos de um ano** de empresa, e consequentemente **não possui** 30 dias de Férias vencidas, o sistema irá **gerar uma nova linha** na rotina de Controle de Dias de Direito **após o fechamento do período** de cálculo destas, **criando um novo período aquisitivo para uma nova contagem:**  
![](https://totvssuporte.zendesk.com/attachments/token/ZmRrlc4nfhodHyAhfg02yYH1U/?name=inline1124532770.png)

Note que o valor do campo **Qtd. Ref. Per**. também é ajustado para que não haja inconsistências, trazendo o mesmo valor de dias proporcionais adquiridos pelo Funcionário até a concessão das Férias Coletivas.  
​​

**Exemplo:** Funcionário foi admitido em Março de 2017.  
Em Dezembro ele possuía 22,5 dias de direito adquiridos, porém, a empresa teve Férias Coletivas durante 10 dias​.  
Referente ao período aquisitivo entre 03/2017 e 12/2017, ainda restam 12,5 dias de direito, portanto o sistema manterá o primeiro período com *status***Ativo**.

![](https://totvssuporte.zendesk.com/attachments/token/5Gtb2kkqyhgMK1Qlmcc52AD9a/?name=inline-693377362.png)

Período **Ativo:**

![](https://totvssuporte.zendesk.com/attachments/token/1Ulu9jkV92NaVodenOUqZyKaY/?name=inline-478563352.png)  
​

**Observação**Somente quando o restante dos dias de direito forem calculados, integrados à Folha e fechado o período do novo cálculo, o sistema irá alterar seu *status* para **Pago**.

**Importante**  
O Controle de Dias de Direito atualmente é atualizado pela rotina de **Fechamento de Período (GPEM120)** através do roteiro **FOL**, portanto, o novo período só será criado após o fechamento.   
O período aquisitivo do funcionário só é alterado se as Férias forem calculadas via **GPEM060 - Férias Coletivas**, ou seja, se as Férias forem calculadas por Férias individuais (GPEM030) ou programadas (GPEM060), o período aquisitivo **não é alterado.**

**Saber Mais:**

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)

[RH - Linha Protheus - GPE - Como calcular férias coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZJfk%2BXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDAxMDE3MjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY2FsY3VsYXItZiVDMyVBOXJpYXMtY29sZXRpdmFzBjsIVDoOc2VhcmNoX2lkSSIpNDc5NWNjN2MtMTFlYi00Y2M1LTgzZGItNTU0N2MyOWY5ZTE3BjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVZmVyaWFzIGNvbGV0aXZhcwY7CFQ6EnJlc3VsdHNfY291bnRpAkMG--c47a6f6afb5d178bfacf2117c7d39394d35616a7)  
[RH - Linha Protheus - GPE - Como excluir o calculo de férias coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXfpDeAwQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTQ2NjU0MjQ0MDctUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZXhjbHVpci1vLWNhbGN1bG8tZGUtZiVDMyVBOXJpYXMtY29sZXRpdmFzBjsIVDoOc2VhcmNoX2lkSSIpNDc5NWNjN2MtMTFlYi00Y2M1LTgzZGItNTU0N2MyOWY5ZTE3BjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVZmVyaWFzIGNvbGV0aXZhcwY7CFQ6EnJlc3VsdHNfY291bnRpAkMG--2eb3e6f78effbefe24c2282d54fd02b62b77de79)  
[RH - Linha Protheus - GPE - Pontos de Entrada disponíveis na rotina GPEM060 - Férias Coletivas/Programadas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhmSB8%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBs2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDI2MDEwNjItUkgtTGluaGEtUHJvdGhldXMtR1BFLVBvbnRvcy1kZS1FbnRyYWRhLWRpc3BvbiVDMyVBRHZlaXMtbmEtcm90aW5hLUdQRU0wNjAtRiVDMyVBOXJpYXMtQ29sZXRpdmFzLVByb2dyYW1hZGFzBjsIVDoOc2VhcmNoX2lkSSIpNDc5NWNjN2MtMTFlYi00Y2M1LTgzZGItNTU0N2MyOWY5ZTE3BjsIRjoJcmFua2kPOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVZmVyaWFzIGNvbGV0aXZhcwY7CFQ6EnJlc3VsdHNfY291bnRpAkMG--9458ca47a10db48419c0df87279e8ebb95f649b5)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
