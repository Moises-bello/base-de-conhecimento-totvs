---
article_id: 19573360885271
category: eSocial
content_hash: b203a8ba38baff8ff476f30153b1363f18748b24576e2d5c93b77bf944a2ad28
fetched_at: '2026-06-28T22:47:15.355348+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500: Erro de schema: nrInsc'': [facet ''pattern''] The
  value ''XXXXXXXXX'' is not accepted by the pattern ''\d{12}|\d{14}'''
type: support-article
updated_at: '2025-09-19T19:35:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19573360885271-RH-RM-RHU-S-2500-Erro-de-schema-nrInsc-facet-pattern-The-value-XXXXXXXXX-is-not-accepted-by-the-pattern-d-12-d-14
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19573360864791) Tempo aproximado para leitura: **00:01:15 min****Dúvida**Ao gerar o XML do evento S-2500 aparece a mensagem de erro: **Erro de schema: nrInsc': [facet 'pattern'] The value 'XXXXXXXXX' is not accepted by the pattern '\d{12}|\d{14}'**. O que fazer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155** e superiores.  
  
**Solução**De acordo com o leiaute disponibilizado pelo eSocial, o campo '**Número de inscrição**' - **guia Identificação do estabelecimento, disponível no cadastro do contrato de trabalho** -  deve ser preenchido com 12 ou 14 dígitos:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30248800345879)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19573345272215)  
  
Para ajustar o cenário e realizar o envio sem que a mensagem de erro seja exibida, acesse o **contrato de trabalho do Processo Trabalhista**, edite-o e ajuste o campo **Número de inscrição** com a inscrição correta contendo 12 ou 14 posições e seguindo as orientações de validação exibidas na segunda imagem, retirada do Leiaute do eSocial.  
  
**Importante**  
Conforme pontuado na segunda imagem, retirada do Layout do eSocial, no caso de empregador doméstico, informar os 9 (nove) primeiros dígitos do CPF do empregador, seguidos de 5 (cinco) dígitos 0 (zero). Por exemplo, se o CPF do empregador doméstico for 111111111-99, informar 11111111100000.   
  
**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543-RH-RM-RHU-eSocial-Processos-Trabalhistas-Perguntas-e-respostas-do-evento-webinar)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783-RH-RM-RHU-eSocial-S-2500-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2500)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855-RH-RM-RHU-eSocial-S-2501-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2501)
