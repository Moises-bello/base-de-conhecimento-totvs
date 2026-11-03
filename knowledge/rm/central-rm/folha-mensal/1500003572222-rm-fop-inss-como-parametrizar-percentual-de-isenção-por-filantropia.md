---
article_id: 1500003572222
category: Folha Mensal
content_hash: 3145ae68dc92c1a63849e2009df69e689889d722e4216071ee7c153803353dc6
fetched_at: '2026-06-28T22:46:59.421276+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RM - FOP - INSS: Como parametrizar percentual de isenção por filantropia '
type: support-article
updated_at: '2021-06-18T13:21:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003572222-RM-FOP-INSS-Como-parametrizar-percentual-de-isen%C3%A7%C3%A3o-por-filantropia
---

**Dúvida**

Como parametrizar percentual de isenção de filantropia?   
  
**Ambiente**

RM - Folha de pagamento - Todas as versões  
  
**Solução**

Para uma empresa ser enquadrada como filantrópica e ter a isenção de contribuições para a seguridade social, ela deverá ter a certificação das entidades beneficentes, de acordo com o art. 1° da Lei n° 12.101/2009.

> ***Lei 12.101/2009***
>
> ***Art. 1o  A certificação das entidades beneficentes de assistência social e a isenção de contribuições para a seguridade social serão concedidas às pessoas jurídicas de direito privado, sem fins lucrativos, reconhecidas como entidades beneficentes de assistência social com a finalidade de prestação de serviços nas áreas de assistência social, saúde ou educação, e que atendam ao disposto nesta Lei.***
>
> ***(...)***

Para parametrizar esse percentual de isenção é necessário acessar o cadastro da seção, aba Dados p/ INSS, informar opção "1 - Não optante" e informar percentual de isenção de filantropia:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003576562/mceclip0.png)  
  
O Percentual de isenção de filantropia será considerado para redução das bases de cálculo das contribuições previdenciárias. Somente empresas que são beneficentes deverão informar o percentual de isenção.

**Atenção:**  
Quando a empresa tem 100% de Isenção de Filantropia (FPAS 639), o campo "Percentual de Acid.de Trabalho" deve ser zerado. Desta forma, o programa SEFIP será validado corretamente.

Caso o Faturamento Bruto esteja preenchido com valor da receita bruta e a competência do sistema seja a partir de 12/2011, o valor do campo Empresa será zerado na guia de INSS, pois o valor deste campo será recolhido via DARF.

Esta regra valerá para quaisquer segmentos que estejam com este valor preenchido no cadastro de seções a partir de 12/2011, exceto produtor rural. Portanto, este campo deverá ser preenchido somente se a empresa se encaixar nos parâmetros da Lei.

**Saiba mais:**

<http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12546.htm>
