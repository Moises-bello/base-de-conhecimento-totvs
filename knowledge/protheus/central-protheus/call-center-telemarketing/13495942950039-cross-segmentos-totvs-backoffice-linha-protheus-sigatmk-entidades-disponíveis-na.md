---
article_id: 13495942950039
category: Call Center - Telemarketing
content_hash: 2e4986fefc1bbd54031ce9a2dc0d21ae6e0156e059924ce51ec8d78c8222978d
fetched_at: '2026-06-28T22:41:29.461399+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Entidades disponíveis
  na inclusão de um Atendimento Telemarketing
type: support-article
updated_at: '2023-03-31T12:48:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13495942950039-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Entidades-dispon%C3%ADveis-na-inclus%C3%A3o-de-um-Atendimento-Telemarketing
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**De onde o sistema carrega as entidades da tela de inclusão do atendimento Telemarketing?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Todas as versões  
  
**Solução**Ao configurar o parâmetro **MV\_TMKF3** como .T., o sistema passa a apresentar, na inclusão de um atendimento do tipo "Telemarketing", a seguinte tela de seleção de entidades:

![Sele__o_de_Entidades.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13495722853911)

As entidades apresentadas para seleção, são carregadas das Tabelas Genéricas (SX5), para visualizar as entidades disponíveis basta acessar as tabelas genéricas acesse o Configurador (SIGACFG) e as opções:

Ambiente > Cadastros > Tabelas:

![Tabelas_Gen_ricas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13495824770711)

Nas Tabelas Genéricas, basta pesquisar pela tabela "T5", nela estarão as opções de entidades que devem ser apresentadas na tela do atendimento Telemarketing:

![T5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13495835772567)
