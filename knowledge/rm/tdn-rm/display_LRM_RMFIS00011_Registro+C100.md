---
content_hash: 8a17ee71c9fc8c88d24e4b0ce687a36240f9989c553331ecea9362018b5479d7
fetched_at: '2026-06-29T00:08:44.000293+00:00'
page_id: '307837408'
product: rm
source: tdn-rm
title: RMFIS00011_Registro C100
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00011_Registro+C100
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.7 |
| **Ocorrência:** | Parametrização do Registro C100 - EFD Contribuições. |
| **Ambiente:** |  |
| **Passo a passo:** | Este registro deve ser gerado para cada documento fiscal código 01, 1B, 04, 55 e 65 (NFC-e), registrando a entrada ou saída de produtos ou outras situações que envolvam a emissão dos documentos fiscais mencionados, representativos de receitas auferidas, tributadas ou não pelo PIS/Pasep ou pela Cofins, bem como de operações de aquisições e/ou devoluções com direito a crédito da não cumulatividade.     * Para o tipo de documento informado no lançamento fiscal - Deve existir código de modelo de documento e este deve ser pertinente a rotina;          * Na Natureza de Operação, o flag fiscal deve estar marcado;        * Item vinculado do Tipo: Produto;        * Nos itens do lançamento os tributos PIS e COFINS destacados de acordo com a operação;       Segue abaixo resultado do exemplo:    |C001|0| |C010|21867387000158|2| |C100|1|0|GC00013|55|00|1|000004545||19102017|19102017|5000,00|2|0,00||5000,00||0,00|0,00|0,00|5000,00|600,00|0,00|0,00|0,00|32,50|380,00||| |C170|1|01.01||1,00000|UN|5000,00|0,00|0|100|5101|510101|5000,00|12,00|600,00|0,00|0,00|0,00||||0,00|0,00|0,00|01|5000,00|0,6500|||32,50|01|5000,00|7,6000|||380,00|| |C990|5|    **Observação:**    Não devem ser informados documentos fiscais que não se refiram a operações geradoras de receitas ou de créditos de PIS/Pasep e de Cofins.    Para cada registro C100, obrigatoriamente deve ser apresentado, pelo menos, um registro C170, exceto em relação aos documentos fiscais referentes à nota fiscal cancelada (código “02” ou “03”), Nota Fiscal Eletrônica (NF-e) denegada (código “04”) ou numeração inutilizada (código “05”), os quais não devem ser escriturados os registros filhos de C100. |
| **Observações:** |  |
