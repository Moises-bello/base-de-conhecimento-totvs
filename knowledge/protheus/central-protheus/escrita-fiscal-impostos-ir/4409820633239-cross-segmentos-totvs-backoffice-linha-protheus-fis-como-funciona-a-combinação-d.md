---
article_id: 4409820633239
category: Escrita Fiscal - Impostos - IR
content_hash: e2a57a41a0f7f0baca38c6dbed8c7858faa77520d7b02d63935e7e77a7fe89d5
fetched_at: '2026-06-28T22:39:31.916994+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como funciona a combinação
  das configurações do campo "Recolhe IRRF" (ED_RECIRRF) da natureza com o campo A1_RECIRRF
  do cadastro de clientes ?
type: support-article
updated_at: '2021-10-01T12:49:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409820633239-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-funciona-a-combina%C3%A7%C3%A3o-das-configura%C3%A7%C3%B5es-do-campo-Recolhe-IRRF-ED-RECIRRF-da-natureza-com-o-campo-A1-RECIRRF-do-cadastro-de-clientes
---

**Dúvida**

Como funciona a combinação das configurações do campo "Recolhe IRRF" (ED\_RECIRRF) da natureza com o campo A1\_RECIRRF do cadastro de clientes ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões]  
  
**Solução**

Quando a natureza está configurada para reter IR (ED\_CALCIRF = Sim), é verificado as seguintes combinações para a retenção:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409820607127/mceclip0.png)

A verificação da cumulatividade é feita por cliente, independente se o tributo foi gerado para o cliente ou para o emitente.

**Exemplo:**

Temos um cadastro do cliente AAA configurado como Recolhe IRRF = Sim.

Natureza IR1 : configurada para calcular IR (1,5%) e Recolhe IRRF = SIM

Natureza IR2 : configurada para calcular IR (1,5%) e Recolhe IRRF = NAO

Incluir um titulo abaixo do valor mínimo de retenção:

TIT 1 : valor de 100,00, natureza IR1

Como o valor do IR calculado não atinge o valor mínimo configurado, não haverá retenção, portanto será gravado desta forma na SE1:

|  |  |
| --- | --- |
| E1\_VALOR | 100,00 |
| E1\_VRETIRF ( valor calculado de IR para o título) | 1,50 |
| E1\_IRRF ( valor retido de IR) | 0,00 |

Incluir o segundo titulo atingindo o valor mínimo de retenção porém com outra natureza:

TIT 2 : valor de 1000,00, natureza IR2

Como o valor do IR atual + anterior atinge o valor mínimo configurado, haverá a retenção acumulada, portanto será gravado desta forma na SE1 no título principal:

|  |  |
| --- | --- |
| E1\_VALOR | 1000,00 |
| E1\_VRETIR( valor calculado de IR para o título) | 15,00 |
| E1\_IRRF ( valor retido de IR acumulado) | 16,50 |

E será gerado um registro de IR- no valor de 15,00 no contas a receber e um registro do tipo TX no valor de 1,50 no contas a pagar.

Mesmo que houve a retenção para o emitente, em E1\_IRRF será gravado o valor total retido, porém na baixa deste título 2, deverá considerar somente o valor do IR- gerado para o cliente, no caso de 15,00.

**Informações adicionais:**

<https://tdn.totvs.com/display/public/PROT/FIN0002_CREC_Duvidas_sobre_ED_RECIRRF>

<https://tdn.totvs.com/pages/releaseview.action?pageId=47908805>
