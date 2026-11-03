---
content_hash: dc7a6606e379e7d64542e290a83088f43c6ad5cece34ee297cff19426fd24741
fetched_at: '2026-06-29T00:08:43.655275+00:00'
page_id: '305923753'
product: rm
source: tdn-rm
title: RMFIS00010_Registro A100
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00010_Registro+A100
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.7 |
| **Ocorrência:** | Parametrização do Registro A100 - EFD Contribuições. |
| **Ambiente:** |  |
| **Passo a passo:** | Deve ser gerado um Registro A100 para cada documento fiscal a ser relacionado na escrituração, referente à prestação ou à contratação de serviços, que envolvam a emissão de documentos fiscais estabelecidos pelos Municípios, eletrônicos ou em papel.     * Para o tipo de documento informado no lançamento fiscal - não pode ter código de modelo do documento informado;          * No cadastro da Natureza de Operação/ aba de identificação/ Não pode ter flag fiscal marcado;          * Item vinculado do Tipo: Serviço;            * Os tributos PIS e COFINS destacados nos itens do lançamento de acordo a operação;         Segue abaixo resultado do exemplo:    |A001|0| |A010|21867387000158| |A100|0|1|F00002|00|1||000454545||09102017|09102017|3500,00|9|0,00|0,00|0,00|0,00|0,00|||0,00| |A170|1|09.90||3500,00|0,00||0|50|0,00|0,00|0,00|50|0,00|0,00|0,00||| |A990|5|     * Para cada registro A100, obrigatoriamente deve ser apresentado, pelo menos, um registro A170.     **Observação:**    Para documento fiscal de serviço cancelado (código da situação = 02), somente podem ser preenchidos os campos de código da situação, indicador de operação, emitente, número do documento, série, subsérie e código do participante. Os campos série e subsérie não são obrigatórios e o campo código do participante é obrigatório nas operações de contratação de serviços. |
| **Observações:** |  |
