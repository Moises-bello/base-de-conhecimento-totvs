---
article_id: 19542566715415
category: eSocial
content_hash: 6a5dece64451da0b7715bcf944838be20ffba4d88a0aa5447c6e45d0bd9a9436
fetched_at: '2026-06-28T22:47:15.378035+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500: Erro de schema: Element ''nrInsc'': [facet ''pattern'']
  The value '''' is not accepted by the pattern ''\d{11}|\d{14}'''
type: support-article
updated_at: '2024-09-27T17:03:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19542566715415-RH-RM-RHU-S-2500-Erro-de-schema-Element-nrInsc-facet-pattern-The-value-is-not-accepted-by-the-pattern-d-11-d-14
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19542581445527) Tempo aproximado para leitura: 00**:01:00 min**

**Dúvida**Ao gerar o XML do evento S-2500 aparece a mensagem de erro: **Erro de schema: Element 'nrInsc': [facet 'pattern'] The value '' is not accepted by the pattern '\d{11}|\d{14}'.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155**e superiores.  
  
**Solução**De acordo com o Leiaute do eSocial, o número de inscrição do contribuinte deve ser de acordo com o tipo de inscrição indicado no campo 'tpInsc'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19542613586711)

Sendo assim, ao informar no campo presente no sistema '**Informações de identificação do contribuinte (responsável direto), caso tenha havido imposição de responsabilidade indireta.**' que o tipo de inscrição é igual a **1 - CNPJ**, no campo referente ao **número de inscrição** é necessário que o mesmo possua **14 caracteres numéricos.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19542552061207)

Assim sendo, ao informar que o campo **'Tipo inscrição'** é igual a **2 - CPF**, o campo **'Número inscrição'** deve possuir **11 caracteres****numéricos**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19542597951127)

Após estes ajustes, salve as modificações feitas e gere o XML novamente para efetuar o envio do evento. 

**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

- [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543-RH-RM-RHU-eSocial-Processos-Trabalhistas-Perguntas-e-respostas-do-evento-webinar)

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783-RH-RM-RHU-eSocial-S-2500-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2500)

- [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855-RH-RM-RHU-eSocial-S-2501-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2501)
