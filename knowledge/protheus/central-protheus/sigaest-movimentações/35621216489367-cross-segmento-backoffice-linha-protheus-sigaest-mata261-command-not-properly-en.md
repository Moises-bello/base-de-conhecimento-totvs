---
article_id: 35621216489367
category: SIGAEST - MOVIMENTAÇÕES
content_hash: dbd96c9b201b8260c4714d32de24133d05ec2da63c78628eb1bfe8cd1ed22fb5
fetched_at: '2026-06-28T22:38:57.023394+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA261 - command
  not properly ended SELECT COALESCE SD3 DOCMAX
type: support-article
updated_at: '2025-10-30T11:27:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35621216489367-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-command-not-properly-ended-SELECT-COALESCE-SD3-DOCMAX
---

O erro ORA-00933 ocorre na rotina MATA261 ao tentar transferir lote com data de validade inferior. A correção permite a transferência mesmo com data inferior no lote destino. Atualize para as versões 12.1.2210, 12.1.2310 ou 12.1.2410 disponíveis no Portal de Clientes, realizando backup e testes antes da atualização.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35621216482071) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar realizar uma transferencia via rotina MATA261 ocorre o erro:

THREAD ERROR  
Error : 933 - ORA-00933: SQL command not properly ended SELECT COALESCE SD3 DOCMAX  
SELECT COALESCE(SD3.DOCMAX,'000000000') AS DOCMAX FROM (SELECT D3\_DOC AS DOCMAX,ROW\_NUMBER() OVER ( ORDER BY  D3\_DOC DESC) AS LINHA FROM SD3010 WHERE  D3\_FILIAL = :1 AND D3\_DOC >= :2 AND D\_E\_L\_E\_T\_ = :3 )  AS SD3 WHERE  SD3.LINHA = 2  on A261CDOC(MATA261.PRX) 26/08/2024 19:00:04 line : 5287  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**  
A rotina de Transferência Múltipla não permite movimentar informando um novo lote destino com data de validade inferior.  
Efetuado ajuste para rotina de Transferência Múltipla permitir movimentar informando um novo lote destino com data de validade inferior.

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1187610> ;

12.1.2310:<https://suporte.totvs.com/portal/p/10098/download?e=1187609> ;

12.1.2410:<https://suporte.totvs.com/portal/p/10098/download?e=1187608> ;

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://suporte.totvs.com/portal/p/10098/download#000006/all/)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização.  
Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
