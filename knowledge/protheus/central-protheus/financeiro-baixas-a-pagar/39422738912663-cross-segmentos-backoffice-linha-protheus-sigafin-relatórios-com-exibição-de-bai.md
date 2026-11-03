---
article_id: 39422738912663
category: Financeiro - Baixas a Pagar
content_hash: 4dd5031e46b6e8161a8451b25e2739c08e6760d6922b2c0f5d491cbaa752d000
fetched_at: '2026-06-28T22:42:13.614693+00:00'
product: protheus
section_id: 38310054605975
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Relatórios com exibição
  de baixas parciais
type: support-article
updated_at: '2026-04-02T12:22:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39422738912663-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Relat%C3%B3rios-com-exibi%C3%A7%C3%A3o-de-baixas-parciais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39422738881943)Tempo aproximado para leitura: 00:06 min**

**Dúvida**  
No módulo Contas a Receber, não é possível gerar relatórios que indiquem o pagamento parcial de um cliente.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Release 12.1.2210 e superiores  
  
**Solução**  
Alguns relatórios da linha FINR, utilizados em versões anteriores, foram descontinuados e não recebem mais manutenções ou suporte. Como evolução, foram desenvolvidos novos relatórios utilizando a ferramenta SmartView, que oferecem uma proposta moderna para a conferência.

Como alternativa dentro do novo modelo SmartView, podem ser utilizados os seguintes relatórios:

* **FINSV005 (Posição de Títulos a Receber):** Permite visualizar o saldo total do título e o valor já liquidado. Na coluna Saldo Líquido, é exibido o valor restante após as baixas, facilitando a identificação de títulos com pagamentos parciais, embora apresente uma visão consolidada e não o histórico detalhado de cada movimentação.
* **FINSV010 (Relação de Baixas):** Traz uma visão analítica e detalhada de cada baixa realizada. Este relatório garante a rastreabilidade, apresentando os respectivos valores de cada evento de baixa ocorrido no título.
* **FINSV013 (Posição de Títulos a Pagar):** Funciona de forma análoga ao FINSV005, voltado para a carteira de pagamentos.

**Segue um exemplo de utilização no Contas a Receber, onde um título possui 03 baixas parciais:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39422738883863)

**FINSV005 (Posição de Títulos a Receber):**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39422786358679)

**FINSV010 (Relação de Baixas):**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39422738886935)
