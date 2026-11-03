---
article_id: 360000731448
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: cff9dfb7061073742dd739e4a2bb51951fe38de79174b5d045b3e4494090184d
fetched_at: '2026-06-28T22:38:30.043418+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Uso Moeda Modulo
  Faturamento
type: support-article
updated_at: '2026-03-26T14:41:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000731448-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Uso-Moeda-Modulo-Faturamento
---

**Dúvida**

Como utilizar o cadastro de moedas no modulo faturamento?  
  
**Ambiente**

Cross Segmentos- TOTVS Backoffice (Linha Protheus)- SIGAFAT – A partir da versão 11.80.  
  
**Solução**

No módulo faturamento é realizada a seguinte configuração:

1. A primeira moeda sempre será REAL;

2. No Pedido de Venda preencher o campo **C5\_MOEDA** de acordo com a moeda desejada, a qual deve estar registrada no cadastro de moedas (**SM2**);

**Obs**: **No pedido de venda nunca haverá conversão de moeda. A conversão será realizada no Documento de saída - Tabelas SD2 e SF2;**

Para que seja gerado o Titulo na moeda corrente (Real) ou na moeda de conversão registrada no **C5\_MOEDA** (Ex: Dollar) é necessário definir no parâmetro **MV\_MOEDTIT**.

**Saiba Mais:****[Como utilizar o cadastro de moedas no modulo faturamento?](http://tdn.totvs.com/display/public/PROT/FAT0096_Uso_Moeda_Modulo_Faturamento)**

**Importante:** - Dúvida sobre baixa de título em lote ou baixa de título em outra moeda, deve ser verificado o artigo: **[Cross Segmento BackOffice Linha Protheus - SIGAFIN - FINA080 - Taxa contratada na baixa por lote dos titulos em moeda estrangeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406434720663-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-FINA080-Taxa-contratada-na-baixa-por-lote-dos-titulos-em-moeda-estrangeira?source=search)**

**Dúvidas no processo, contate a equipe de atendimento de Financeiro.**
