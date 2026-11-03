---
article_id: 21918289518231
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 9899f274b446e646e0fba90e93be9d8452caf689e32d87f6cf66f13e49f7b678
fetched_at: '2026-06-28T22:37:56.461370+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN- FINA713 - Como gerar
  o boleto com valor líquido do título e o desconto dos impostos
type: support-article
updated_at: '2024-03-12T20:22:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21918289518231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Como-gerar-o-boleto-com-valor-l%C3%ADquido-do-t%C3%ADtulo-e-o-desconto-dos-impostos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21918289494039) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como gerar o valor líquido do título que desconsidere os impostos, exemplo PIS, COFINS, CSLL?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA713  - A partir da release 12.1.33  
  
**Solução**Na geração de títulos com impostos no **Contas a Receber**, o campo de saldo se mantém conforme o valor total, neste caso, precisa ajustar no layout da FINA710 - Configuração de Contas para diminuir o valor com base nos impostos. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21918289496215)

Aplicará seguinte regra na engrenagem

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21918289500055)

Será exibido o **valor desconto**, além dos abatimentos dos impostos gerados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21918282574615)

**Saiba Mais**[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)
