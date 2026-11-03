---
content_hash: 33f7c92910e153c881b66751b8c5f24d2b328b047c404b9638e2154caf5eab24
fetched_at: '2026-06-29T00:10:35.359715+00:00'
page_id: '528481672'
product: rm
source: tdn-rm
title: RMFIS00028_Registro_C600
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00028_Registro_C600
version: 3
---

# Geração do registro C500

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1 |
| **Ocorrência:** | Como gerar o registro C600 do EFD Contribuições |
| **Ambiente:** | CorporeRM |
| **Passo a passo:** | De acordo com o Manual do EFD Contribuições, o Registro C600 refere-se a Consolidação Diária de Notas Fiscais/Contas Emitidas de Energia Elétrica (Código 06), Nota Fiscal de Energia Elétrica Eletrônica – NF3e (Código 66), Nota Fiscal/Conta de Fornecimento D'água Canalizada (Código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) (Empresas Obrigadas ou não Obrigadas ao Convenio ICMS 115/03) – Documentos de Saída    Para geração do registro o sistema irá selecionar lançamentos de Saídas que possuam o Cod. Mod. Doc pertinente ao registro.  Obrigações Principais | Saídas.      O lançamento deve possuir PIS e CONFINS destacado no Item.       OBS: Caso seja informado na tela de geração da ROTINA que os lançamentos de energia elétrica serão gerados pela data de leitura, o sistema consistira esta data informada na Informações Adicionais - Energia \ Comunicação.        Trecho do arquivo gerado:  **|C600|06||5541|||1|0|09012020|2000,00|0,00||2000,00|0,00||0,00|0,00|0,00|0,00|0,00|13,00|60,00|** |C601||2000,00|2000,00|0,65|13,00|| |C605||2000,00|2000,00|3,00|60,00|| |
| **Observações:** | o C600 é um Registro diário, significando que o mesmo irá totalizar o valor do documento caso os seguintes campos forem iguais:  COD\_MOD, COD\_MUN, SER, SUB, COD\_CONS e DT\_DOC |
