---
article_id: 360043233853
category: ADVPL - Rotina Automática
content_hash: 410b80f428c8e78ba90f042e4a5d0c201020964439565f0b727db22995f63987
fetched_at: '2026-06-28T22:40:25.022486+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina automática
  atendimentos TMKA271
type: support-article
updated_at: '2022-06-21T17:28:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043233853-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-atendimentos-TMKA271
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao incluir um atendimento o sistema gera o seguinte erro.  
Exemplo:

```
Tabela SUA 01/01/19 12:36:20  
Cliente - UA_CLIENTE := 000001 < -- Invalido  
Loja - UA_LOJA := 01
```

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 12.1.23  
  
**Causa**Este ocorre quando não se passa o usuário na preparação do ambiente, visto que é obrigatório para a rotina identificar o operador.  
  
**Solução**Deve-se informar o usuário e senha na execução, exemplo:

```
PREPARE ENVIRONMENT EMPRESA "01" FILIAL "00" USER "USUARIO" PASSWORD "SENHA" MODULO "TMK" TABLES "SUA","SUB","SUC","SUD","SB1","SA1","SUS","SE4","AC8","SA4","SU7"
```

**Saiba mais**

**[TMKA271 - Rotina automática atendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=6787711)**
