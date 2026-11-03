---
article_id: 360026815053
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 91586cacab60b09aa12d96b20a732d9461dffa81228da861a769a62abc786bc5
fetched_at: '2026-06-28T22:37:20.211288+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos  - Totvs Backoffice Protheus - SIGAGCT - Error log ao acessar
  a rotina CNTA300 invalid macro source (SSYacc0105e: Error token failed, no valid
  token) :(CN9_FILCTR on FWMBROWSE:GETPOSICIONE(FWBROWSE.PRW)'
type: support-article
updated_at: '2022-02-24T17:41:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026815053-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Error-log-ao-acessar-a-rotina-CNTA300-invalid-macro-source-SSYacc0105e-Error-token-failed-no-valid-token-CN9-FILCTR-on-FWMBROWSE-GETPOSICIONE-FWBROWSE-PRW
---

**Ocorrência**Ao acessar a rotina CNTA300 ocorre o error log "invalid macro source (SSYacc0105e: Error token failed, no valid token) :(CN9\_FILCTR on FWMBROWSE:GETPOSICIONE(FWBROWSE.PRW)"  
  
**Ambiente**  
Microsiga Protheus – Gestão de Contratos – A partir da versão 12.17  
  
**Causa**

Esse incidente ocorre, pois, o inicializador do browser do campo CN9\_DESC está com o posicione incorreto.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Realize o ajuste do Inicializador Browser do campo conforme imagem abaixo no configurador em ambiente de homologação:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041698814/mceclip0.png)

```
 - Acessar o modulo "Configurador (SIGACFG)'  
 - Acessar a rotina "Base de Dados"  
 - Abrir a tabela CN9 - Contratos  
 - Localizar e editar o campo CN9_DESC  
 - Clicar na aba "Opções" Campo "Inic. Browse"  
 - Ajustar o conteúdo do campo X3_INIBRW para:  POSICIONE("CN1",1, xFilial("CN1",CN9->CN9_FILCTR) + CN9->CN9_TPCTO,"CN1_DESCRI")
```

***Saiba Mais:***

* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
