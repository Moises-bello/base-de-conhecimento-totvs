---
article_id: 7080703725975
category: SIGAEST - LEGAIS
content_hash: 88f3c737038b5614c1dcefb1dbb0cb2fff5031613920c93d4e24ba7d497bb6d7
fetched_at: '2026-06-28T22:38:51.885080+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPEDFISCAL - TOP Error
  -19 - [ERROR] (from tDBServer::ROP_CREATEFILE - table K_K200_*******) Invalid operation
  with active transaction
type: support-article
updated_at: '2022-08-09T19:17:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7080703725975-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPEDFISCAL-TOP-Error-19-ERROR-from-tDBServer-ROP-CREATEFILE-table-K-K200-Invalid-operation-with-active-transaction
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:29 min****Ocorrência**Ao processar o SPED Fiscal com o Bloco K é exibido o seguinte error.log:

*"TOP Error -19 - [ERROR] (from tDBServer::ROP\_CREATEFILE - table K\_K200\_\*\*\*\*\*\*\*) Invalid operation with active transaction."*

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**  
Esse incidente ocorre pois o DBAccess não consegue fazer a chamada da criação do arquivo temporário K\_K200\_\*\*\*\*\*\*\*.  
  
**Solução**A última versão do DBAccess trata de contemplar o suporte a um novo tipo de tabela temporária, que pode ser acessada em modo compartilhado por múltiplas conexões, permitindo com que o processamento consiga gerar corretamente a tabela temporária inicial para o correto processamento dos Registros do Bloco K.

Para efetuar o Download desta versão do DBAccess, clique no link abaixo:

**[DBAccess atualizado](https://suporte.totvs.com/portal/p/10098/download#detail/1031464)**

OBS: Sempre atualizar ambientes sempre em ambiente de homologação.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
