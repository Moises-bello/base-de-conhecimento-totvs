---
article_id: 26247617625751
category: Encargos
content_hash: a40f3e2e5c7a2a039e34f9f33884437784104cdca9ce9d1d878e0c3e17e697a7
fetched_at: '2026-06-28T22:46:52.247380+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Lançamento financeiro tipo 24 Total Guia FGTS Digital para
  tipo de guia Rescisório
type: support-article
updated_at: '2026-04-24T17:40:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26247617625751-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-24-Total-Guia-FGTS-Digital-para-tipo-de-guia-Rescis%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26247617598103) Tempo aproximado para leitura: **00:02:00 min**

Dúvida  
Como gerar o lançamento financeiro FGTS Digital para parametrização tipo de guia rescisório ?

Ambiente  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos Patches 12.1.2306.264, 12.1.2310.213 e 12.1.2402.155

Solução

Cadastrar o parâmetro financeiro em Encargos | cadastros financeiros| parâmetros, incluir novo parâmetro selecionando o tipo de guia rescisório, ele irá levar funcionários demitidos que e tiveram o tipo de rescisão com direito ao saque de FGTS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26247626289431)

O lançamento financeiro tipo 24 irá gerar conforme a parametrização feita em seu agrupamento podendo ser por filial, coligada ou lotação tributaria.

Orientamos a ter três cadastros do parâmetro financeiro um para cada tipo de guia, associado cada um a código ativo diferente para cada lançamento, criação de novos códigos ativos são feitos na tabela dinâmica Codlanativ.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26247617604503)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26247626296343)

Exemplo de geração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26247617608471)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26247617610135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26247626305047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26247617613207)

Saiba mais:

[RH - RM - FOP - Lançamento financeiro tipo 24 Total Guia FGTS Digital para tipo de guia Rescisório + mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23727716648343-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-24-Total-Guia-FGTS-Digital-para-tipo-de-guia-Rescis%C3%B3rio-mensal#:~:text=O%20lan%C3%A7amento%20financeiro%20tipo%2024,marca%C3%A7%C3%A3o%20da%20flag%20FGTS%20M%C3%8AS)

[RH - RM - FOP - Lançamento financeiro tipo 24 - Total Guia FGTS Digital, gerar guia para o tipo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26197437790487-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-24-Total-Guia-FGTS-Digital-gerar-guia-para-o-tipo-Mensal)

[DT - FGTS Digital - Lançamento Financeiro](https://tdn.totvs.com.br/pages/releaseview.action?pageId=834247089)
