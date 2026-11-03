---
article_id: 360019534772
category: Contabilidade Gerencial - Reprocessamento
content_hash: dfbc3387c76fad00cc679a14376632c3ec3755ada5c631ac17ea3b533298384e
fetched_at: '2026-06-28T22:40:42.006569+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Saldos não estão sendo
  atualizados de forma online.
type: support-article
updated_at: '2025-04-09T13:52:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online
---

**Ocorrência**

Ao incluir ou modificar algum lançamento contábil os saldos não estão sendo atualizados de forma online.

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Causa**

O erro ocorre devido a criação indevida(via procedure) da tabela temporária ***TRWxxSP*** no banco de dados, quando o correto é ***TRWxx0\_SP(******com o '\_')***, e com isso a procedure se perde no momento de atualizar os saldos, deixando vestígios na tabela temporária.

**Solução**

**1**- Para correção deve verificar o fonte CFGX051.PRW para que esteja com data igual ou superior a 14/08/2018.

Após aplicar o pacote, 'desinstalar' as procedures, automaticamente vai apagar a tabela ***TRWxx0\_SP*** do banco de dados, porém a tabela ***TRWxxSP*** não é excluída automaticamente então deve fazer este processo de forma manual. Feito isso faça um refresh na pasta de tabelas do banco para confirmar se realmente estão excluídas.  
  
Reinstale as procedures do contábil e inclua um novo lançamento e os saldos serão atualizados com sucesso, criando também somente a tabela TRWxx0\_SP no banco de dados.

***Importante :***Faça os procedimentos primeiramente em base teste e certifique-se se os parâmetros: **MV\_ATUSAL** esteja com conteúdo igual a 'S' e o parâmetro **MV\_MUDATRT** = esteja com conteúdo igual a '.T.' .  
  
**2** - Verifique também o compartilhamento se o compartilhamento das tabelas CQx (CQ0 a CQ9) estão conforme ao da tabela CT2, este ponto deve ser verificado tanto no dicionário quanto na tabela SX2 contida no banco de dados, isso, pois quando a atualização dos saldos online é feito via Stored Procedure, o compartilhamento visualizado é o contido na SX2 do banco de dados. Pode-se verificar as regras de compartilhamento do módulo contábil em: [Compartilhamento Contabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-)

* [Campo Filial das tabelas CQ não estão sendo alimentadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018497311-MP-SIGACTB-CTBA190-Campo-Filial-das-tabelas-CQ-n%C3%A3o-est%C3%A3o-sendo-alimentadas-?source=search)
