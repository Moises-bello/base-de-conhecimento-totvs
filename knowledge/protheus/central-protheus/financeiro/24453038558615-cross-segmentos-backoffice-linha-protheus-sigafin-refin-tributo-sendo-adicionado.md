---
article_id: 24453038558615
category: Financeiro
content_hash: a16708a53b8648277d1469b286952776c1f7470037a4b6488d3ef7481bd172ba
fetched_at: '2026-06-28T22:38:03.429423+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REFIN - Tributo sendo
  adicionado de forma manual no título
type: support-article
updated_at: '2024-06-26T18:59:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24453038558615-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REFIN-Tributo-sendo-adicionado-de-forma-manual-no-t%C3%ADtulo
---

Dúvida

Se o valor do tributo for preenchido manualmente no título, será considerado no REINF?

Ambiente

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Apartir da 12.1.33

**Exemplo**

Caso o título a pagar não tiver a configuração para o calculo do sistema para IR, PIS, COFINS e CSLL (configuração dos cadastros de fornecedor e natureza financeira), e os valores dos impostos forem preenchidos manualmente no título, não serão considerados pelo Extrator Fiscal.

**Saiba mais sobre o preenchimento automático dos impostos**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular o IRRF para notas de entrada e saída?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025517971-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-IRRF-para-notas-de-entrada-e-sa%C3%ADda)

[Cross Segmento - Backoffice Linha Protheus - Parâmetros para ajustes de Retenção de PCC no Módulo (06) Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027163451-Cross-Segmento-Backoffice-Linha-Protheus-Par%C3%A2metros-para-ajustes-de-Reten%C3%A7%C3%A3o-de-PCC-no-M%C3%B3dulo-06-Financeiro)  
  
   
**Importante**  
Caso o título possua os cadastros de natureza financeira (SED) e fornecedor (SA2) devidamente configurados para o calculo de IR, PIS, COFINS ou CSLL e os valores calculados forem modificados manualmente, os mesmos serão considerados na gravação da tabela FKW e consequentemente no Extrator Fiscal;  
**Esse procedimento não é recomendado e pode causar divergências de valores no REINF;**

Os títulos de impostos inseridos no sistema de forma avulta (exemplo: incluir um título do tipo TX sem vinculo com um título principal), não serão considerados pelo Extrator Fiscal.

**Saiba mais:**

[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)
