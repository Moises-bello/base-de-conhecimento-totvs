---
article_id: 360038657433
category: Escrita Fiscal - Impostos - ICMS
content_hash: d8efdd96779eb4937e70e7854a68b12d474c18c06f345c7af93ffeb8f59402ba
fetched_at: '2026-06-28T22:39:25.583822+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configuração do campo
  Agrega Valor ( F4_AGREG )
type: support-article
updated_at: '2021-07-28T14:09:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038657433-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-do-campo-Agrega-Valor-F4-AGREG
---

**Dúvida**Qual a configuração do campo Agrega Valor ( F4\_AGREG )?

**Ambiente**  
Microsiga Protheus – Livros Fiscais– A partir da versão 11.80  
  
**Solução**

O agregador de valor dos tipos de entrada e saída tem como objetivo alterar a tratativa do valor da mercadoria:

S - O valor da mercadoria será agregado ao total do documento.  
N - O valor da mercadoria não será agregado ao total do documento. Esse valor poderá ser escriturado, ou não, conforme a parametrização do sistema MV\_LFAGREG.  
I - O valor da mercadoria não contém o valor do ICMS, portanto, o valor do ICMS e da mercadoria será agregado ao total do documento.  
A - O valor da mercadoria não contém o valor do ICMS, mas somente o valor da mercadoria será agregado ao total do documento. Note que a base de cálculo do ICMS sofrerá a incorporação do valor do ICMS.  
B - O valor da mercadoria não contém o valor do ICMS, portanto, o valor do ICMS e da mercadoria será agregado ao total do documento. Este agregador de valor não calcula nenhum imposto, mantendo-se o que for informado pelo usuário ou transmitido por outro sistema.  
C - O valor da mercadoria não contém o valor do ICMS, mas somente o valor da mercadoria será agregado ao total do documento. Note que a base de cálculo do ICMS sofrerá a incorporação do valor do ICMS. Este agregador de valor não calcula nenhum imposto, mantendo-se o que for informado pelo usuário ou transmitido por outro sistema.  
D - Deduz o valor do ICMS ou ISS, no caso de redução de base de cálculo, do valor contábil. Atenção! a dedução do Imposto será subtraída na base do PIS e COFINS. Deduzirá também no caso de Isenção por operação com cliente órgão público.  
E - Deduz o valor do ICMS embutido no valor da mercadoria.  
F - Deduz o valor da mercadoria do valor da duplicata.  
G - O valor a ser lançado na duplicata deverá ser somente o valor de ICMS do documento fiscal.  
H - Somente o valor do ICMS Retido será agregado ao total do documento fiscal.  
R - Deduz o valor do ICMS do valor unitário da mercadoria nos casos de redução de base de cálculo.
