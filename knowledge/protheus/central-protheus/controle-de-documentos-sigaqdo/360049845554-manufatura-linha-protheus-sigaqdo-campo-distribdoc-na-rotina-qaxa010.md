---
article_id: 360049845554
category: Controle de Documentos (SIGAQDO)
content_hash: 56425ced2604b3cdd6d611a0da6b5aea9ef2ed3895c8b3ff18a5ca32b715edb3
fetched_at: '2026-06-28T22:42:28.964830+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Campo Distrib.Doc na rotina QAXA010
type: support-article
updated_at: '2021-05-11T17:21:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049845554-Manufatura-Linha-Protheus-SIGAQDO-Campo-Distrib-Doc-na-rotina-QAXA010
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:35 min**  
**Dúvida**Qual a função do campo **Distrib.Doc**na rotina **QAXA010 - Cadastro de Usuários**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**O campo **Distrib.Doc**, registra a permissão do usuário em distribuir um documento. O uso deste campo permite ter vários usuários responsáveis em distribuição, usando o princípio de serem controlados no documento pelo campo **Cod Dep Dst**na rotina **QDOA020 - Tipos de Documento.**  
**Exemplo**No departamento 01 existem três usuários com **Distrib.Doc** igual **1-Sim**, portanto, os três receberão cada um, uma pendência de distribuição do documento que já foi previamente definida na rotina **QDOA020**, no campo **Cod Dep Dst**.
