---
article_id: 12549400233239
category: Chão de Fábrica (SIGASFC)
content_hash: 8876acc4c29f08b9e0d6f03bbc494c0a0405051ed97a2c76ea27acae82d3ffbb
fetched_at: '2026-06-28T22:42:49.835048+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Encerramento automático da OP ao realizar
  o apontamento total
type: support-article
updated_at: '2023-02-20T17:08:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12549400233239-Manufatura-Linha-Protheus-SIGASFC-Encerramento-autom%C3%A1tico-da-OP-ao-realizar-o-apontamento-total
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:35 min** **Dúvida**Por que ao realizar o apontamento pelo **APP Minha Produção** do **Chão de Fábrica**, mesmo que a **OP - Ordem de Produção** já tenha consumido seu saldo, ela não é encerrada?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Solução**Para que a **OP** seja encerrada ao realizar o apontamento com a quantidade planejada é necessário configurar o parâmetro **MV\_SFCEDRP - Indica se fecha automaticamente split/operação quando quantidade reportada na operação seja maior ou igual a prevista. Não - Mantem abertos**igual a **T**.
