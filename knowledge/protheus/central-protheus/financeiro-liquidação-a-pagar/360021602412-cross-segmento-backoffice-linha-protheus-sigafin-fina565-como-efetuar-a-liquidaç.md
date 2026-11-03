---
article_id: 360021602412
category: 'Financeiro - Liquidação a Pagar '
content_hash: 7ba51b336e3cd091862be58be20294eba17bc9a0bee56d6d09ee99cf9c7d4bef
fetched_at: '2026-06-28T22:37:32.442868+00:00'
product: protheus
section_id: 35057594361879
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA565 - Como efetuar
  a Liquidação a Pagar
type: support-article
updated_at: '2025-11-26T20:29:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021602412-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA565-Como-efetuar-a-Liquida%C3%A7%C3%A3o-a-Pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25478273956247) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**  
Como efetuar a Liquidação a Pagar (FINA565)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro - FINA565 –  Todas as versões  
  
**Solução**  
Esta rotina é responsável pela quitação das dívidas pendentes com fornecedores. Após a negociação, poderá resultar na criação de um ou mais títulos a pagar, conforme os termos de pagamento acordados. Tanto os títulos originais quanto aqueles gerados pelo sistema recebem um número de liquidação, atribuído sequencialmente conforme o parâmetro **MV\_NUMLIQP.**

**Contabilização**:  
A contabilização dos títulos gerados por esta rotina pode ser realizada por meio dos lançamentos padrão  
• **LP 510** - Contas a Pagar - Inclusão de títulos.  
• **LP 515** - Contas a Pagar - Exclusão de títulos.  
A contabilização da baixa dos títulos utilizados na liquidação pode ser feita pelo lançamento padrão:  
• **LP 530** - Contas a Pagar - Baixa de Títulos.  
Nesse caso, o motivo da baixa utilizado para identificar os títulos baixados por liquidação deve ser o LIQ.

**Liquidação**

**![liquidar 565.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25472326364951)**

**Reliquidação**  
Os títulos gerados por essa rotina também podem ser **renegociados**. Nesse caso, a ação é denominada Reliquidação.

![reliquidar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25472339811223)

**Estorno da Liquidação ou Reliquidação**

![Gravar_2024_08_07_11_19_07_550.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25472521206039)

**Base reduzida de impostos**  
Em situações de renegociação, os impostos retidos na baixa e suas respectivas bases serão transferidos para os novos títulos gerados, sempre que a Natureza da Liquidação permitir o cálculo desses impostos. Os impostos que não forem calculados pela Natureza da Liquidação serão desconsiderados.

**Saiba mais**  
[Liquidação a pagar - FINA565](https://tdn.totvs.com/pages/releaseview.action?pageId=312167645)
