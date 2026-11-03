---
article_id: 360004341792
category: RH - Folha de Pagamento
content_hash: 168ca0b25d4028e71f99ad164f0ea28e4419ced5d6537cb3ae57387e7192050f
fetched_at: '2026-06-28T22:44:17.146562+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Fluxo de cálculos e processos
type: support-article
updated_at: '2024-09-05T17:56:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004341792-RH-Linha-Protheus-GPE-Fluxo-de-c%C3%A1lculos-e-processos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19147373515927) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como funciona o fluxo de cálculo da folha na versão 12?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**O fluxo da folha de pagamento a partir da **release 12** do **Protheus** segue as seguintes definições:

1. Calcular os roteiros de**Outros** **Benefícios****BEN - Plano de Saúde PLA - **Vale Alimentação VAL - Vale Refeição VRF -**Vale Transporte VTR**/ **Férias - FER** e **Rescisão - RES** e após integrar pela rotina de **Integração de Roteiros - GPEM019.**
2. Calcular o adiantamento e fazer o fechamento (Não integra roteiro de **ADI**).
3. O período seguinte é habilitado após o fechamento do período atual, para executar o **Fechamento do****Período** é necessário que exista os roteiros cadastrados no período seguinte.
4. Calcular o roteiro de folha - **FOL.**
5. Roteiros **131 - 1 ª Parcela do 13º Salário** e **132 - 2ª Parcela do 13º Salário**, só devem ser cadastrados no mês em que forem ser pagos (exemplo 131 novembro, 132 dezembro) não são integrados é necessário executar o fechamento antes de calcular a folha.
6. Após estes processos efetuar a conferência da folha e executar o fechamento do período.

**Saiba Mais**  
[MP - GPE0844 - Fluxo de cálculos e processos](http://tdn.totvs.com/pages/viewpage.action?pageId=239031455)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Passo a passo para o processo de fechamento da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057785494-RH-Linha-Protheus-GPE-Passo-a-passo-para-o-processo-de-fechamento-da-folha)
