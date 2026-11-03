---
article_id: 14154517008151
category: Financeiro - Contas a Receber
content_hash: 73606a73fd83020cc4703c4bc458a7ad7d2921c91213cff1b6915fb05011408e
fetched_at: '2026-06-28T22:38:12.640209+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050/FINA040 -
  HELP: FA050NUM / FA040NUM'
type: support-article
updated_at: '2026-03-25T18:28:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14154517008151-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-FINA040-HELP-FA050NUM-FA040NUM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36685115973783) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Ao incluir um título no contas a receber ou pagar, é apresentado HELP: FA050NUM / FA040NUM?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14638738811159)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Valida se possui outro título com as mesmas informações dos campos abaixo:  
Referente ao **Contas a Receber**:

```
E1_PREFIXO + E1_NUM + E1_PARCELA + E1_TIPO
```

Referente ao **Contas a Pagar**:

```
E2_PREFIXO + E2_NUM + E2_PARCELA + E2_TIPO + E2_FORNECEDOR + E2_LOJA
```

Verifique se o tamanho dos campos **filial, prefixo, número, parcela, tipo, fornecedor, loja** na **SX3** e no **Banco** estão iguais.  
Realizar o ajuste no campo caso tenha alguma das divergências acima.

**Saiba mais**

[**FIN0079\_Utilização do parâmetro MV\_1DUP**](https://tdn.totvs.com/pages/viewpage.action?pageId=286197157&draft=true)
