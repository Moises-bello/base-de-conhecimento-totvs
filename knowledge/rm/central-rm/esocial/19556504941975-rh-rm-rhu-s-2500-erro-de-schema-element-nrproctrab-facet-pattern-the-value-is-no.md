---
article_id: 19556504941975
category: eSocial
content_hash: 1c0ed0f3fa81414db28fa46e31efb235fd98a7f79d085a738d9c92be2c60e007
fetched_at: '2026-06-28T22:47:15.359491+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500: Erro de schema: Element ''nrProcTrab'': [facet ''pattern'']
  The value is not accepted by the pattern ''\d{15}|\d{20}''.'
type: support-article
updated_at: '2023-12-15T20:34:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19556504941975-RH-RM-RHU-S-2500-Erro-de-schema-Element-nrProcTrab-facet-pattern-The-value-is-not-accepted-by-the-pattern-d-15-d-20
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19556504921879) Tempo aproximado para leitura: **00****:01:06 min**

**Dúvida**Ao gerar o XML do evento S-2500 aparece a mensagem de erro: **Erro de schema: Element 'nrProcTrab': [facet 'pattern'] The value is not accepted by the pattern '\d{15}|\d{20}'.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155**e superiores.  
  
**Solução**

A mensagem de erro ocorre devido ao número de caracteres numéricos informados no campo **'Número do processo'**presente na guia **'Identificação do processo'.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19556468087703)**

Conforme estabelecido pelo Leiaute do eSocial, o campo deverá possuir 15 ou 20 caracteres numéricos, de acordo com a '**Origem'** que for informada. Segue a regra abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19556451502231)

Por tratar-se de um campo chave, uma vez que o processo for cadastrado e salvo, não há como editar os campos referente a **'Origem'** e '**Número do processo'**. Sendo assim, deverão excluir o processo cadastrado com a quantidade de caracteres incorretos e realizar o cadastro de um novo registro, informando o número do processo corretamente.

**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543-RH-RM-RHU-eSocial-Processos-Trabalhistas-Perguntas-e-respostas-do-evento-webinar)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783-RH-RM-RHU-eSocial-S-2500-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2500)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855-RH-RM-RHU-eSocial-S-2501-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2501)
