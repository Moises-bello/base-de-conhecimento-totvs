---
article_id: 360021137192
category: ADVPL - Classe e Função
content_hash: 3e9a7665922be72c542304fffc48f26cc025ea5854e3bc3f1084cb5fad86d0d2
fetched_at: '2026-06-28T22:40:19.263982+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Error.log -  invalid
  macro source
type: support-article
updated_at: '2022-01-10T15:03:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021137192-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Error-log-invalid-macro-source
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Error.log - *invalid macro source*  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**O erro específico começou a ocorrer após as atualizações de lib, disponibilizadas no inicio de 2017:

```
invalid macro source (SSYacc0105e: Error token failed, no valid token)   
(STATICCALL(#FUNCAO_DO_USUARIO,MenuDef)) on FWLOADMENUDEF(PROTHEUSFUNCTIONMVC.PRX)
```

O motivo é que foi realizado uma alteração no fonte **FWLOADMENUDEF** para, no caso de não estar como usuário administrador, macroexecutar as funções afim de validá-las, e como a função de usuário começa com '#' ele gera o erro. Anteriormente a essa alteração já havia sido implementado o TYPE 03, que é específico para funções de usuário, não mais utilizando o '#' para essa finalidade.  
Para que não gere mais o erro verifique nos arquivos XNU a chamada de uma função de usuário se está com # ((#**FUNCAO\_DO\_USUARIO**) e TYPE como 01(função Protheus), retire o '#' e altere o TYPE para 03 conforme instruções a seguir:

**Errado:**

```
<Function>#FUNCAO_DO_USUARIO</Function>  
<Type>01</Type>
```

**Certo:**

```
<Function>FUNCAO_DO_USUARIO</Function>  
<Type>03</Type>
```

**Observação**  
Caso persista verifique se o nome do fonte está com caractere especial ou iniciando por número.  
Não recomendamos a manipulação direta dos arquivos xnu, a opção mais segura é cadastrar os menus pelo configurador.
