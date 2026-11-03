---
article_id: 360022215791
category: ADVPL - Classe e Função
content_hash: 6e5ab7be3c021ed4dd032a470cb819a2cb12f2050f5e14179815de5c86285682
fetched_at: '2026-06-28T22:40:18.154270+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Update error - lock
  required - File (...)
type: support-article
updated_at: '2022-06-14T17:46:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022215791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Update-error-lock-required-File
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:04:00 min  
  
Ocorrência**ERRO THREAD (xxx, xxxxx) 28/05/2007 09:52:27 Stack :Update error - lock required - File: SX5990 in file  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Quando uma aplicação **AdvPL** tenta realizar uma atribuição, ***REPLACE*** ou **FieldPut**() em qualquer campo de um determinado Alias, e o registro atualmente posicionado não estiver devidamente bloqueado pelo usuário atual para alteração (**DBRLock**(), **MSRLock**() e/ou **RecLock**()), a aplicação é finalizada com a mensagem de erro acima, onde é informado o arquivo a ser atualizado, e a linha do código-fonte onde houve a tentativa de atualização, seguinda da pilha de chamadas.  
  
**Solução**Para solucionar essa ocorrência, deve ser verificado o código-fonte que realiza a alteração do registro, para certificar-se que o registro posicionado para alteração realmente foi bloqueado para alteração. Na grande maioria dos casos, não foi verificado no código-fonte se houve sucesso na tentativa de bloqueio do registro para alteração.  
  
**Informações acionais**  
São boas práticas de programação, sempre ao fazer uma alteração de registro em uma tabela, utilizar ALIAS->CAMPO para fazer a atribuição, ou ainda a função **FieldPut**(). Não é boa prática fazer a atualização de um campo **SEM** utilizar o *ALIAS*.

**Exemplo:**

```
Ao invés de :   
CAMPO := xConteudo  
  
Utilize :  
ALIAS->CAMPO := xConteudo
```

**Saiba mais  
[Update error - lock required - File (...)](http://tdn.totvs.com/pages/viewpage.action?pageId=6063162)**
