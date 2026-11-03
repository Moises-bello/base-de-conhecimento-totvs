---
content_hash: 53776468fc6ce087e96af528e8704d0288f8d0d4795a91b4c473e2dc5067af75
fetched_at: '2026-06-29T00:11:26.434444+00:00'
page_id: '716369799'
product: rm
source: tdn-rm
title: tipoAjuste
type: documentation
url: https://tdn.totvs.com/display/LRM/tipoAjuste
version: 1
---

## Tipo do ajuste da CPRB

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| tipoAjuste | tipoCod | 0-N | - | Registro a ser preenchido caso a pessoa jurídica tenha de proceder a ajustes da contribuição apurada no período, decorrentes da legislação tributária da contribuição, de estorno ou de outras situações. | Este grupo será gerado com os lançamentos de Outros Débitos/Créditos inseridos para o Tributo "Contribuição Previdenciária" no período. |
| tpAjuste | tipoAjuste | 1-1 | 1 | Preencher com o código correspondente ao tipo de ajuste:  Valores Válidos: 0- Ajuste de redução; 1- Ajuste de acréscimo | Se o lançamento for de Crédito, recebe valor “0”.  Se for do Tipo Débito recebe valor “1”. |
| codAjuste | tipoAjuste | 1-1 | 2 | Preencher com o código de ajuste:  Valores Válidos: 1 - Ajuste da CPRB: Adoção do Regime de Caixa 2 - Ajuste da CPRB: Diferimento de Valores a recolher no período 3 - Adição de valores Diferidos em Período(s) Anteriores(es). 4 - Exportações diretas 5  -Transporte internacional de cargas 6 -  Vendas canceladas e os descontos incondicionais concedidos 7 - IPI, se incluído na receita bruta 8 - ICMS, quando cobrado pelo vendedor dos bens ou prestador dos serviços na condição de substituto tributário 9 -  Receita bruta reconhecida pela construção, recuperação, reforma, ampliação ou melhoramento da infraestrutura, cuja contrapartida seja ativo intangível representativo de direito de exploração, no caso de contratos de concessão de serviços públicos 10 - O valor do aporte de recursos realizado nos termos do art 6 §3 inciso III da Lei 11.079/2004 11 - Demais ajustes oriundos da Legislação Tributária, estorno ou outras situações. | Recebe o valor gravado no campo "Código Ajuste SPED" da tela de inclusão de Outros Débitos e Créditos. |
| vlrAjuste | tipoAjuste | 1-1 | 14 | Valor do ajuste | Recebe o valor do lançamento de Outros Débitos/Créditos |
| descAjuste | tipoAjuste | 1-1 | 20 | Descrição resumida do ajuste | Recebe o valor do campo Histórico do lançamentos de Outros Débitos/Créditos. |
| dtAjuste | tipoAjuste | 1-1 | 7 | Informar o mês/ano (formato AAAA-MM) de referência do ajuste  Validação: Deve ser um mês/ano válido. | Não aderência. |
