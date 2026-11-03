---
article_id: 360059782414
category: Escrita Fiscal - Impostos - ICMS
content_hash: 4517c711f60f6aa28d22b255a2af1514ed4e148daf23c877b51710172037a668
fetched_at: '2026-06-28T22:39:26.035703+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: MP - FIS - Alteração de Alíquota de ICMS Conforme o Decreto 65.253/2020
type: support-article
updated_at: '2021-05-31T14:24:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059782414-MP-FIS-Altera%C3%A7%C3%A3o-de-Al%C3%ADquota-de-ICMS-Conforme-o-Decreto-65-253-2020
---

**Dúvida**

Como configurar o sistema para atender a alteração de alíquota de ICMS, conforme o decreto 65.253/2020?

**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12

**Solução**

Entendemos que o decreto trata alterações de alíquotas, a configuração pode ser tratada via cadastro de produto ou exceção fiscal conforme abaixo:

**Cadastro de Produtos**B1\_PICM

**Exceção fiscal**F7\_ALIQINT

As alterações são para as alíquotas internas no estado de SP, as vendas saindo de SP para qualquer outro estado assume as alíquotas interestaduais:  
  
4%  
7%  
12%

Documentação Referente Exceção Fiscal:

[MP FIS - Exceções Fiscais (MATA540) - Todos os campos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047488214-MP-FIS-Exce%C3%A7%C3%B5es-Fiscais-MATA540-Todos-os-campos?source=search)

Parecer Consultoria de Segmentos:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=574900258>
