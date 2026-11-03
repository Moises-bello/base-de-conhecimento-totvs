---
content_hash: 5500fdf99e8a94c19c49d5f0f168a736f33c13eed13e050958ae481bbe39aca4
fetched_at: '2026-06-29T00:09:10.452826+00:00'
page_id: '397385156'
product: rm
source: tdn-rm
title: 3617768 FISCAL01-6132 DT Sped Fiscal Registro C176 campos 09, 12, 14, 15 e
  17
type: documentation
url: https://tdn.totvs.com/display/LRM/3617768+FISCAL01-6132+DT+Sped+Fiscal+Registro+C176+campos+09%2C+12%2C+14%2C+15+e+17
version: 1
---

# SPED Fiscal - Geração do Arquivo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | SPED Fiscal - Geração do Arquivo |
| **Situação/Requisito:** | Cliente entrou em contato informando que ao analisar o registro C176 gerado pelo sistema no PVA, identificou que os valores gerados estão divergentes do que é solicitado pelo manual do SPED Fiscal.  O mesmo informa que no próprio manual da rotina, informa que para os campos 09,12,13,14,15 e 17, devem ser gerados com o valor unitário do item referenciado.  Ou seja se o lançamento possui 1.000 itens, e o valor total da base de calculo do ICMS ST é 15.100,00 ao gerar a rotina, o campo "09" deveria ser gerado com o valor de 15.100,00 / 1.000 = 15,10. Dessa mesma forma para os outros campos 12,13,14,15 e 17 |
| **Solução/Implementação:** | Modificações na Geração do Registro C176 do Sped Fiscal:  O registro passou a gerar mais de um item desde que o item do lançamento de saída possua mais de uma referência.  O registro passa a ser gerado para todas as Operações de Saída em que o parâmetro ”Operação com Ressarcimento de ST na Compra” estiver habilitado no CFOP.  Os campos 09, 12, 14, 15 e 17 serão gerados considerando valor unitário do item referenciado. Ex: Base Calculo ICMS\Quantidade Prd do Item Referenciado ou Base Calculo ICMS ST\Quantidade Prd do Item Referenciado.  TAF  Ajuste na geração do registro T015AG conforme regra do Sped Fiscal |
| **Requisito:** | FIS000212 |
| **Documento de Referência:** |  |
