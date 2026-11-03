---
article_id: 360039695453
category: ADVPL - Classe e Função
content_hash: 6a320392d2a315ba164a879fede1f20b677c89fb3f487b13185015e7700521fb
fetched_at: '2026-06-28T22:40:14.369570+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alterar TIMEOUT:
  RecLock e SoftLock'
type: support-article
updated_at: '2022-04-13T12:37:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039695453-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Alterar-TIMEOUT-RecLock-e-SoftLock
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Existe algum recurso ou e possível estabelecer um timeout para a tentativa de reserva de registros pelas funções *RecLock()* e *SoftLock()*?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.17.  
  
**Solução**Não é possível alterar Timeout.   
Na tela que retorna para o usuário decidir se quer terminar a busca ou abortar o sistema.  
Neste momento o processo está utilizando a função *Simplelock()*, e caso o *lock* no registro possa ser realizado é chamada a função *Recklock()*.  
Caso o registro esteja bloqueado é necessário desenvolver as tratativas para tratar esse registro em um outro momento.  
  
**Saiba mais**  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro timeout em consumo de WebService](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027401212)  
[SimpleLock - Realiza o bloqueio de edições (reserva) do registro.](https://tdn.totvs.com/display/PROT/SimpleLock) [DBRLockList - Retorna um array com a lista de registros bloqueados na tabela da thread atual](https://tdn.totvs.com/display/tec/DBRLockList)
