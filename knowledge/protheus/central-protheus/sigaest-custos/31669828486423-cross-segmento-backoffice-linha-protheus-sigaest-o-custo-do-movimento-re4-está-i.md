---
article_id: 31669828486423
category: SIGAEST - CUSTOS
content_hash: bc6d40933e75d85aba332a027e4e9c21976a73504f1652bd39f3e83f89e4e26b
fetched_at: '2026-06-28T22:39:02.279883+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O custo do movimento
  RE4 está indo com valor zerado enquanto sua devolução DE4 está com custo, porque
  o mesmo está sendo custeado?
type: support-article
updated_at: '2025-04-25T18:10:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31669828486423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-custo-do-movimento-RE4-est%C3%A1-indo-com-valor-zerado-enquanto-sua-devolu%C3%A7%C3%A3o-DE4-est%C3%A1-com-custo-porque-o-mesmo-est%C3%A1-sendo-custeado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31669828470167) Tempo aproximado para leitura: **00:01:00 min****Dúvida**

O custo do **movimento RE4** está indo com valor zerado enquanto sua **devolução DE4** está com custo, porque o mesmo está sendo custeado?

Segue um exemplo das movimentações:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31669842445975)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31669828471063)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

No caso descrito, a movimentação **DE4** foi valorizada devido ao fato de o sistema estar utilizando o **custo por armazém (MV\_CUSFIL = A)**. Dessa forma, o sistema considera o custo médio histórico daquele armazém para gerar a movimentação.  
  
Quando ocorre uma movimentação sem valor de custo ou com custo zero, o sistema recorre ao custo médio histórico para calcular e gerar a movimentação.  
  
Para evitar que o recalculo utilize o custo médio histórico, é necessário ativar o parâmetro **MV\_CUSZERO**. Exemplos e explicações detalhadas sobre esse procedimento podem ser consultados no seguinte link:

[***https://tdn.totvs.com/x/v6NHKQ***](https://tdn.totvs.com/x/v6NHKQ)

**Nota:** Lembrando que o exemplo foi uma movimentação de **Transferência entre Armazéns (RE4/DE4)** porém pode ser também para outras movimentações internas do estoque.

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
