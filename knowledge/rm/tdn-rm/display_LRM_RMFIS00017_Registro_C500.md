---
content_hash: d0947f391f9a7fdad6262e17ad81806c121dc1244f67b7eac40dca0660753287
fetched_at: '2026-06-29T00:09:09.206651+00:00'
page_id: '393352260'
product: rm
source: tdn-rm
title: RMFIS00017_Registro_C500
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00017_Registro_C500
version: 3
---

# Geração do registro C500

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1 |
| **Ocorrência:** | Como gerar o registro C500 do EFD Contribuições |
| **Ambiente:** | CorporeRM |
| **Passo a passo:** | De acordo com o Manual do EFD Contribuições, o Registro C500 refere-se a Nota Fiscal/Conta de Energia Elétrica (Código 06), Nota Fiscal de Energia Elétrica Eletrônica – NF3e (Código 66), Nota Fiscal/Conta de fornecimento D’água Canalizada (Código 29), Nota Fiscal/Consumo Fornecimento de Gás (Código 28) e NF-e (Código 55) – Documentos de Entrada / Aquisição com Crédito    Para geração do registro o sistema irá selecionar lançamentos de Entrada que possuam o Cod. Mod. Doc pertinente ao registro.  Obrigações Principais | Entrada.      A CFOP deve ser fiscal e o código pertinente ao fornecimento de Energia Elétrica, Gás ou Água.  Serão consideradas as CFOPs abaixo:  "1252","2252","1253","2253","1254","2254","1255","2255","1256","2256","1257","2257","1305","2305","1355","2355","3355"      O lançamento deve possuir PIS e CONFINS destacado no Item.       OBS: Caso seja informado na tela de geração da ROTINA que os lançamentos de energia elétrica serão gerados pela data de leitura, o sistema consistira esta data informada na Informações Adicionais - Energia \ Comunicação.        Trecho do arquivo gerado:  |C010|53113791000122|2|  **|C500|GF00009|06|00|1||255225|20082018|20082018|1000,00|180,00||6,50|30,00||**  |C501|50|1000,00|07|1000,00|0,65|6,50|2| |C505|50|1000,00|07|1000,00|3,00|30,00|2| |
| **Observações:** |  |
