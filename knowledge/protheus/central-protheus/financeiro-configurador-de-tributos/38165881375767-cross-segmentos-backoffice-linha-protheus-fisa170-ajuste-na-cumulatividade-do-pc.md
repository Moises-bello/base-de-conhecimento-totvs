---
article_id: 38165881375767
category: Financeiro - Configurador de Tributos
content_hash: 26ddcbb780c09d7b2e102f479bd0a0c372bb18c45aff104eee43283f3515a607
fetched_at: '2026-06-28T22:37:45.804805+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FISA170 - Ajuste na cumulatividade
  do PCC - Lei 13.137 de 2015
type: support-article
updated_at: '2026-03-30T12:04:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38165881375767-Cross-Segmentos-Backoffice-Linha-Protheus-FISA170-Ajuste-na-cumulatividade-do-PCC-Lei-13-137-de-2015
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38165825952663) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
A partir da Lei 13.137/2015, a retenção das contribuições sociais (PCC) deixou de ser baseada na cumulatividade mensal de pagamentos. A dispensa da retenção agora ocorre de forma **individualizada por pagamento**, sempre que o valor total das contribuições (somatória das alíquotas de 4,65%) for **igual ou inferior a R$ 10,00**.

Não se deve mais somar os títulos pagos ao mesmo fornecedor no dia ou no mês para atingir o limite. A análise é isolada para cada transação financeira.

**Exemplo Prático (Vários pagamentos no mesmo dia/mês):**

Considere três notas fiscais pagas ao **mesmo fornecedor** dentro de um único mês/dia:

| **Evento** | **Valor do Serviço** | **PCC (4,65%)** | **Retenção Obrigatória?** | **Justificativa** |
| --- | --- | --- | --- | --- |
| **Título 01 (Dia 05)** | R$ 200,00 | R$ 9,30 | **NÃO** | Valor do tributo R$ 10,00 |
| **Título 02 (Dia 15)** | R$ 215,00 | R$ 10,00 | **NÃO** | Valor do tributo = R$ 10,00 |
| **Título 03 (Dia 15)** | R$ 500,00 | R$ 23,25 | **SIM** | Valor do tributo maior que R$ 10,00 |

**Análise do Exemplo:**

Mesmo que no dia 15 ocorram dois pagamentos que, somados, resultariam em R$ 33,25 de imposto, a retenção **não é aplicada sobre a soma (cumulatividade)**

Conforme as Soluções de Consulta COSIT nº 22/2022 e nº 258/2024, deve-se considerar apenas o valor de cada pagamento isolado. No cenário acima, apenas o **Título 03** sofre a retenção de R$ 23,25.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.2210  
  
**Solução**  
Como é feita a configuração da regra de retenção para atender a Lei 13.137 de 2015:

Boletim:

[Configuração regra de cumulatividade por documento fiscal](https://tdn.totvs.com/pages/releaseview.action?pageId=1023310280)

* Na regra de retenção, selecione os campos conforme regra de cumulatividade que deseja, mas no campo FKO\_CUMUL, selecione a opção 4 - Por Documento fiscal.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38165881364247)

|  |  |
| --- | --- |
| Tipo Cumulat | Define como será realizada a cumulatividade de valores de um imposto.  1 – Por Tipo de Imposto 2 – Por Regras Financeiras 3 – Por Tipo de Imposto + Regras Financeiras 4 – Por Documento Fiscal |

Essa opção estará disponível a partir da Expedição Contínua de Fevereiro de **2026**e possibilitará a base individual por documento fiscal para cumulatividade de impostos do **PCC.**

Caso queira utilizar a cumulatividade do PCC da forma antiga, deverá utilizar as demais opções.

**Saiba mais:**

[**PCC - Novas Regras de Retenção - Lei 13.137/2015**](https://tdn.totvs.com/pages/releaseview.action?pageId=344461389)

[**Cross Segmento - Backoffice Linha Protheus - FISA170 - Configurador de tributos**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34975309866135-Cross-Segmento-Backoffice-Linha-Protheus-FISA170-Configurador-de-tributos)

[**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - How to configurador de tributos regra financeira**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33852958399767-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-How-to-configurador-de-tributos-regra-financeira)

[Configurador de tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)
