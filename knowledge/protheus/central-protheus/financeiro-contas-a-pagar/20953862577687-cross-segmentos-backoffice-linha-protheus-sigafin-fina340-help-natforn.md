---
article_id: 20953862577687
category: Financeiro - Contas a Pagar
content_hash: 0096865506237f464bfd34962fc038fe9c328113c5fcf9a6e3f683bedd78284b
fetched_at: '2026-06-28T22:38:09.632316+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - HELP NATFORN
type: support-article
updated_at: '2024-01-30T14:39:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20953862577687-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-HELP-NATFORN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20953798964247) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Quando um título (NDF) é migrado para o Financeiro, ao tentar realizar a compensação é apresentado o **Help: NATFORN** (Natureza ou fornecedor não encontrado!).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20953798966295)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre quando o preenchimento do campo **A2\_NATUREZ** está vazio (" ").  
  
**Solução**Na Compensação do título, o campo **A2\_NATUREZ** deve ser preenchido no **Cadastro do Fornecedor**, caso não esteja, é necessário alterar a NDF, e preencher o campo **E2\_NATUREZ** manualmente.  
  
**Observação**

**O Sistema não carregará a informação no campo E2\_NATUREZ**,** pois é possível devolver várias notas de Entrada em uma só nota de Saída e cada uma dessas notas devolvidas poderá ter naturezas diferentes. Por esta razão é fixa a busca através da natureza do Cadastro do Fornecedor.****Saiba mais**

[FAT0130 Gerar NDF pelo modulo de Faturamento (SIGAFAT)](https://tdn.totvs.com/pages/releaseview.action?pageId=253988539)
