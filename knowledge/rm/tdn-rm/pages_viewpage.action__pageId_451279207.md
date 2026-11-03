---
content_hash: 76cdb23e12d47770b8c1c9abfbc899322006abcc53d7ebc7cf6faa4a6c322209
fetched_at: '2026-06-29T00:09:58.238850+00:00'
page_id: '451279207'
product: rm
source: tdn-rm
title: 4238826 FISCAL01-7081 DT Evento tributário - Considerar a base de cálculo para
  calcular o Adicional do IRPJ
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451279207
version: 9
---

# Evento tributário - Considerar a base de cálculo para calcular o Adicional do IRPJ

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Apuração do IRPJ |
| **Situação/Requisito:** | Cliente solicita que seja considerado o Lucro Real após compensação para calculo do Lucro da Exploração. |
| **Solução/Implementação:** | Foi alterado o cálculo do Evento Tributário para considerar o Lucro Real Após as compensações (Base de Cálculo) para o calcular a proporção do adicional do IRPJ nas receitas por atividade do Lucro da Exploração.  O cálculo passa a ser gerado conforme abaixo:  **SE** (Base de Cálculo) < (Lucro da Exploração)  **Então**Valor do Adicional de IRPJ = (Receita líquida da atividade \* Adicional do IRPJ) / Total das receitas por atividade  **Senão**Valor do Adicional de IRPJ = (Parcela do lucro da exploração ref atividade \* Adicional do IRPJ) / Base de Cálculo 11Exemplo 1 Considere os valores apurados:   |  |  | | --- | --- | | Receita Liquida por Atividade | 1.530.335,23 | | Total das receitas por atividade | 31.201.715,06 | | Valor do Adicional de IRPJ | 1.466.567,91 | | Lucro da Exploração | 20.892.320,34 | | Base de Cálculo | 14.725.679,06 | | Parc. Lucro Exploração Atividade | 1.024.695,40 |   Neste caso o adicional será calculado da seguinte forma  Valor do Adicional de IRPJ = (Receita líquida da atividade \* Adicional do IRPJ) / Total das receitas por atividade  Valor do Adicional de IRPJ = (1.530.335,23 \* 1.466.567,91) / 31.201.715,06  Valor do Adicional de IRPJ = 71.930,04 2Exemplo 2 Considere os valores apurados:   |  |  | | --- | --- | | Receita Liquida por Atividade | 1.530.335,23 | | Total das receitas por atividade | 31.201.715,06 | | Valor do Adicional de IRPJ | 2.097.411,30 | | Lucro da Exploração | 20.892.320,34 | | Base de Cálculo | 21.034.112,95 | | Parc. Lucro Exploração Atividade | 1.024.695,40 |   Neste caso o adicional será calculado da seguinte forma  Valor do Adicional de IRPJ = (Parcela do lucro da exploração ref atividade \* Adicional do IRPJ) / Base de Cálculo  Valor do Adicional de IRPJ = (1.024.695,40 \* 2.097.411,30) / 21.034.112,95  Valor do Adicional de IRPJ = 102.177,24 |
