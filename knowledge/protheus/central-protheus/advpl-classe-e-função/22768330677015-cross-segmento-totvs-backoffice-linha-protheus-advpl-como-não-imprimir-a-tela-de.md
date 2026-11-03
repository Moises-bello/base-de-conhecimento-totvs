---
article_id: 22768330677015
category: ADVPL - Classe e Função
content_hash: 8d8305d9f0670903245986428b429b8eec01569d38e31494aa159bd93e24a71c
fetched_at: '2026-06-28T22:40:20.698799+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como não imprimir
  a tela de parâmetros usando a classe TReport?
type: support-article
updated_at: '2024-04-12T19:23:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22768330677015-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-n%C3%A3o-imprimir-a-tela-de-par%C3%A2metros-usando-a-classe-TReport
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22768338402455) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Como não imprimir a tela de parâmetros usando a classe TReport?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Para que não seja impresso a página com os parâmetros usados pelo usuário em fontes customizados. Pode-se usar o método ShowParamPage, no qual define se será impresso a página com os parâmetros.

Exemplos:

```
oReport:ShowParamPage()  
oReport:lParamPage := .F.
```

**Saiba Mais**

[Treport](https://tdn.totvs.com/display/public/framework/TReport)
