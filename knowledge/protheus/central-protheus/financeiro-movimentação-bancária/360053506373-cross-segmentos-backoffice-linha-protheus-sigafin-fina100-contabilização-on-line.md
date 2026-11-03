---
article_id: 360053506373
category: Financeiro - Movimentação Bancária
content_hash: 86a7210da1aa456ba8b481402a3cd7a9a117f1d817511e1e3a5e162e9c3e5fd2
fetched_at: '2026-06-28T22:38:19.478395+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA100 - Contabilização
  on-line de cancelamento de movimentos a receber e a pagar '
type: support-article
updated_at: '2022-09-30T22:24:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053506373-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Contabiliza%C3%A7%C3%A3o-on-line-de-cancelamento-de-movimentos-a-receber-e-a-pagar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:10:00 min  
  
Dúvida**Porque ao cancelar um movimento a receber e/ou a pagar nos movimentos bancários através da rotina **FINA100 - Movimentos Bancários**, a contabilização ocorre independente de configuração dos parâmetros F12 (Contabiliza Online? = Não)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA100 - Todas as versões

**Solução**A contabilização do **LP 564** (**No cancelamento de movimentos a pagar nos Movimentos Bancários**) e **LP 565** (**No cancelamento de movimentos a receber nos Movimentos Bancários**) somente ocorrerá de forma online, por isso mesmo que a pergunta **Contabiliza Online?** esteja igual a **Não** no parâmetro F12 da rotina **FINA100**, o processo de contabilização irá ocorrer de forma online, desde que tenha sido realizado a contabilização da inclusão dos movimentos a receber e/ou a pagar nos movimentos bancários, através dos **LP 562** (**Na inclusão de movimentos a pagar nos Movimentos Bancários**) e **LP 563** (**Na inclusão de movimentos a receber nos Movimentos Bancários**).  
  
**Saiba mais**:  
[Contabilização do LP 562564 - FINA100](https://tdn.totvs.com/pages/releaseview.action?pageId=6070720)  
[FIN0026\_LPAD\_lancamento\_padrao\_por\_macro\_processo](https://tdn.totvs.com/display/PROT/FIN0026_LPAD_lancamento_padrao_por_macro_processo)<https://tdn.totvs.com/pages/viewpage.action?pageId=235585410>
