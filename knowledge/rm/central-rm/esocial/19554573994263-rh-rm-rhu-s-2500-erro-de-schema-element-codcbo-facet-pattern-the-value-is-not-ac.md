---
article_id: 19554573994263
category: eSocial
content_hash: 54a9784d1bb8c04306675dc1fa5e415ff7b667f4e4d3af1a73075e258df7fd9f
fetched_at: '2026-06-28T22:47:15.367779+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500: Erro de schema: Element ''codCBO'': [facet ''pattern'']
  The value is not accepted by the pattern ''\d{6}'''
type: support-article
updated_at: '2026-03-06T17:08:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19554573994263-RH-RM-RHU-S-2500-Erro-de-schema-Element-codCBO-facet-pattern-The-value-is-not-accepted-by-the-pattern-d-6
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19554573926039) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao gerar o XML do evento S-2500 aparece a mensagem de erro: **Erro de schema: Element 'codCBO': [facet 'pattern'] The value 'XXXX-X' is not accepted by the pattern '\d{6}'**. O que fazer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155** e superiores.  
  
**Solução**De acordo com o layout disponibilizado pelo eSocial, o campo '**Classificação Brasileira de Ocupações - CBO**' - **guia Informações Complementares disponível no cadastro do contrato de trabalho** -  deve ser preenchido com um código válido e existente na tabela de CBO, com 6 (seis) posições:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26679717298199)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26679717300887)  
  
Acesse o site [**CBO**](https://cbo.mte.gov.br) e no menu **Downloads** você poderá visualizar e baixar o arquivo '**Listagem da CBO - Arquivo PDF**'.  
  
Após isso, identifique o código que representa a Classificação Ocupacional desejada e cadastre-o corretamente no campo **Classificação Brasileira de Ocupações - CBO**' - **guia Informações Complementares disponível na cadastro do contrato de trabalho**, para envio correto do xml do evento.

**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543-RH-RM-RHU-eSocial-Processos-Trabalhistas-Perguntas-e-respostas-do-evento-webinar)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783-RH-RM-RHU-eSocial-S-2500-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2500)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855-RH-RM-RHU-eSocial-S-2501-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2501)
