---
article_id: 11601499400727
category: Financeiro - Viagens
content_hash: e11369dfdd7ceb34a2ef3b0c4a123d66406cf810b9e772c3f15fbc1ef8f80cdd
fetched_at: '2026-06-28T22:38:21.459479+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA691: Não é possível
  alterar tipo do título para adiantamento'
type: support-article
updated_at: '2023-01-12T14:06:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11601499400727-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA691-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-tipo-do-t%C3%ADtulo-para-adiantamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar alteração do tipo dos Títulos na guia Adiantamento de **RC** para **PA**, fica travado no campo Tipo dos Títulos (MV\_RESTPAD).   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Financeiro- Todas as versões  
  
**Causa**Na **FINA691** parametrização do sistema *Wizard* configuração sistema não permite alterar tipo de adiantamento para **PA**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11601298675607)  
  
**Solução**O tipo **PA** por regra não é permitido pois por padrão ele gera movimentação bancaria no momento de sua criação, indicado para realização de compensação de operações entre fornecedores com notas de compra.  
Você pode usar qualquer outro tipo, esses em especifico por regra só podem ser usados no financeiro para compensações futuras como informado acima.
