---
article_id: 4859217662359
category: Controle de Documentos (SIGAQDO)
content_hash: aed6a823bb93cfd6e95cb6aeb394a146ff25517db475402a12880d7390cc7783
fetched_at: '2026-06-28T22:42:29.264629+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - QDOA050 - Existe pendência de Solicitação
  de Alteração neste Documento
type: support-article
updated_at: '2022-03-18T20:12:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4859217662359-Manufatura-Linha-Protheus-SIGAQDO-QDOA050-Existe-pend%C3%AAncia-de-Solicita%C3%A7%C3%A3o-de-Altera%C3%A7%C3%A3o-neste-Documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:15 min****Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao gerar revisão de um documento por meio da rotina **QDOA050 - Controle de Documentos** é apresentada a mensagem **Existe pendência de Solicitações de Alteração neste Documento. Usuário não autorizado a gerar revisão**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esta mensagem é apresentada na geração da revisão do documento, quando existe alguma pendência para o documento em questão na tabela **QDP - Solicitações**, incluída pela rotina **QDOA052 - Cadastro de Solicitações** e o parâmetro **MV\_QDBLORV - Define o bloqueio do botão Gera Revisão quando há solicitações pendentes** estiver definido como **1-Sim**.  
  
**Solução**Para que esta mensagem não seja apresentada e seja possível gerar a revisão do documento, temos as seguintes opções de parametrização para o parâmetro **MV\_QDBLORV**:  
1. Quando estiver com conteúdo igual à **1-Sim**: é necessário realizar a baixa das solicitações por meio da rotina **QDOA052** em **Outras Ações/Baixar**;  
2. Conteúdo igual à **2-Não**: a geração da revisão é liberada, mesmo existindo pendência de solicitações, porém também é possível baixar a solicitação conforme descrito no passo acima.
