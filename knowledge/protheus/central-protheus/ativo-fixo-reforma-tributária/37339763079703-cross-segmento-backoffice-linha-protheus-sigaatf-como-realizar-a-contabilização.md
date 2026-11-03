---
article_id: 37339763079703
category: Ativo fixo - Reforma Tributária
content_hash: aa16efa2553d55064f718db1d7f0b48e09e4e88fa1ff3eb2e85f6bacd9a1bd7c
fetched_at: '2026-06-28T22:41:35.576444+00:00'
product: protheus
section_id: 37095895776791
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Como realizar a contabilização
  de Estorno de crédito CBS/IBS na baixa do Ativo Imobilizado?
type: support-article
updated_at: '2025-12-30T13:53:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37339763079703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Como-realizar-a-contabiliza%C3%A7%C3%A3o-de-Estorno-de-cr%C3%A9dito-CBS-IBS-na-baixa-do-Ativo-Imobilizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37339763071767) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como realizar a contabilização de Estorno de crédito CBS/IBS na baixa do Ativo Imobilizado conforme a Reforma Tributária?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - Todas as versões  
  
**Solução**  
Para calcular o valor proporcional de estorno de crédito de IBS/CBS em casos de baixa, inutilização ou perda de bens do ativo imobilizado, devem ser seguidos os critérios definidos pela LC 214/2025.

O cálculo deve considerar a vida útil do bem (taxa de depreciação), o tempo de uso até a data da baixa e o percentual baixado (no caso de baixas parciais).

**1. Fórmula utilizada no Lançamento Padrão (LP 810)**

A fórmula abaixo pode ser utilizada para automatizar o cálculo do estorno:  
  
CTBVLTRIB(SN1->N1\_IDTRIB,"IBSEST",,.T.)\*SN4->N4\_QUANTD\*(1-((SN4->N4\_DATA-SN1->N1\_AQUISIC)/((100/SN3->N3\_TXDEPR1)\*365)))  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340130826903)

**Descrição dos componentes:**

| Campo / Função | Descrição |
| --- | --- |
| CTBVLTRIB(SN1->N1\_IDTRIB,"IBSEST",,.T.) | Retorna o valor total do crédito tributário (IBS/CBS) registrado na aquisição do bem. |
| SN4->N4\_QUANTD | Representa o percentual fracionado da quantidade baixada (ex: 0,4 equivale a 40%). |
| SN4->N4\_DATA | Data em que a baixa do ativo foi realizada. |
| SN1->N1\_AQUISIC | Data da aquisição do bem no sistema. |
| SN3->N3\_TXDEPR1 | Taxa de depreciação anual cadastrada para o bem (em %). |
| 365 | Fator de conversão da taxa anual em dias para o cálculo proporcional. |

**2. Lógica do Cálculo**

O estorno é composto por duas proporções principais:

1. **Proporção da quantidade baixada:** A fração do bem que está sendo baixada no momento.  
   Exemplo:  N4\_QUANTD = 0,4 → o bem está sendo baixado em 40%.
2. **Proporção do crédito remanescente:** Indica quanto do crédito ainda não foi "consumido" pela depreciação (calculado como: 1 - (tempo de uso / vida útil total))

**3. Exemplo Prático**

Considere o seguinte cenário:

* **Valor total do crédito IBS:** R$ 1.000,00
* **Data de aquisição:** 01/01/2023
* **Data da baixa:** 01/01/2025
* **Taxa de depreciação:** 25% a.a.
* **Percentual baixado:** 40% (0,4)

**Passo a passo do cálculo:**

1. **Vida útil total:** 100 ÷ 25% = 4 anos (1460 dias).
2. **Tempo de uso:** 01/01/2025 − 01/01/2023 = 730 dias.
3. **Proporção remanescente:** 1 − (730 ÷ 1460) = 0,5 (ou 50%).
4. **Cálculo Final (Estorno):** R$ 1.000,00 (Crédito) × 0,4 (Baixa) × 0,5 (Remanescente) = **R$ 200,00**.

**Importante** Os exemplos apresentados têm caráter meramente ilustrativo e servem como sugestão. Caso o cenário real da empresa possua particularidades — como diferentes métodos de depreciação ou políticas internas —, é indispensável ajustar a fórmula conforme a realidade operacional e as regras fiscais aplicáveis.

**Saiba Mais**  
[Contabilização Estorno de crédito CBS/IBS](https://tdn.totvs.com/pages/releaseview.action?pageId=1012515671)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como Contabilizar IBS, CBS e IS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36639180648983-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-Contabilizar-IBS-CBS-e-IS)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Contabilização com Base na Classificação do Tributo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37097599152663-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-Base-na-Classifica%C3%A7%C3%A3o-do-Tributo)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Contabilização com Base na Sigla do Tributo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37100272710039-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-Base-na-Sigla-do-Tributo)
