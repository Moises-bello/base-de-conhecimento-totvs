---
article_id: 360024797174
category: RH - Cálculo Adiantamento
content_hash: 0c529a0d4836f034c5cf808a5e2da56b576383f18207bb9f4e7a1cbaab6f269e
fetched_at: '2026-06-28T22:43:14.244584+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir o desconto de IR no adiantamento
  para o tipo de regime de pagamento caixa
type: support-article
updated_at: '2024-06-25T19:37:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024797174-RH-Linha-Protheus-GPE-Como-conferir-o-desconto-de-IR-no-adiantamento-para-o-tipo-de-regime-de-pagamento-caixa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24428291482007) Tempo aproximado para leitura: 00:02:30 min**

**Ocorrência**Como conferir o desconto de IR no adiantamento para o tipo de regime de pagamento caixa?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - a partir versão 12  
  
**Solução****Regime Caixa -**O funcionário trabalha em um mês e recebe até o 5º dia útil do mês subseqüente, e provavelmente auferiu um adiantamento no dia 20. Neste caso teremos o cálculo do IRRF no Adiantamento de Salário e na Folha de Pagamento.  
Para isso deve-se ser configurado as verbas abaixo para que seja respeitado o regime de pagamento:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038226454)  
  
Cálculo na pratica:

- Calculada folha 10/2018 para pagamento dia 05/11/2018![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039064013)  
  
Os valores das verbas de desconto de IR (Id 0066) e Base de IR da folha (Id 0015) vão para a **RGB - Lançamentos > Por funcionários** no fechamento do período, como verbas de **Base de IR Mês Anterior** (Id 0106) e **IR descontado Mês Anterior** (Id 0107) através da amarração no campo **V. Mês Segui** (RV\_CODMSEG), no roteiro ADI. No aguardo do cálculo do Adiantamento do mês.

- RGB período 11/2018 - Roteiro ADI

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039064713)  
  
As verbas de IR mês Anterior e Base de IR Mês anterior ficam no **roteiro ADI.**  
  
- Calculo do Adiantamento 11/2018  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038228674)

Base de IR **4.272,00**

Desconto de IR 4.272,00 \* 22,5% = 961,20 - 636,13 = 325,07 - 33,60 = **291,47**

Saiba mais

Para adquirir mais conhecimento acesse:

[RH - Linha Protheus - GPE - Alteração do tipo de regime caixa/competência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046198893-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-do-tipo-de-regime-caixa-compet%C3%AAncia?source=search)

[RH - Linha Protheus - GPE - Configuração de verbas para Adiantamento (regime competência)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036123334-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-verbas-para-Adiantamento-regime-compet%C3%AAncia-?source=search)

[RH - Linha Protheus - GPE - Como efetuar a configuração de verbas de IR para o tipo de regime caixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006990952-RH-Linha-Protheus-GPE-Como-efetuar-a-configura%C3%A7%C3%A3o-de-verbas-de-IR-para-o-tipo-de-regime-caixa?source=search)

[RH - Linha Protheus - GPE - Adiantamento Salarial - Configurações e Conceitos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052166714-RH-Linha-Protheus-GPE-Adiantamento-Salarial-Configura%C3%A7%C3%B5es-e-Conceitos?source=search)

[RH - Linha Protheus - GPE - Como identificar a origem das verbas gravadas no cálculo da folha e períodos abertos de fechados (tabelas SRC e SRD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016689031-RH-Linha-Protheus-GPE-Como-identificar-a-origem-das-verbas-gravadas-no-c%C3%A1lculo-da-folha-e-per%C3%ADodos-abertos-de-fechados-tabelas-SRC-e-SRD-?source=search)

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)
