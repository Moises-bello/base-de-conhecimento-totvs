---
article_id: 24818254759703
category: Faturamento - Cadastros
content_hash: 164c1db8b6dd35a3d9fe6ca3d7850179704ce8c6aa204c9a5841c80a8ca4cc17
fetched_at: '2026-06-28T22:38:35.478249+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Simulação da condição de
  pagamento não administra corretamente impostos
type: support-article
updated_at: '2024-07-11T14:41:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24818254759703-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Simula%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-n%C3%A3o-administra-corretamente-impostos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24818277175447) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**A simulação da condição de pagamento não administra corretamente impostos, como arrumar?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Caso a condição de pagamento tenha ICMS ou IPI, o valor informado dos impostos tem que estar no total e não fora dele, exemplo:

No exemplo, o total do pedido de venda seria R$ 100 e total com cada imposto, R$ 120.

**Maneira errada:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24818277178647)![](https://centraldeatendimento.totvs.com/hc/article_attachments/24818254671639)

**Total: R$ 100 (Errado, pois não tem os impostos que se deseja considerar)**

ICI: R$ 10

ICMS: R$ 10

Total esperado: R$ 120

Resultado pela maneira errada [caso na condição de pagamento fosse escolhido o ICMS e IPI da maneira "IPI (E4\_IPI)" e "ICMS (E4\_SOLID)" = "S - Separa" (que concentra os impostos na primeira parcela)]

**Maneira correta:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24818254673687)![](https://centraldeatendimento.totvs.com/hc/article_attachments/24818254675607)

**Total: R$ 120**

ICI: R$ 10

ICMS: R$ 10

Total esperado: R$ 120

**Saiba mais:**

* [FAT0089 - Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)
* [Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento do campo "ICM Solid." (E4\_SOLID)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535941177367-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-ICM-Solid-E4-SOLID)
* [Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento do campo "IPI (N/J/S)" (E4\_IPI)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9245346715159-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-IPI-N-J-S-E4-IPI)
