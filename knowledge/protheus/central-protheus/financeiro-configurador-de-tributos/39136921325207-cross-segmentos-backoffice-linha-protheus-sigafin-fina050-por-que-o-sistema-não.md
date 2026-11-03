---
article_id: 39136921325207
category: Financeiro - Configurador de Tributos
content_hash: 10fc0be5d5b54a9b83a7d9ee50256cacf4e98807b6e5ecd7b2e230a23406a4c2
fetched_at: '2026-06-28T22:37:45.817586+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Por que o
  sistema não calcula a cumulatividade de IR sobre Lucros e Dividendos de forma automática
  via rotina legada para valores menores que R$ 50.000,00 ?
type: support-article
updated_at: '2026-03-23T22:08:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39136921325207-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Por-que-o-sistema-n%C3%A3o-calcula-a-cumulatividade-de-IR-sobre-Lucros-e-Dividendos-de-forma-autom%C3%A1tica-via-rotina-legada-para-valores-menores-que-R-50-000-00
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39136921306135) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**

Por que o sistema não calcula a cumulatividade de IR sobre Lucros e Dividendos de forma automática, via rotina legada, para valores menores que R$ 50.000,00 ?

**Exemplo 1**

Ao lançar um título 01 no valor de R$ 20.000,00 (natureza sem retenção), em seguida um título 02 no valor de R$ 35.000,00 (natureza com retenção -10%) o sistema não acumula as bases, e só retem os 10% somente sobre os R$ 35.000,00 conforme demonstração a seguir:

[![LEGADO CUMULATIV LUCROS E DIVIDENDOS 2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39136921307159)](https://centraldeatendimento.totvs.com/hc/article_attachments/39136921307159)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir 12.1.2410

**Solução:**

Esse comportamento ocorre porque a rotina legada que é configurado os impostos pelo cadastro de natureza e fornecedor do Protheus **(FINA050)** não foi adaptada para calcular a cumulatividade de Lucros e Dividendos de forma automática.

A recomendação oficial da TOTVS para o cálculo automático e tratamento adequado da cumulatividade de IR sobre Lucros e Dividendos é a utilização do Configurador de Tributos **(FISA170)**.

Caso opte por continuar utilizando a rotina legada, o processo deve ocorrer totalmente de forma manual, neste cenário, terá que calcular e digitar o valor do IR de R$ 5.500,00 manualmente.

Para automatizar o processo de cumulatividade de IR sobre Lucros e Dividendos, parametrize e passe a utilizar o Configurador de Tributos **(FISA170)** em substituição à rotina legada.

## 

## **Configurador de Tributos - Cumulatividade de IR para Lucros e Dividendos de forma automática**

Para que o cálculo de IR sobre Lucros e Dividendos ocorra de forma automática e considere a cumulatividade corretamente, a TOTVS recomenda a utilização do Configurador de Tributos (FISA170).

Através dessa rotina, o sistema controla o valor mínimo para retenção, e acumula a base de cálculo conforme as baixas dos títulos vinculados ao mesmo Fornecedor/Cliente.

Abaixo demonstramos o funcionamento prático do cenário acima, a cumulatividade automática do IR, para os valores menores que R$ 50.000,00

**Solução**

1. **Lançar um titulo 01 (R$ 20.000,00).** Ao realizar a baixa deste primeiro título, o sistema identificará que o valor (R$ 20.000,00) está abaixo do mínimo para retenção estipulado (R$ 50.000,00). Portanto, **não haverá retenção** de IR nesta etapa.
2. **Lançar um título 02 (R$ 35.000,00)** Ao efetuar a baixa do segundo título, o Configurador de Tributos reconhecerá a cumulatividade e somará o valor do Título 01 ao Título 02 para compor a nova base de cálculo (R$ 20.000,00 + R$ 35.000,00 = **R$ 55.000,00**).
3. **Cálculo da Retenção:** Como a base acumulada (R$ 55.000,00) ultrapassou o teto mínimo de isenção, o sistema aplicará a alíquota de 10% sobre o valor total acumulado.
4. **Resultado:** O sistema fará a retenção automática do imposto no momento da baixa do segundo título, totalizando **R$ 5.500,00** de IR sobre Lucros e Dividendos.

**Exemplo 2**

[![FISA170 CUMULATIV LUCROS E DIVIDENDOS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39136921307671)](https://centraldeatendimento.totvs.com/hc/article_attachments/39136921307671)

**Saiba mais:**

[FISA170 - Configurando o IR para lucros/dividendos](https://tdn.totvs.com/pages/releaseview.action?pageId=1043719216)

[Reforma do Imposto de Renda 2026 - Tributação sobre a distribuição de lucros e dividendos para titulo com o origem do modulo Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37565957361815-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Lei-15-270-2025-Reforma-do-Imposto-de-Renda-2026-Tributa%C3%A7%C3%A3o-sobre-a-distribui%C3%A7%C3%A3o-de-lucros-e-dividendos-para-titulo-com-o-origem-do-modulo-Financeiro)

[Configurador de tributos - Regras Financeiras](https://tdn.totvs.com.br/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)
