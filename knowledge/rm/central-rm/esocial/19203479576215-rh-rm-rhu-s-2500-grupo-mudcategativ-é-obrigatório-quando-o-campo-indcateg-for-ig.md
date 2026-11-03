---
article_id: 19203479576215
category: eSocial
content_hash: ca812bb7964bd4ba124877d1b49cb15a62404661b2705d8dcc33a40efc8babeb
fetched_at: '2026-06-28T22:47:15.390822+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: RH - RM - RHU - S-2500 - 'Grupo mudCategAtiv é obrigatório quando o campo 'indCateg'
  for igual a [S] ou o campo 'indNatAtiv' for igual a [S]'
type: support-article
updated_at: '2025-08-11T13:44:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19203479576215-RH-RM-RHU-S-2500-Grupo-mudCategAtiv-%C3%A9-obrigat%C3%B3rio-quando-o-campo-indCateg-for-igual-a-S-ou-o-campo-indNatAtiv-for-igual-a-S
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19203475063959) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao gerar o XML do evento S-2500, é exibida a seguinte mensagem de erro: **Grupo mudCategAtiv é obrigatório quando o campo 'indCateg' for igual a [S] ou o campo 'indNatAtiv' for igual a [S].**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155**e superiores.  
  
**Solução**

O erro ocorre quando os campos Reconhecimento de Categoria e/ou Reconhecimento da natureza atividade presentes no cadastro do Contrato de Trabalho > Guia Informações Gerais, forem iguais a 'Sim'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34093312547863)

Conforme estabelecido pelo Leiaute do eSocial, quando estes campos forem iguais a 'Sim', os campos referentes ao cadastro de 'Informação do novo código de categoria e/ou da nova natureza da atividade' deverão ser obrigatórios, se existir na condição. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19203491051799)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34093312550423)

Sendo assim, deverão preencher este cadastro presente em Contrato de Trabalho > Guia Informações Gerais > Informação do novo código de categoria e/ou da nova natureza da atividade.

Após realizar a inclusão do período no cadastro do contrato, salve as modificações feitas na visão e realize a geração do XML novamente para efetuar o envio.

**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
