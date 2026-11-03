---
article_id: 19202369828503
category: eSocial
content_hash: 6be517859a98c030065609ff24271aa5b6efaebe9abb554a8b8da1ffc3c67120
fetched_at: '2026-06-28T22:47:15.395134+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500: Erro: código 1765: Quando tpContr = [1, 2], o campo
  deve ser igual ou anterior ao mes/ano da data de desligamento.'
type: support-article
updated_at: '2025-08-11T13:54:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19202369828503-RH-RM-RHU-S-2500-Erro-c%C3%B3digo-1765-Quando-tpContr-1-2-o-campo-deve-ser-igual-ou-anterior-ao-mes-ano-da-data-de-desligamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19202374407575) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Ao gerar o XML do evento S-2500, é exibida a seguinte mensagem de erro: Erro: código 1765: Quando quot;tpContrquot; = [1, 2], o campo deve ser igual ou anterior ao mes/ano da data de desligamento.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155**e superiores.  
  
**Solução**

A mensagem de erro ocorre quando o tipo de Contrato de Trabalho for igual a 1 ou 2, conforme destacado na imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26718190114199)

Sendo assim, quando o tipo de contrato for 1 ou 2, a data da competência final, localizada em Contrato de Trabalho > Guia Informações Gerais > Informações dos períodos e valores decorrentes de processo trabalhista e ainda não declarados no eSocial, deverá ser uma data igual ou anterior a data de desligamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19203637234583)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26718190116375)

Após realizar estes ajustes no cadastro do contrato de trabalho, salve as modificações feitas na visão e realize a geração do XML novamente para efetuar o envio. 

**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
