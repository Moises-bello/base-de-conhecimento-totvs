---
article_id: 10823823828631
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 4ceaa90ce1c7f6c0a7e9b15536f2ef7753f4903931061bc6d3b604f57a79fb62
fetched_at: '2026-06-28T22:38:42.626137+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Dúvidas na Aba Rentabilidade da planilha financeira
type: support-article
updated_at: '2022-12-13T19:27:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10823823828631-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-D%C3%BAvidas-na-Aba-Rentabilidade-da-planilha-financeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:45 min****Ocorrência**Dúvidas na Planilha financeira do pedido de vendas, aba Rentabilidade

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.

**Solução**

(**1**) - Na Consulta Rentabilidade Pedido de Venda, o valor do frete é considerado na coluna do Valor Presente e depois no Valor Bruto, independente se é CIF ou FOB. Está correto este cálculo?

**RESPOSTA:** Está correto sim, para o pedido de vendas o fato de ser FIB ou FOB não interfere no cálculo, são apenas campos informativos que não tem ação no sistema. E se o valor do frete for informado, será apresentado na coluna valor presente e depois no valor Bruto.

 (**2**) - Sobre a comissão: Não está sendo deduzido do valor bruto para calculo da margem. Existe algum parâmetro para considerar este valor ? Se negativo, existe algum ponto de entrada para personalizar esta rotina ?

**RESPOSTA:** A comissão não foi calculada ainda, apenas quando o faturamento é realizado, então o mesmo não será apresentado na rentabilidade. O conceito de rentabilidade é apenas para dados do pedido o que for gerado após sua preparação, como a comissão especificamente, não será considerado.

**Para atender as necessidades acima, favor avaliar o ponto de entrada abaixo:**

**MA410RPV** - Alterar valores ou inibir demonstrações de valores **(****[http://tdn.totvs.com/pages/releaseview.action?pageId=6784271](https://tdn.totvs.com/pages/releaseview.action?pageId=6784271))**

**Saiba Mais:**

**[FAT0139 Processo para utilização de Rentabilidade no Pedido de Vendas (MATA410)](https://tdn.totvs.com/x/RojpDw)**
