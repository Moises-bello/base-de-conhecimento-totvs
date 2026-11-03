---
article_id: 360018590551
category: ADVPL - Classe e Função
content_hash: 649f77ccc3c9f441dcd1b3e9e73d1c9d35e1e9838191bae180f0a225a963c84d
fetched_at: '2026-06-28T22:40:15.738917+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Deadload (reclock
  sem saída) nas tabelas sa1,sa2 ou sb2
type: support-article
updated_at: '2022-01-05T15:21:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018590551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Deadload-reclock-sem-sa%C3%ADda-nas-tabelas-sa1-sa2-ou-sb2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:04:00 min  
  
Ocorrência**Durante o processamento do sistema, ocasionalmente ocorre um travamento de duas ou mais threads de banco em uma mesma tabela.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.16  
  
**Causa**Este erro ocorre por conta de um evento chamado *deadlock*, ao qual a transação 1 tenta efetuar o bloqueio de uma tabela, porém essa tabela já se encontra travada pela transação 2, contudo a transação 1 precisa da tabela a qual a transação 2 está travando:  
  
![TRANSA__O.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360013959851/TRANSA__O.jpg)  
  
![](https://pedrogalvaojunior.files.wordpress.com/2011/11/deadlocks.jpg)  
  
**Solução**Utilizar o parâmetro MV\_FATTRAV para efetuar travamento (*lock*) sob demanda dos registros.  
Por padrão o Protheus efetua o *lock*total da tabela ao efetuar um operação de manipulação de dados, uma vez que este parâmetro esteja configurado com uma das tabelas acima (SA1, SA2 ou SB2), será efetuado um espécie de *lock on demand* (travamento sob demanda), ao qual ao invés de travar a tabela completamente, irá tratar apenas o registro utilizado na operação, diminuindo a possibilidade de *deadlock*.  
Lembrando que a utilização deste parâmetro diminui a possibilidade de *deadlock* durante o processamento de rotinas que manipulem as três tabelas acima citadas, contudo não extingue a possibilidade da ocorrência do mesmo.  
  
**Saiba mais**  
[Parâmetro MV\_FATTRAV](http://tdn.totvs.com/pages/releaseview.action;jsessionid=45C5AC5CACC6CD6C16189E62EE93F15E?pageId=235312018)
