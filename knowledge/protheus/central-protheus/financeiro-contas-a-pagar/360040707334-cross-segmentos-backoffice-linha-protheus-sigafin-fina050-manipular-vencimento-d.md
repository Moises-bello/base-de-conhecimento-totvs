---
article_id: 360040707334
category: Financeiro - Contas a Pagar
content_hash: 35dabb09397a067827f1b280657fda91c0901cc4c7a725755dc5b31c13052e2f
fetched_at: '2026-06-28T22:38:08.575434+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Manipular
  vencimento dos impostos
type: support-article
updated_at: '2025-09-12T17:42:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040707334-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Manipular-vencimento-dos-impostos
---

**Dúvida**É possível manipular a data de vencimento dos impostos de um título?  
  
 **Ambiente**Microsiga Protheus - Financeiro - FINA050 - Todas as versões.  
  
**Solução:**

No padrão do sistema, a definição da **data de vencimento dos impostos** é controlada por parâmetros.

**Parâmetros padrões:**  
Para consultar quais parâmetros são utilizados pelo sistema, acesse a documentação oficial: [Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Vencimento de imposto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411217267735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Vencimento-de-imposto)

Atualmente, o sistema disponibiliza o ponto de entrada:

* **[F050MDVC – Cálculo da data de vencimento de imposto](https://tdn.totvs.com/pages/releaseview.action?pageId=6070892)s**  
  Este PE permite que o cliente personalize a regra de cálculo da data de vencimento.  
  Ele pode ser utilizado, por exemplo, para impostos como **IRRF, INSS e PCC**.

O **imposto de ISS** **não é contemplado** pelo ponto de entrada F050MDVC.  
O seu vencimento é controlado **exclusivamente por parâmetros**:

**MV\_DIAISS -**Define o dia padrão para gerar os títulos de ISS.

Exemplo: se preenchido com *10*, o sistema fixará o dia 10 como vencimento.

**MV\_VENCISS**-

Define o tipo de vencimento do ISS:

* **E** = Emissão
* **Q** = Quinzenal/Emissão
* **V** = Vencimento
* **F** = Se a data de emissão for menor que 15 (primeira quinzena) a data de vencimento será 15  somados ao conteúdo  MV\_DIAISS (considerando o primeiro dia do mês na conta), se a data de emissão for maior que 15 (segunda quinzena) será no dia informado no **MV\_DIAISS** do mês subsequente.

**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Configuração e parâmetros do imposto ISS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018436431-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Configura%C3%A7%C3%A3o-e-par%C3%A2metros-do-imposto-ISS)
