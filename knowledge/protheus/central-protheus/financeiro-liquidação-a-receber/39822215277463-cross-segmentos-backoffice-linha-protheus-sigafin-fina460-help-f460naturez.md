---
article_id: 39822215277463
category: Financeiro - Liquidação a Receber
content_hash: 8dba1ede0c04b41819759820c92aa9f7b539cda163f4e7beea5185aa35631165
fetched_at: '2026-06-28T22:37:42.333986+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA460 - HELP F460NATUREZ
type: support-article
updated_at: '2026-04-17T20:18:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39822215277463-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA460-HELP-F460NATUREZ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39822215266711) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao tentar confirmar a liquidação de títulos através da rotina FINA460, o sistema apresenta o Help F460NATUREZ

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as versões

**Causa**  
O Help **F460NATUREZ** ocorre quando o campo **Natureza Liquidação** (CNATUREZA) não está preenchido nos parâmetros da rotina de Liquidação. Este campo é de preenchimento obrigatório para que o sistema consiga gerar os novos títulos liquidados, determinando a classificação financeira que será atribuída aos mesmos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39834641840279)

**Solução:**

1. No módulo **Financeiro (SIGAFIN)**, acesse **Atualizações** > **Contas a Receber** > **Liquidação (FINA460)**;
2. Selecione os títulos desejados e clique em **Liquidar**;
3. Na tela de parâmetros de liquidação, localize o campo **Natureza Liquidação**;
4. Clique na consulta (F3) e selecione uma natureza válida cadastrada no sistema;
5. Preencha os demais campos obrigatórios e clique em **Ok** para processar a liquidação.

Saiba mais:

[Fina460 - Liquidação Contas a Receber](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)
