---
article_id: 26197437790487
category: Encargos
content_hash: 78c7f38bf3dceff4333dfcb01c9d38eb25ca6655acb9d68e293908993db4618e
fetched_at: '2026-06-28T22:46:52.252202+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Lançamento financeiro tipo 24 - Total Guia FGTS Digital, gerar
  guia para o tipo Mensal
type: support-article
updated_at: '2024-09-06T19:53:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26197437790487-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-24-Total-Guia-FGTS-Digital-gerar-guia-para-o-tipo-Mensal
---

Tempo aproximado para leitura: 00:02:00 min**Dúvida**Como gerar o lançamento financeiro tipo 24 Total Guia FGTS Digital, gerar guia para o tipo Mensal.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos Patches 12.1.2306.264, 12.1.2310.213 e 12.1.2402.155  
**Solução**Acessar Encargos | Cadastros financeiros | Parâmetros, novo cadastro o código do lançamento assim como o tipo de documento e o fornecedor é especifico de cada organização incluir tipo de lançamento 24 Total Guia FGTS Digital, selecionar em gerar guia para o tipo : Mensal, na aba parâmetro do cadastro do lançamento, O parâmetro financeiro tipo 24 ele vai obedecer a parametrização do seu agrupamento, se informar por coligada ele vai gerar todos os lançamentos em um único lote financeiro e se fizer por seção ele irá gerar um para cada filial da coligada que está, é necessário cadastrar um lançamento ativo para cada tipo de guia assim como nossa orientação é cadastrar três parâmetros financeiros do tipo 24 Total Guia FGTS Digital um para cada tipo de guia o lançamento ativo é cadastrado na tabela dinâmica CODLANATIV:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197437739927)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197491663383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197437745303)

Com esse tipo de guia marcado ele vai considerar para o lançamento o FGTS mensal de funcionários ativos e FGTS de demitidos que tiveram o tipo de rescisão que não tem direito ao saque de FGTS e também casos de rescisão complementar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197491667351)

Geração do lançamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197491669143)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197491671703)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197437759383)

Caso utilizar rateio fixo no momento da geração do lançamento selecionar o rateio:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197437760791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197437761559)

Conforme rateio fixo do funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26197491677463)

Saiba mais:

[DT - FGTS Digital - Lançamento Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=834247089#Aba1-2)

[RH - RM - FOP - Lançamento financeiro tipo 24 Total Guia FGTS Digital para tipo de guia Rescisório + mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23727716648343-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-24-Total-Guia-FGTS-Digital-para-tipo-de-guia-Rescis%C3%B3rio-mensal#:~:text=O%20lan%C3%A7amento%20financeiro%20tipo%2024,marca%C3%A7%C3%A3o%20da%20flag%20FGTS%20M%C3%8AS)

[RH - RM - FOP - Incluir Lançamentos Ativos na Geração de Lançamentos Financeiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7763397883159-RH-RM-FOP-Incluir-Lan%C3%A7amentos-Ativos-na-Gera%C3%A7%C3%A3o-de-Lan%C3%A7amentos-Financeiros)
