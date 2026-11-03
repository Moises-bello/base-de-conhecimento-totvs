---
content_hash: bb25f7f94683f5447609ec1e1791095035a865d3a7bf4cd556c50b3b3b87b02e
fetched_at: '2026-06-29T00:08:49.593110+00:00'
page_id: '331846049'
product: rm
source: tdn-rm
title: RMFIS00014_Registro M410 e M810
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00014_Registro+M410+e+M810
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.X. |
| **Ocorrência:** | Parametrização dos Registros M410 e M810 - EFD Contribuições. |
| **Ambiente:** |  |
| **Passo a passo:** | Este registro será gerado por pessoas jurídica, para consolidar as receitas não sujeitas ao pagamento da contribuição social, com base nos CST específicos: (04, 05 - com alíquota zero, 06, 07, 08 e 09) informados nas receitas relacionadas nos Blocos A, C, D e F.    **Registro M400 – Receitas Isentas, Não alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota zero ou de Vendas com Suspensão PIS/PASEP**  **M410: Detalhamento das Receitas Isentas, não Alcançadas pela Incidência da** **Contribuição, Sujeitas a Alíquota Zero ou de Vendas com Suspensão – PIS/PASEP**  **Registro M800 – Receitas Isentas, Não alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota zero ou de Vendas com Suspensão COFINS**  **Registro M810: Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da** **Contribuição, Sujeitas a Alíquota Zero ou de Vendas com Suspensão – COFINS**      Abaixo será demonstrando qual a consistência que o sistema apresenta para que os registros sejam gerados corretamente no arquivo do EFD Contribuições a ser validado no PVA da Receita Federal.    Para que os registros sejam gerados com os seus respectivos campos corretamente preenchidos, deverá ser levado em consideração as seguintes regras:  - Será gerado neste registro, somente os lançamentos fiscais cujo CST do PIS/COFINS, esteja preenchido como:   * 04 - Operação Tributável Monofásica - Revenda a Alíquota Zero, * 05 - Operação Tributável por Substituição Tributária, * 06 - Operação Tributável a Alíquota Zero, * 07 - Operação Isenta da Contribuição, * 08 - Operação sem Incidência da Contribuição, * 09 - Operação com Suspensão da Contribuição,           **- Para o preenchimento do campo “NAT\_REC”, o sistema irá consistir na informação contida no lançamento fiscal:  Itens > Outros dados > Natureza da Receita.**  *Exemplo:*      Para o correto preenchimento do código da natureza da receita, deverá ser levado em consideração as tabelas disponibilizadas no site da Receita Federal.    Link: <http://sped.rfb.gov.br/pasta/show/1616>    Informações das tabelas:   * Para o **CST 04 – Operação Tributável Monofásica – Revenda a Alíquota Zero**, utilize os códigos constantes nas tabelas 4.3.10: Produtos Sujeitos à Incidência Monofásica da Contribuição Social – Alíquotas Diferenciadas e 4.3.11: Produtos Sujeitos à Incidência Monofásica da Contribuição Social – Alíquotas por Unidade de Medida de Produto. * Para o **CST 05 (e alíquota zero) – Operação Tributável por Substituição Tributária**, utilize os códigos da Tabela 4.3.12: Produtos Sujeitos à Substituição Tributária da Contribuição Social. * Para o **CST 06 – Operação Tributável a Alíquota Zero**, utilize os códigos da Tabela 4.3.13: Produtos Sujeitos à Alíquota Zero da Contribuição Social. * Para o **CST 07 – Operação Isenta da Contribuição**, utilize os códigos da Tabela 4.3.14: Operações com Isenção da Contribuição Social. * Para o **CST 08 – Operação sem Incidência da Contribuição**, utilize os códigos da Tabela 4.3.15: Operações sem Incidência da Contribuição Social. * Para o **CST 09 – Operação com Suspensão da Contribuição**, utilize os códigos da Tabela 4.3.16: Operações com Suspensão da Contribuição Social.       Segue abaixo exemplo do resultado do lançamento fiscal:    |M001|0|  |M400|07|1000,00|2.1.1.1.003||  |M410|201|1000,00|2.1.1.1.003||  |M800|07|1000,00|2.1.1.1.003||  |M810|201|1000,00|2.1.1.1.003|| |
| **Observações:** |  |
