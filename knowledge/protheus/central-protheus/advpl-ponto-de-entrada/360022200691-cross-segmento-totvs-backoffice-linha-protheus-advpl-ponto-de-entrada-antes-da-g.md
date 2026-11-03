---
article_id: 360022200691
category: ADVPL - Ponto de Entrada
content_hash: c4c43fe4dce9af77bed674b41b6bb9336ea19e551554b6f3c6a67d9da70a35a1
fetched_at: '2026-06-28T22:40:11.780428+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  antes da geração NF's  MATA460A
type: support-article
updated_at: '2021-12-29T17:30:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200691-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-antes-da-gera%C3%A7%C3%A3o-NF-s-MATA460A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Qual ponto posso utilizar na preparação do documento de saída (**MATA460A**), antes da geração das NF's?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**O ponto de entrada **M460MARK** é utilizado para validar os pedidos marcados e está localizado no inicio da função **a460Nota** (endereça rotinas para a geração dos arquivos **SD2**/**SF2**). Determina se deverá prosseguir com o processamento para geração da nota fiscal.

**Exemplo**

```
User Function M460MARK()  
Local lRet  
  
lRet := ApMsgYesNo('PE - M460MARK - Continua ?')  
  
Return lRet
```

**![KCS_M460MARK.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360019189092/KCS_M460MARK.gif)**

**Saiba Mais**[M460MARK - Validação de pedidos marcados](http://tdn.totvs.com/pages/releaseview.action?pageId=6784189)
