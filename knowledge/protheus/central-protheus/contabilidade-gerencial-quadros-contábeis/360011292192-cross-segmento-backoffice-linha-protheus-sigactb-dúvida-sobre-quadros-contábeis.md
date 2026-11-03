---
article_id: 360011292192
category: Contabilidade Gerencial - Quadros Contábeis
content_hash: ee8e67ec14df61058cac8e04897ce1e7dda8046e010c4887cb92bc994e396160
fetched_at: '2026-06-28T22:40:34.933629+00:00'
product: protheus
section_id: 1500001548982
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Dúvida sobre quadros
  contábeis - CTBR040
type: support-article
updated_at: '2022-06-10T23:01:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011292192-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-D%C3%BAvida-sobre-quadros-cont%C3%A1beis-CTBR040
---

**Dúvida**  
Como imprimir os quadros contábeis no CTBR040?  
   
 **Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
   
**Solução**1- Para imprimir o Quadro Contábil é necessário realizar a Apuração de Resultados (CTBA211). No exemplo abaixo foi utilizado a conta ponte.

2- Efetue **lançamento manual do** **total a debito contra o total a crédito apurado** *preferencialmente*em contas que não estejam no range de apuração, pois facilita a identificação no relatório. Neste exemplo, foi utilizada as contas 9100500 para o total a débito e 9100600 para o total a crédito.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045662394/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045662414/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045662454/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045662574/mceclip3.png)

No quadro acima:

Quadro 1 - Totais Ativo/Passivo

1 - (Informado na pergunta 1) - Total do Ativo

2 - (Informado na pergunta 2) - Total do Passivo

Quadro 2 - Demonstrativo de Resultados - Mensal - apresentam os movimentos totais (coluna movimento) no período.

3 - (Informado na pergunta 3) – Contas de Resultado - Devedora – movimento do período

4 - (Informado na pergunta 4) - Contas de Resultado - Credora – movimento do período

Resultado do mês MM/9999 - Débito + credito do período

Resultado acumulado até MM/9999 – Saldo Atual Débito (Despesa) + Saldo Atual crédito (Crédito)

Quadro 3 - Demonstração do patrimônio líquido destacado

Patrimônio Líquido  – Saldo Atual da conta

Total da receita (Informado na pergunta 6 – Não imprime a conta) - 5.300,00 D

Total da despesa (Informado na pergunta 7 – Não imprime a conta) - 4.600,00 C

Patrimônio Líquido Corrigido – 700,00 D - Patrimônio Líquido (Saldo atual da conta pergunta 5) + Total da despesa + Total da Receita

Lançamento de Correção – 700,00 -  Total da despesa + Total da Receita

**Veja :**

[**Quadro Contábil - CTBR040**](http://tdn.totvs.com/pages/releaseview.action?pageId=152110148)
