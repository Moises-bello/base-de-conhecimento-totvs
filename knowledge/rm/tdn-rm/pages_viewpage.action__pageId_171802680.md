---
content_hash: 85be2a8a967504a214f191aa33fac6e306145b5c8c7686f0f880c759734e7aab
fetched_at: '2026-06-29T00:05:57.260173+00:00'
page_id: '171802680'
product: rm
source: tdn-rm
title: Diferença na contabilização do movimento em TOTVS Gestão de estoque, compras
  e faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=171802680
version: 2
---

|  |  |
| --- | --- |
| Produto | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| Versões | A partir da 11.40 |
| **Processo** | Integração Contábil |
| **Subprocesso** | Contabilização de Movimentos |
| Sintoma | Diferença na contabilização do movimento “O Lançamento não pode ser salvo pois a soma das partidas de débito R$ XX,xx é diferente da soma das partidas de crédito R$ YY,yy” |
| Causa | O Evento contábil utilizado no movimento está retornando os valores incorretos ou não retorna valores.  *Ex.:O evento só retornou uma conta contábil (de crédito) deixando o lançamento com diferença.* |
| Solução | Utilize o “Log de evento contábil” para identificar o erro do Evento Contábil e após isto realizar as devidas correções.  **link: [Como Fazer - Log contábil no TOTVS Gestão de estoque, compras e faturamento](http://tdn.totvs.com/x/hQBFCg)** |
