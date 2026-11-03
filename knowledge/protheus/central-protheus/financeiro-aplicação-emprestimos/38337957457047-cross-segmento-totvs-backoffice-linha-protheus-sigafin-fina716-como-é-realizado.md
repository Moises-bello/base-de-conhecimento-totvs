---
article_id: 38337957457047
category: Financeiro - Aplicação / Emprestimos
content_hash: 8cabee635fbfb7bbf03a220822f7c4b661b6e0ec9084f6bf38eca0e2b84a196b
fetched_at: '2026-06-28T22:37:59.456933+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) SIGAFIN - FINA716 - Como
  é realizado o cálculo e a retenção do IOF em operações de Empréstimo
type: support-article
updated_at: '2026-03-18T13:25:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38337957457047-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-realizado-o-c%C3%A1lculo-e-a-reten%C3%A7%C3%A3o-do-IOF-em-opera%C3%A7%C3%B5es-de-Empr%C3%A9stimo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38337957416727) Tempo aproximado para leitura: **00:05:00**  
  
**Dúvida**

Como é realizado o cálculo e a retenção do **IOF** em operações de Empréstimo através da rotina **FINA716**, e por que ele não é calculado de forma separada no momento do resgate/liquidação como ocorre em Aplicações Financeiras?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
No Protheus, a rotina **FINA716** trata as operações de empréstimos (onde a empresa é a tomadora dos recursos) de forma distinta das aplicações financeiras.

Diferente de uma aplicação (onde o IOF incide sobre o rendimento e é retido no resgate), no **Empréstimo**, o IOF (Imposto sobre Operações Financeiras) incide sobre o valor total do crédito disponibilizado.

**Responsabilidade do Cálculo:**

O banco (instituição financeira) é o responsável por calcular o imposto e recolhê-lo ao Governo Federal.

**Repasse ao Tomador:**

O valor do IOF é repassado ao cliente (tomador) já no ato da contratação, sendo geralmente financiado junto ao valor principal ou descontado do valor líquido liberado em conta.

**Composição do Título:**

No sistema, o valor do IOF compõe o Custo Efetivo da Operação. Portanto, as parcelas geradas no Financeiro já contemplam o valor do IOF diluído ou incorporado ao saldo devedor, não havendo um cálculo de IOF "extra" ou separado no momento da liquidação das parcelas (resgate do passivo).

**Regras de IOF em Empréstimos:**  
IOF Diário**:** Calculado sobre o saldo devedor por dia de permanência (limitado a 365 dias).  
IOF Adicional: Uma alíquota fixa (atualmente 0,38%) aplicada sobre o valor total da operação, independentemente do prazo.

**Contrato de Empréstimo**

No exemplo abaixo podemos observar no contrato que foi informado um valor de IOF, valor este que irá compor o custo efetivo da operação.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38337942035095)](https://centraldeatendimento.totvs.com/hc/article_attachments/38337942035095)

**Resgate**

No momento do resgate, pagamento da parcela 1, podemos observar que não teve cálculo de IOF extra apenas o valor da parcela com os custos e despesas diluídos no contrato.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38337957421079)](https://centraldeatendimento.totvs.com/hc/article_attachments/38337957421079)[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38337942037783)](https://centraldeatendimento.totvs.com/hc/article_attachments/38337942037783)

**Saiba mais**

[FINA716 - Aplicações e Emprestimos](https://tdn.totvs.com/pages/viewpage.action?pageId=684987254)

[Contrato de Emprestimo com IOF incluso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27463706818455-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA716-Empr%C3%A9stimo-Price-n%C3%A3o-bate-as-parcelas-como-posso-fazer-as-parcelas-baterem-com-o-contrato-quando-possui-IOF-despesa-e-car%C3%AAncia)
