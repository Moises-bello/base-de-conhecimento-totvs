---
article_id: 360021997171
category: Contabilidade Gerencial - Reprocessamento
content_hash: 036fe4314d3733aaa73cd5ca29835ff83286231b088e442e34bce27608656a63
fetched_at: '2026-06-28T22:40:41.952616+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Saldos não são atualizados
  com Stored Procedure.
type: support-article
updated_at: '2026-06-10T14:55:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021997171-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Saldos-n%C3%A3o-s%C3%A3o-atualizados-com-Stored-Procedure
---

**Ocorrência**  
As tabelas de saldos contábeis não são atualizadas quando são utilizadas com stored procedure.   
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - SIGACTB - A partir da versão 12.  
  
**Causa**  
Atualmente o sistema controla o auto-incremento na tabela caso o campo X2\_AUTREC contenha o valor "1"= Sim. Caso contrário '2' = Não este recurso é desabilitado.  
  
**Solução**  
Orientamos que o processo abaixo seja acompanhado de um DBA com conhecimento em Protheus, para adequação da base de dados.   
  
1. Ajustar o conteúdo dos campos X2\_AUTREC das tabelas de saldos (CQ0, CQ1, CQ2, etc..) com o conteúdo 2 (não habilitado),    
2. Garantir que os campos X2\_TAMFIL, X2\_TAMEMP e X2\_TAMUN estão corretamente preenchidos conforme o seu SIGAMAT,  
3. Backup das Tabelas de Saldo,   
4. Drop das Tabelas de Saldo,  
5. Recriação das tabelas pelo sistema,   
6. Restauração do Backup.
