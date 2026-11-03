---
article_id: 26078533158039
category: Financeiro - Contas a Receber - LCDPR
content_hash: 8599e69f478b0e8c1f7a8d6d1fde38c4d659662152de5895a06347a7967dad7f
fetched_at: '2026-06-28T22:38:15.851597+00:00'
product: protheus
section_id: 1500001539361
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA820 - Qual o conceito
  para o pagamento de empréstimo IR para o bloco Q100
type: support-article
updated_at: '2024-09-02T19:02:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26078533158039-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA820-Qual-o-conceito-para-o-pagamento-de-empr%C3%A9stimo-IR-para-o-bloco-Q100
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26078516472215) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Qual o conceito para o pagamento de empréstimo IR para o (bloco Q100)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

**Pagamento de empréstimo (bloco Q100)**

Quando houver um pagamento de empréstimo, será levado para o registro **Q100**, somente os movimentos de encargos financeiros (juros).

Para o correto funcionamento, o parâmetro **MV\_NATREMP (Natureza para Pagamento de empréstimo)** deve estar preenchido com uma **Natureza que gere LCDPR (ED\_LCDPR = 1)**.

**Saiba mais:**   
[LCDPR - Extrator do Livro Caixa Digital do Produtor Rural (FINA820)](https://tdn.totvs.com/pages/releaseview.action?pageId=520110581)

[LCDPR - Empréstimos e Financiamentos - Atividade Rural](https://tdn.totvs.com/pages/releaseview.action?pageId=571003317)
