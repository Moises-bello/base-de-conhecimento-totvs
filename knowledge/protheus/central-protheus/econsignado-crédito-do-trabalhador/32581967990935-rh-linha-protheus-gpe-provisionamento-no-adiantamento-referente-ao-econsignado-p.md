---
article_id: 32581967990935
category: eConsignado (Crédito do Trabalhador)
content_hash: dc02a418b767420a2859325d404757b0afd9cc1bdbb892b61ba3eb0ccbb271c7
fetched_at: '2026-06-28T22:43:07.374050+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Provisionamento no Adiantamento referente ao Econsignado
  (Programa Crédito do Trabalhador MP1.292/2025)
type: support-article
updated_at: '2026-04-14T14:41:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32581967990935-RH-Linha-Protheus-GPE-Provisionamento-no-Adiantamento-referente-ao-Econsignado-Programa-Cr%C3%A9dito-do-Trabalhador-MP1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32581935304087) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como é feito o provisionamento no Adiantamento referente ao eConsignado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para realizar o cálculo de adiantamento com o **provisionamento** do empréstimo eConsignado referente ao programa de Crédito do Trabalhador, siga os passos abaixo:  
  
**1.** Realize a importação da parcela para valores futuros ou realizar o lançamento da natureza 9253 - No exemplo abaixo foi realizado a importação do arquivo para valores futuros com parcela de R$1500,00;

![](https://i.imgur.com/fDsjABB.png)

**2.** Para possibilitar o provisionamento do empréstimo referente ao Programa Crédito do Trabalhador no cálculo de adiantamento, foram criados três novos identificadores de calculo, sendo necessário a criação das verbas conforme artigo: [Como cadastrar as verbas de Provisionamento nas Férias e Adiantamento referente ao eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32292447017239-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador);

**3.** Realize o cálculo do adiantamento em **Miscelânea > Cálculos > Por Roteiro (GPEM020)**;

![](https://i.imgur.com/oGl6uC8.png)

![](https://i.imgur.com/HT95MsK.png)  
  
**4.** Consulte o calculo do adiantamento em **Consultas > Cálculos > Por Funcionário (GPEA090)**;

![](https://i.imgur.com/0bUcKvU.png)

Cálculo:

R$1500,00 (Parcela do eConsignado) \* 40% (Percentual do adiantamento no cadastro do funcionário SRA) = R$600,00  
  
**5.** Após realizar o **fechamento** do roteiro **ADI**, será gerado a verba de ID **1975** nos **lançamentos** por **Funcionários** (RGB), essa verba é referente a devolução do provisionamento; Ela terá origem **C** e o campo **Num. Identif.** estará em branco:

![](https://i.imgur.com/710JmHT.png)  
  
**6.** No calculo da Folha, será calculado o ID 1975 referente a devolução e será descontado efetivamente o valor do eConsignado de acordo com o limite da margem consignável:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32581967976343)  
  
**Margem consignável**  
Verbas de **provento** com **sim para INSS** + verbas informadas no **P\_ADICONS** - **INSS** - **IR** - verbas de **desconto** com **sim para INSS** - verbas informadas no **P\_DEDCONS**  
  
**Para maior conhecimento assista os videos How To abaixo:**

**Importante**  
A orientação é realizar uma provisão (retenção) no adiantamento que o trabalhador receber, podendo ser na **mesma proporção**, desta forma utiliza-se como **referência** o **percentual do adiantamento** que o funcionário recebe para o cálculo, e **não** o **limite de 35%** informado no mnemônico **P\_LIMECONS**, conforme entendimento da nossa [Consultoria de Segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-3.4Provis%C3%A3odoEmpr%C3%A9stimoConsignado-Adiantamento).

Para que o percentual do provisionamento do eConsignado no adiantamento seja diferente do informado no cadastro do funcionário, orientamos solicitar a melhoria do produto em nossa central colaborativa. [Central Colaborativa TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics).

**Saiba Mais**  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
