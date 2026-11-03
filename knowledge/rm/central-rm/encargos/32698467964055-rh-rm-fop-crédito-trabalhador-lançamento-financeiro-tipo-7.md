---
article_id: 32698467964055
category: Encargos
content_hash: 4076c97e2a209fe673846186900769daabcf91289a482d597a7824ad32578048
fetched_at: '2026-06-28T22:46:52.212213+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Crédito trabalhador - Lançamento financeiro tipo 7
type: support-article
updated_at: '2025-06-11T12:10:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32698467964055-RH-RM-FOP-Cr%C3%A9dito-trabalhador-Lan%C3%A7amento-financeiro-tipo-7
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32698421693847) Tempo aproximado para leitura: 00**:02:00 min****Dúvida**Como realizar o lançamento financeiro para o crédito do trabalhador?  
  
**Ambiente**

* 12.1.2406.284
* 12.1.2410.247
* 12.1.2502.154
* 12.1.2506 e superiores

**Solução**

Para realizar o lançamento financeiro com o valor do evento de desconto do crédito trabalhador lançado no envelope do funcionário é necessário que cadastre um parâmetro financeiro com tipo 7 valor calculado por formula, exemplo:

Acessar **encargos | cadastros financeiros | parâmetros**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698467941527)

O cadastro do parâmetro financeiro deve ser realizado individualmente para cada banco ou instituição financeira responsável pelo financiamento do empréstimo. É importante ressaltar que deve ser criado um evento específico para cada banco, pois a fórmula utilizada faz referência direta a esse evento. Essa separação é necessária, uma vez que cada parâmetro financeiro contém informações bancárias distintas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698421695255)

Conforme o exemplo abaixo, foi utilizada a função de fórmula **MV**, informando o código do evento **480**, o mesmo que foi previamente cadastrado no empréstimo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698467943191)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698421698071)

É necessário cadastrar um **código ativo** para cada parâmetro financeiro:

**Saiba mais:** [RH - RM - FOP - Incluir Lançamentos Ativos na Geração de Lançamentos Financeiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7763397883159-RH-RM-FOP-Incluir-Lan%C3%A7amentos-Ativos-na-Gera%C3%A7%C3%A3o-de-Lan%C3%A7amentos-Financeiros)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698467944727)

Geração do lançamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698421701143)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698421701655)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698467946391)

O valor do lançamento financeiro é exatamente o valor retornado pela formula.

No FGTS Digital, o empregador poderá gerar guias que incluam valores referentes ao empréstimo consignado por meio das funcionalidades “**Emissão de Guia Rápida**” ou “**Emissão de Guia Parametrizada**”.

**Saiba mais :** [Espaço legislação - Crédito do Trabalhador](https://espacolegislacao.totvs.com/credito-do-trabalhador/#fluxo-operacional-para-o-empregador)
