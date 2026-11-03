---
article_id: 360050186973
category: RH - 13º salário
content_hash: 2683a44e5a27e82f7ff88865ec29b368c36ddcc4643754f2a1963736e6f4e721
fetched_at: '2026-06-28T22:44:00.453615+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de 13º não efetuado - Calculo Finalizado
  Pela FinalCalc() ou Pela EndCalc() - S_CAINSAL
type: support-article
updated_at: '2026-06-25T11:41:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050186973-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-13%C2%BA-n%C3%A3o-efetuado-Calculo-Finalizado-Pela-FinalCalc-ou-Pela-EndCalc-S-CAINSAL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18852773074199) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Cálculo de 13º não efetuado - Calculo Finalizado Pela FinalCalc() ou Pela EndCalc() - [S\_CAINSAL](https://totvssuporte.zendesk.com/knowledge/editor/01HERB41HJ4F5E47N2Q45E1CVC/pt-br?brand_id=1509248)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para correção da mensagem gerada no log e para que consiga calcular corretamente, verifique se existem os identificadores de cálculo a seguir cadastrados na tabela SRV - Cadastro de Verbas em Atualizações  > Definições de Cálculo > Verbas GPEA040:  
  
**- 1304 - Insalubridade Férias Mês**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18852715829271)

**- 1634 - Insalubridade 13. Salario 1ª Parc.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18852715843863)

**- 1645 - Insalubridade 13. Salario Maternidade 1ª Parc.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18852715855767)  
  
**- 1930 - Insalubridade 13º Lic. Adoção 1ª Parc**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18884323560983)**

**- 1442 - Insalubridade 13. Salario Maternidade 2ª Parc.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18852715865879)

**- 1942 - Insalubridade 13º Lic. Adoção**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18884352080151)  
  
  
**- 1292 - Insalubridade 13º Salário 2ª Parc.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18852773151383)

3. Caso não encontre algum deles, cadastre a verba como Provento, com tipo Valor, exceto as verbas com Ids **1930** e **1942**, que devem ser incluídas como **Base Provento**.  
Após realizar o cadastro execute novamente o cálculo do 13º salário onde não será mais gerada a mensagem.

**Saber Mais:**

[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento:**[**https://www.youtube.com/watch?v=T7b4zMlphTI**](https://www.youtube.com/watch?v=T7b4zMlphTI)
