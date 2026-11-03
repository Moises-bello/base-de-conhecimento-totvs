---
article_id: 360046628474
category: Controle de Documentos (SIGAQDO)
content_hash: d29fe229f58d762c2bacff5097c4787a3c163606e8e85e48376dbb8702b8b4b0
fetched_at: '2026-06-28T22:42:29.095240+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Geração de pendência de distribuição
type: support-article
updated_at: '2025-02-12T14:42:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046628474-Manufatura-Linha-Protheus-SIGAQDO-Gera%C3%A7%C3%A3o-de-pend%C3%AAncia-de-distribui%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29933036459287)**Tempo aproximado para leitura:**00:00:40 min**  
**Dúvida**Quando é gerada a **pendência de distribuição**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**A **pendência de distribuição** é gerada para todos os usuários que estiverem no mesmo **departamento** que foi relacionado na rotina **QDOA020 - Tipos de Documento** e que estejam parametrizados na rotina **QAXA010 - Usuários** para distribuir o documento. O vínculo do usuário distribuidor é automático na primeira revisão do documento. As demais revisões do documento manterão o cadastro da revisão anterior e os usuários distribuidores não serão atualizados automaticamente.  
Na rotina **QDOA050 - Cadastro de Documento** é possível alterar, incluir e excluir o usuário distribuidor, acessando o documento em indo em **Outras Ações > Distrib**.
