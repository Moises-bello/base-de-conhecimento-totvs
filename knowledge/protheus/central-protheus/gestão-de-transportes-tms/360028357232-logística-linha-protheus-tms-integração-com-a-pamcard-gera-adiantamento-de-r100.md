---
article_id: 360028357232
category: Gestão de Transportes (TMS)
content_hash: 924d8e54971a63625be2661a3096033ad28c0a4f806428e74e101416ec66cb1a
fetched_at: '2026-06-28T22:45:29.349548+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Integração com a Pamcard gera adiantamento
  de R$1,00
type: support-article
updated_at: '2025-10-22T17:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028357232-Log%C3%ADstica-Linha-Protheus-TMS-Integra%C3%A7%C3%A3o-com-a-Pamcard-gera-adiantamento-de-R-1-00
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28629468592663)*** Tempo aproximado para leitura: **00:00:30 min****Dúvida**Porque na integração com a **Pamcard** em alguns casos é gerada uma parcela de adiantamento de R$1,00?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**Isto ocorre porque na geração de um contrato na **Pamcard**é necessário ter um valor e uma parcela. Este lançamento é considerado como adiantamento. Quando não há valor de adiantamento na viagem no campo **DTR\_ADIFRE - Adiantamento**, o Sistema envia a parcela de adiantamento no valor de R$1,00 para a **Pamcard** com o status **PENDENTE**.  
  
No pagamento do saldo do contrato, este lançamento de adiantamento de R$ 1,00 é excluído e o valor apresentado no pagamento de saldo gera o registro **SALDO FINAL**, conforme demonstra imagem abaixo:

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029029631)

O valor de R$1,00 é enviado apenas para a parcela de adiantamento. Para o valor total do frete a pagar enviado para a Pamcard na *tag* **viagem.frete.valor.bruto**, o Sistema realiza a seguinte regra:

* Caso o valor da viagem esteja preenchido no campo **DTR\_VALFRE - Valor do Frete** , este será o valor considerado;
* Caso a viagem não possua valor preenchido, será feita uma simulação do frete pagar para que seja enviado o valor total do frete junto a **Pamcard**.

Essa regra se aplica ao valor total do frete a pagar enviado para a **Pamcard** com a rotina **TMSPamcard**com data 09/10/2025 ou superior.  **Importante**  
Caso a viagem tenha valor de adiantamento e ainda assim na integração com a **Pamcard** o valor enviado não for o preenchido na viagem e sim R$ 1,00, verifique se a despesa de adiantamento que está utilizando movimenta banco, no campo **DT7\_MOVBCO = 1 - Sim**, pois a integração depende da movimentação bancária. Caso esteja utilizando percentual de adiantamento, a despesa que deve verificar é a definida no parâmetro **MV\_DESADF**.  
  
**Saiba mais**Atualização do envio da *tag* **viagem.frete.valor.bruto:[DT Integração Pamcard Inconsistência no envio do valor bruto do frete](https://tdn.totvs.com/pages/releaseview.action?pageId=1003479975)**
