---
article_id: 19305877679895
category: eSocial
content_hash: 001b9ca6054a3044b9b9d4db2483a0509ea6a136f967bd21a28e5a6f57ee7f0a
fetched_at: '2026-06-28T22:47:15.386324+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500: Erro de schema: Element ''codMunic'': [facet ''pattern'']
  The value  is not accepted by the pattern ''\d{7}'''
type: support-article
updated_at: '2025-08-11T13:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19305877679895-RH-RM-RHU-S-2500-Erro-de-schema-Element-codMunic-facet-pattern-The-value-is-not-accepted-by-the-pattern-d-7
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19305877652503) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao gerar o XML do evento S-2500 aparece a mensagem de erro: **Erro de schema: Element 'codMunic': [facet 'pattern'] The value '' is not accepted by the pattern '\d{7}' (Erro de esquema: Elemento 'codMunic': [faceta 'padrão'] O valor '' não é aceito pelo padrão '\d{7}')**. O que fazer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155** e superiores.  
  
**Solução**De acordo com o layout disponibilizado pelo eSocial, o campo '**Município**' - **Informações Complementares disponível na guia Identificação do Processo** - deverá possuir 7 dígitos e ser um código válido que conste na tabela do IBGE:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34093665746199)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19305891032983)  
  
Acesse o site do IBGE através do link abaixo e busque pelo município desejado a fim de que possa obter a informação e preencher o campo corretamente:  
  
[Códigos dos municípios IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php)

**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543-RH-RM-RHU-eSocial-Processos-Trabalhistas-Perguntas-e-respostas-do-evento-webinar)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783-RH-RM-RHU-eSocial-S-2500-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2500)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855-RH-RM-RHU-eSocial-S-2501-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2501)
