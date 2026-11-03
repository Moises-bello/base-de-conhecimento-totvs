---
article_id: 360025322852
category: Financeiro - Contas a Pagar
content_hash: 97c1404243da982e47ec0a16a30670cb1352479e208897a1bd3dd731493b9785
fetched_at: '2026-06-28T22:38:08.290014+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA241 - HELP CNBIMPG
type: support-article
updated_at: '2022-04-19T20:56:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025322852-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA241-HELP-CNBIMPG
---

**Ocorrência**Ao acessar a rotina FINA241 (Borderô de impostos) apresenta o Help CNBIMPG?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024355831/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA241 - Todas as versões  
  
**Causa**Porque o parâmetro **MV\_CNBIMPG** referente a permissão da geração dos títulos de Pis, Cofins, Csll e IR somente após baixa efetuada por leitura de arquivo CNAB está ativado.

**Solução**Deverá utilizar a rotina **FINA240** (Borderô Pagamentos) para gerar os impostos no **retorno CNAB** e inserir os títulos no borderô e não utilizar a rotina **FINA241** Borderô de impostos.
