---
article_id: 360009629271
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 5217d378940eab5435eaa0487c64f92325b8d70f34df3ea319081b6f8f60d60e
fetched_at: '2026-06-28T22:40:32.559615+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA102 - Erro ao Rastrear
  Contabilização: invalid field name in Alias CT2->CT2_SEQUENC on CTC010VAL'
type: support-article
updated_at: '2023-02-06T12:24:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009629271-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Erro-ao-Rastrear-Contabiliza%C3%A7%C3%A3o-invalid-field-name-in-Alias-CT2-CT2-SEQUENC-on-CTC010VAL
---

**Ocorrência**Ao rastrear lançamento contábil, sistema apresenta error.log.

invalid field name in Alias CT2->CT2\_SEQUENC on CTC010VAL (CTBC010.PRW)

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - SIGACTB - Contabilidade – A partir da versão 11.80

**Causa**Esse incidente ocorre, pois no campo está escrito CT2\_SEQUENC e o correto é CT2\_SEQUEN

**Solução**

1. Na tabela CT2 o correto é o campo CT2\_SEQUEN conforme ambiente padrão como print abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/Eswxih3hXQfazTqk1USzS2owW/?name=inline-680308457.png)  
  
2. Efetue o ajuste do mesmo e se necessário, atualize o dicionário conforme Portal do Cliente.  
  
3. Rodar UPDDISTR
