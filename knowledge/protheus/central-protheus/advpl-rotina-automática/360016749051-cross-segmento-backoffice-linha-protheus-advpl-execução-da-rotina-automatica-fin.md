---
article_id: 360016749051
category: ADVPL - Rotina Automática
content_hash: a84a6ad33589154899ef4fc583cc362c43fa5ce662b8153f6079da7e5992a06d
fetched_at: '2026-06-28T22:40:24.056255+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Execução da Rotina Automatica
  Fina290
type: support-article
updated_at: '2021-12-29T14:59:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016749051-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Execu%C3%A7%C3%A3o-da-Rotina-Automatica-Fina290
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Gerar rotina automática fazendo com que a tabela **CT2** seja gerada fazendo a contabilização *On-Line.*  
  
**Ambiente**Protheus – ADVPL - Financeiro – A partir da versão 11.80  
  
**Solução**Para que seja gerada a rotina automática e mesma atualize as tabelas FK2 e CT2 , gerando a contabilização *on-line*é necessário que o parâmetro **MV\_PRELAN** esteja setado da seguinte maneira :

1. S = Para gerar pré-lançamento sempre que for efetuada a contabilização.
2. D = Para gerar pré-lançamento quando o documento não conciliar o débito com o crédito.
3. N = Para nunca gerar pré-lançamento, se o documento não bater o fato contábil não será contabilizado ,caso contrário serão tratados como lançamentos contábeis efetivos.

**Saiba Mais** **[Indicador de Pre lançamento Contábil](http://tdn.totvs.com/pages/releaseview.action?pageId=284348618)**
