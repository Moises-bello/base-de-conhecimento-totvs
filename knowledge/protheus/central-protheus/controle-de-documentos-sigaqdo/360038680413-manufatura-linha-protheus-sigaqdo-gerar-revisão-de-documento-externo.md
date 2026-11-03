---
article_id: 360038680413
category: Controle de Documentos (SIGAQDO)
content_hash: f8e614b3570e49c14036bc974ac7f25d6ec060fd4671a3e9b4ce5e9031a6d864
fetched_at: '2026-06-28T22:42:29.097495+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Gerar revisão de documento externo
type: support-article
updated_at: '2021-05-21T13:01:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038680413-Manufatura-Linha-Protheus-SIGAQDO-Gerar-revis%C3%A3o-de-documento-externo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Na rotina **QDOA050 - Controle de Documentos** ao gerar revisão de documento externo, como utilizar o mesmo documento da revisão anterior?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Para que seja utilizado o mesmo documento da revisão anterior é necessário que o parâmetro **MV\_QDUPEXT - Define se Visualiza/Altera/Exclui o documento externo na inclusão/alteração e copia o documento anterior na geração de Revisão** tenha conteúdo igual à **1-Sim**. Caso o parâmetro tenha conteúdo igual à **2-Não**, ao gerar nova revisão será solicitado ao usuário para informar qual é o documento relacionado à esta nova revisão.
